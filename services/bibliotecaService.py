from sqlalchemy.orm import Session
from entities import models, schemas


def addVideogameToLibrary(db: Session, venta: schemas.VentaCreate):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == venta.usuario_id).first()
    videojuego = db.query(models.Videojuego).filter(models.Videojuego.id == venta.videojuego_id).first()
    if usuario and videojuego:
        usuario.videojuegos.append(videojuego)
        db.commit()
        return True
    return False