from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from utils.database import getDB
from entities import schemas
from services import usuarioService

router = APIRouter(prefix="/users", tags=['Usuarios'])


@router.get("/", response_model=list[schemas.Usuario], status_code=status.HTTP_200_OK)
async def getAllUsers(db: Session = Depends(getDB)):
    return usuarioService.getAllUsers(db)


@router.get("/{id}", response_model=schemas.Usuario, status_code=status.HTTP_200_OK)
async def getUser(id: str, db: Session = Depends(getDB)):
    usuario = usuarioService.getUser(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.get("/username/{username}", response_model=schemas.Usuario, status_code=status.HTTP_200_OK)
async def getUserByUsername(username: str, db: Session = Depends(getDB)):
    usuario = usuarioService.getUserByUsername(db, username)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.get("/{id}/videogames", response_model=list[schemas.Videojuego], status_code=status.HTTP_200_OK)
async def getUsersVideogames(id: str, db: Session = Depends(getDB)):
    usuario = usuarioService.getUser(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuarioService.getUserVideogames(db, id)


@router.get("/{id}/purchases", response_model=list[schemas.VentaUser], status_code=status.HTTP_200_OK)
async def getUsersPurchases(id: str, db: Session = Depends(getDB)):
    usuario = usuarioService.getUser(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuarioService.getUserPurchases(db, id)


@router.post("/", response_model=schemas.Usuario, status_code=status.HTTP_201_CREATED)
async def createUser(user: schemas.UsuarioCreate, db: Session = Depends(getDB)):
    usuario = usuarioService.getUserByUsername(db, user.username)
    if usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe un usuario con ese nombre")
    return usuarioService.createUser(db, user)


@router.put("/{id}", response_model=schemas.Usuario, status_code=status.HTTP_202_ACCEPTED)
async def updateUser(id: str, user: schemas.UsuarioCreate, db: Session = Depends(getDB)):
    usuario = usuarioService.getUser(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuarioService.updateUser(db, id, user)
