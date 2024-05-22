from fastapi import APIRouter, Body, Path, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Generator, List
from src.schemas.cliente import ClienteModel
from src.repositories.cliente import ClienteRepository
from src.config.database import SessionLocal
from src.auth.has_access import has_access

clientes_router = APIRouter()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@clientes_router.get('/clientes',
                     tags=['clientes'],
                     response_model=List[ClienteModel],
                     description="Listar los clientes")
def get_all_clientes(db: Session = Depends(get_db), Cliente: dict = Depends(has_access([3]))):
    return ClienteRepository(db).get_clientes()

@clientes_router.get('/clientes/{id}',
                     tags=['clientes'],
                     response_model=ClienteModel,
                     description="Información de un cliente específico")
def get_cliente(id: int = Path(..., title="Ingrese el ID", ge=1),
                db: Session = Depends(get_db), Cita: dict = Depends(has_access([3]))):
    cliente = ClienteRepository(db).get_cliente(id)
    if not cliente:
        return JSONResponse(content={
            "message": "El cliente solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return cliente

@clientes_router.post('/clientes',
                      tags=['clientes'],
                      response_model=ClienteModel,
                      description="Crear un cliente")
def create_cliente(cliente: ClienteModel = Body(...), db: Session = Depends(get_db), Cliente: dict = Depends(has_access([3]))):
    return ClienteRepository(db).create_cliente(cliente)

@clientes_router.put('/clientes/{id}',
                     tags=['clientes'],
                     response_model=ClienteModel,
                     description="Actualiza los datos de un cliente específico.")
def update_cliente(id: int = Path(..., title="El ID del cliente a actualizar", ge=1),
                   cliente: ClienteModel = Body(...), db: Session = Depends(get_db), Cliente: dict = Depends(has_access([3]))):
    updated_cliente = ClienteRepository(db).update_cliente(id, cliente)
    if not updated_cliente:
        return JSONResponse(content={
            "message": "El cliente solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return updated_cliente

@clientes_router.delete('/clientes/{id}',
                        tags=['clientes'],
                        response_model=ClienteModel,
                        description="Elimina un cliente específico")
def remove_cliente(id: int = Path(..., title="El ID del cliente a eliminar", ge=1),
                   db: Session = Depends(get_db), Cliente: dict = Depends(has_access([3]))):
    removed_cliente = ClienteRepository(db).delete_cliente(id)
    if not removed_cliente:
        return JSONResponse(content={
            "message": "El cliente solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return removed_cliente
