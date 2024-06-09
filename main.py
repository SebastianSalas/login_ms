from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.router import router
from database import Base, engine
import logging  # Agrega esta línea para importar el módulo logging

app = FastAPI(title="Auth API")

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen
    allow_credentials=True,  # Permite credenciales en las solicitudes (como cookies, por ejemplo)
    allow_methods=["*"],  # Permite cualquier método HTTP (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Permite cualquier cabecera en las solicitudes
)

app.include_router(router)

# Configuración de registro
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
