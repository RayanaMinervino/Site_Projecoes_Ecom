import pyodbc
from datetime import datetime

# Conexão com o banco de dados
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=servidorprojecaoecom.database.windows.net;'
    'DATABASE=projecao_db;'
    'UID=rayaanminervinoecom;'
    'PWD=Novasenha123@;'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
    'Connection Timeout=30;'
)

cursor = conn.cursor()

# Entrar dados
data_str = input("Digite a data (dd/mm/aaaa): ")
valor = float(input("Digite o valor: "))

# Converter para string no formato aceito pelo SQL
data_formatada = datetime.strptime(data_str, "%d/%m/%Y").strftime("%Y-%m-%d")

# Inserir no banco de dados
cursor.execute("INSERT INTO ProjecaoVendas (Data, Valor) VALUES (?, ?)", data_formatada, valor)
conn.commit()

print("✅ Dados inseridos com sucesso!")

cursor.close()
conn.close()
