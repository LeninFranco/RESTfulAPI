from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from utils.database import getDB
from entities import schemas
from services import ventaService, bibliotecaService

router = APIRouter(prefix="/purchase", tags=['Ventas'])


@router.post("/", response_model=schemas.Venta ,status_code=status.HTTP_201_CREATED)
async def createVenta(venta: schemas.VentaCreate, db: Session = Depends(getDB)):
    response = ventaService.makePurchase(db, venta)
    save = bibliotecaService.addVideogameToLibrary(db, venta)
    if response is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No existe usuario o videojuego en la base de datos")
    return response