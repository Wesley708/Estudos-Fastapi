import mysql.connector
from fastapi import FastAPI

# Crie uma instância do aplicativo FastAPI
app = FastAPI()

# Configuração da conexão com o banco de dados MySQL
config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'daprafaltar',
  'raise_on_warnings': True
}

# Função para conectar ao banco de dados
def conectar_bd():
    return mysql.connector.connect(**config)

# Rota para testar a conexão com o banco de dados
@app.get("/testar_conexao")
async def testar_conexao():
    try:
        # Tenta conectar ao banco de dados
        conexao = conectar_bd()
        conexao.close()
        return {"mensagem": "Conexão bem-sucedida ao banco de dados MySQL."}
    except Exception as e:
        return {"mensagem": "Erro ao conectar ao banco de dados MySQL.", "erro": str(e)}
