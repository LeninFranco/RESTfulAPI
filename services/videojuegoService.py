from sqlalchemy.orm import Session
from entities import models, schemas


def getVideogame(db: Session, videogame_id: str):
    return db.query(models.Videojuego).filter(models.Videojuego.id == videogame_id).first()

def getAllVideogames(db: Session):
    return db.query(models.Videojuego).all()

def createVideogame(db: Session, videogame: schemas.VideojuegoCreate):
    nuevoVideojuego = models.Videojuego(
        nombre=videogame.nombre,
        descripcion=videogame.descripcion,
        desarrolladora=videogame.desarrolladora,
        genero=videogame.genero,
        calificacion=videogame.calificacion,
        precio=videogame.precio
    )
    db.add(nuevoVideojuego)
    db.commit()
    db.refresh(nuevoVideojuego)
    return nuevoVideojuego

def updateVideogame(db: Session, videogame_id: str, videogame: schemas.VideojuegoCreate):
    videojuego = db.query(models.Videojuego).filter(models.Videojuego.id == videogame_id).first()
    if videojuego:
        videojuego.nombre = videogame.nombre,
        videojuego.descripcion = videogame.descripcion,
        videojuego.desarrolladora = videogame.desarrolladora,
        videojuego.genero = videogame.genero,
        videojuego.calificacion = videogame.calificacion,
        videojuego.precio = videogame.precio
        db.commit()
        db.refresh(videojuego)
        return videojuego
    return None

def getVideogameUsers(db: Session, videogame_id: str):
    videojuego = db.query(models.Videojuego).filter(models.Videojuego.id == videogame_id).first()
    return videojuego.usuarios if videojuego else None

def getVideogameSales(db: Session, videogame_id: str):
    videojuego = db.query(models.Videojuego).filter(models.Videojuego.id == videogame_id).first()
    return videojuego.historial_ventas if videojuego else None