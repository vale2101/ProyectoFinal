from fastapi import APIRouter, Body, Path, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Generator, List
from src.schemas.producto import ProductoModel
from src.repositories.producto import ProductoRepository
from src.config.database import SessionLocal
from src.auth.has_access import has_access

productos_router = APIRouter()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@productos_router.get('/producto',
                     tags=['productos'],
                     response_model=List[ProductoModel],
                     description="Listar los productos")
def get_all_productos(db: Session = Depends(get_db), Producto: dict = Depends(has_access([3]))):
    return ProductoRepository(db).get_productos()

@productos_router.get('/producto/{id}',
                     tags=['productos'],
                     response_model=ProductoModel,
                     description="Informacion de un producto en especifico")
def get_producto(id: int = Path(..., title="Ingrese el ID", ge=1),
                db: Session = Depends(get_db), Producto: dict = Depends(has_access([3]))):
    producto = ProductoRepository(db).get_producto(id)
    if not producto:
        return JSONResponse(content={
            "message": "El producto solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return producto

@productos_router.post('/producto',
                      tags=['productos'],
                      response_model=ProductoModel,
                      description="Crear un producto")
def create_producto(producto: ProductoModel = Body(...), db: Session = Depends(get_db), Producto: dict = Depends(has_access([3]))):
    return ProductoRepository(db).create_producto(producto)

@productos_router.put('/producto/{id}',
                     tags=['productos'],
                     response_model=ProductoModel,
                     description="Actualiza los datos de un producto específico.")
def update_producto(id: int = Path(..., title="El ID del producto a actualizar", ge=1),
                   producto: ProductoModel = Body(...), db: Session = Depends(get_db), Producto: dict = Depends(has_access([3]))):
    updated_producto = ProductoRepository(db).update_producto(id, producto)
    if not updated_producto:
        return JSONResponse(content={
            "message": "El producto solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return updated_producto

@productos_router.delete('/producto/{id}',
                        tags=['productos'],
                        response_model=ProductoModel,
                        description="Elimina producto específico")
def remove_producto(id: int = Path(..., title="El ID del producto a eliminar", ge=1),
                   db: Session = Depends(get_db), Producto: dict = Depends(has_access([3]))):
    removed_producto = ProductoRepository(db).delete_producto(id)
    if not removed_producto:
        return JSONResponse(content={
            "message": "El producto solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return removed_producto
