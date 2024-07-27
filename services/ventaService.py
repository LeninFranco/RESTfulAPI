from sqlalchemy.orm import Session
from entities import models, schemas


def makePurchase(db: Session, venta: schemas.VentaCreate):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == venta.usuario_id).first()
    videojuego = db.query(models.Videojuego).filter(models.Videojuego.id == venta.videojuego_id).first()
    if usuario and videojuego:
        newVenta = models.Venta(usuario=usuario, videojuego=videojuego, total=videojuego.precio)
        db.add(newVenta)
        db.commit()
        db.refresh(newVenta)
        return newVenta
    return None