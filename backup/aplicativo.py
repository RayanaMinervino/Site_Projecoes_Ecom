from flask import Flask, render_template, request, jsonify
import pyodbc
from datetime import datetime

app = Flask(__name__)

# Configuração da conexão
def conectar():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=servidorprojecaoecom.database.windows.net;'
        'DATABASE=projecao_db;'
        'UID=rayaanminervinoecom;'
        'PWD=Novasenha123@;'
    )

@app.route('/')
def index():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT Data, Valor FROM ProjecaoVendas ORDER BY Data")
    dados = []

    for row in cursor.fetchall():
        data_str = str(row[0])
        if " " in data_str:
            data_formatada = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
        else:
            data_formatada = data_str  # já está no formato correto
        dados.append({"Data": data_formatada, "Valor": row[1]})

    conn.close()
    return render_template("index.html", dados=dados)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    data = request.json['data']
    valor = float(request.json['valor'])
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ProjecaoVendas (Data, Valor) VALUES (?, ?)", data, valor)
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Dados adicionados com sucesso!"})

@app.route('/editar', methods=['POST'])
def editar():
    data = request.json['data']
    valor = float(request.json['valor'])
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE ProjecaoVendas SET Valor = ? WHERE Data = ?", valor, data)
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Dados atualizados com sucesso!"})

@app.route('/excluir', methods=['POST'])
def excluir():
    data = request.json['data']
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ProjecaoVendas WHERE Data = ?", data)
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Dado excluído com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
