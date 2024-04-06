from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def configure_cors(app: FastAPI):
    # Configurar CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Permitir solicitações de qualquer origem
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir métodos de solicitação específicos
        allow_headers=["*"],  # Permitir cabeçalhos específicos
    )
