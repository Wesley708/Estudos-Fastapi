from fastapi import FastAPI
from pydantic import BaseModel
from database import Usuario, Materias
import json
from cors import configure_cors  # Importar a função de configuração CORS

app = FastAPI()

# Configurar CORS
configure_cors(app)

class UsuarioIn(BaseModel):
    nome: str
    email: str
    senha: str

@app.get('/')

@app.get('/')
# def index():
#     return {'nome':'Mariana Cordeiro Dias'}
async def index():
    usuarios_data = list(Usuario.select())
    lista_usuarios = []
    for usuarios in usuarios_data:
        lista_usuarios.append({'id': usuarios.id, 'nome': usuarios.nome, 'email' : usuarios.email})
    return lista_usuarios

@app.post('/users')

async def create_user(usuario: UsuarioIn):
    novo_usuario = Usuario.create(**usuario.dict())
    return {"id": novo_usuario.id, "nome": novo_usuario.nome, "email": novo_usuario.email}

