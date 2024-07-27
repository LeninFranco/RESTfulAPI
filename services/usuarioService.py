from sqlalchemy.orm import Session
from entities import models, schemas
import bcrypt


def getUser(db: Session, user_id: str):
    return db.query(models.Usuario).filter(models.Usuario.id == user_id).first()

def getUserByUsername(db: Session, username: str):
    usuario = db.query(models.Usuario).filter(models.Usuario.username == username).first()
    return usuario

def getAllUsers(db: Session):
    return db.query(models.Usuario).all()

def createUser(db: Session, user: schemas.UsuarioCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    nuevoUsuario = models.Usuario(username=user.username, password=hashed_password)
    db.add(nuevoUsuario)
    db.commit()
    db.refresh(nuevoUsuario)
    return nuevoUsuario

def updateUser(db: Session, user_id: str, user: schemas.UsuarioCreate):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    if usuario:
        usuario.username = user.username
        usuario.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        db.commit()
        db.refresh(usuario)
        return usuario
    return None

def getUserVideogames(db: Session, user_id: str):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    return usuario.videojuegos if usuario else None

def getUserPurchases(db: Session, user_id: str):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    return usuario.historial_compras if usuario else None