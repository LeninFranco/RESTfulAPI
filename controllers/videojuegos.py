from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from utils.database import getDB
from entities import schemas
from services import videojuegoService

router = APIRouter(prefix="/videogames", tags=['Videojuegos'])


@router.get("/", response_model=list[schemas.Videojuego], status_code=status.HTTP_200_OK)
async def getAllVideogames(db: Session = Depends(getDB)):
    return videojuegoService.getAllVideogames(db)


@router.get("/{id}", response_model=schemas.Videojuego, status_code=status.HTTP_200_OK)
async def getVideogame(id: str, db: Session = Depends(getDB)):
    videojuego = videojuegoService.getVideogame(db, id)
    if videojuego is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Videojuego no encontrado")
    return videojuego


@router.get("/{id}/users", response_model=list[schemas.Usuario], status_code=status.HTTP_200_OK)
async def getVideogamesUsers(id: str, db: Session = Depends(getDB)):
    videojuego = videojuegoService.getVideogame(db, id)
    if videojuego is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Videojuego no encontrado")
    return videojuegoService.getVideogameUsers(db, id)


@router.get("/{id}/sells", response_model=list[schemas.VentaVideogame], status_code=status.HTTP_200_OK)
async def getVideogamesSells(id: str, db: Session = Depends(getDB)):
    videojuego = videojuegoService.getVideogame(db, id)
    if videojuego is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Videojuego no encontrado")
    return videojuegoService.getVideogameSales(db, id)


@router.post("/", response_model=schemas.Videojuego, status_code=status.HTTP_201_CREATED)
async def createVideogame(videojuego: schemas.VideojuegoCreate, db: Session = Depends(getDB)):
    return videojuegoService.createVideogame(db, videojuego)


@router.put("/{id}", response_model=schemas.Videojuego, status_code=status.HTTP_202_ACCEPTED)
async def updateVideogame(id: str, videogame: schemas.VideojuegoCreate, db: Session = Depends(getDB)):
    videojuego = videojuegoService.getVideogame(db, id)
    if videojuego is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Videojuego no encontrado")
    return videojuegoService.updateVideogame(db, id, videogame)