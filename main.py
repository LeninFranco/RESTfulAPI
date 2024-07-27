from fastapi import FastAPI
from controllers import usuarios, videojuegos, ventas

app = FastAPI()
app.title = "VideoGameStore API"
app.version = "1.0"

app.include_router(usuarios.router)
app.include_router(videojuegos.router)
app.include_router(ventas.router)