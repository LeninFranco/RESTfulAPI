from sqlalchemy import Table, Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from utils.database import Base


usuario_videojuego = Table('bibliotecas', Base.metadata,
                           Column('usuario_id', String(36), ForeignKey('usuarios.id')),
                           Column('videojuego_id', String(36), ForeignKey('videojuegos.id'))
                           )


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(32), nullable=False, unique=True)
    password = Column(String(60), nullable=False)

    videojuegos = relationship('Videojuego', secondary=usuario_videojuego, back_populates='usuarios')
    historial_compras = relationship('Venta', back_populates='usuario')


class Videojuego(Base):
    __tablename__ = "videojuegos"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(100), nullable=False)
    desarrolladora = Column(String(50), nullable=False)
    genero = Column(String(25), nullable=False)
    calificacion = Column(Integer, nullable=False)
    precio = Column(DECIMAL(10,2), nullable=False)

    usuarios = relationship('Usuario', secondary=usuario_videojuego, back_populates='videojuegos')
    historial_ventas = relationship('Venta', back_populates='videojuego')


class Venta(Base):
    __tablename__ = "ventas"
    usuario_id = Column(String(36), ForeignKey('usuarios.id'), primary_key=True)
    videojuego_id = Column(String(36), ForeignKey('videojuegos.id'), primary_key=True)
    total = Column(DECIMAL(10,2), nullable=False)
    fecha_compra = Column(DateTime, default=datetime.utcnow())

    usuario = relationship('Usuario', back_populates='historial_compras')
    videojuego = relationship('Videojuego', back_populates='historial_ventas')