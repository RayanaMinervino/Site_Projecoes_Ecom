import pyodbc
from datetime import datetime

# Conexão com o banco de dados
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=servidorprojecaoecom.database.windows.net;'
    'DATABASE=projecao_db;'
    'UID=rayaanminervinoecom;'
    'PWD=Novasenha123@;'
)
cursor = conn.cursor()

# Exibe os dados existentes
print("\n📋 Dados existentes na tabela:")
cursor.execute("SELECT * FROM ProjecaoVendas ORDER BY Data")
for row in cursor.fetchall():
    print(row)

# Insere novo dado
print("\n🆕 Inserir nova projeção")
data_str = input("Digite a data (dd/mm/aaaa): ")
valor = float(input("Digite o valor: "))
data = datetime.strptime(data_str, "%d/%m/%Y").date()
cursor.execute("INSERT INTO ProjecaoVendas (Data, Valor) VALUES (?, ?)", data, valor)
conn.commit()
print("✅ Projeção inserida com sucesso!")

cursor.close()
conn.close()
