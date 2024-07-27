from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class UsuarioBase(BaseModel):
    username: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: str

    class Config:
        from_attributes = True


class VideojuegoBase(BaseModel):
    nombre: str
    descripcion: str
    desarrolladora: str
    genero: str
    calificacion: int
    precio: Decimal

class VideojuegoCreate(VideojuegoBase):
    pass

class Videojuego(VideojuegoBase):
    id: str

    class Config:
        from_attributes = True


class VentaBase(BaseModel):
    usuario_id: str
    videojuego_id: str

class VentaCreate(VentaBase):
    pass

class Venta(BaseModel):
    usuario: Usuario
    videojuego: Videojuego
    total: Decimal
    fecha_compra: datetime

class VentaUser(BaseModel):
    videojuego: Videojuego
    total: Decimal
    fecha_compra: datetime

class VentaVideogame(BaseModel):
    usuario: Usuario
    total: Decimal
    fecha_compra: datetime