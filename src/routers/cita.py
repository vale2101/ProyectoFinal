from fastapi import APIRouter, Body, Path, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Generator, List
from src.schemas.cita import Cita, CitaCreate
from src.repositories.cita import CitaRepository
from src.config.database import SessionLocal
from src.auth.has_access import has_access

citas_router = APIRouter()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@citas_router.get('/cita',
                  tags=['citas'],
                  response_model=List[Cita],
                  description="Listar las citas")
def get_all_citas(db: Session = Depends(get_db), Cita: dict = Depends(has_access([3]))):
    return CitaRepository(db).get_citas()

@citas_router.get('/cita/{id}',
                  tags=['citas'],
                  response_model=Cita,
                  description="Información de una cita específica")
def get_cita(id: int = Path(..., title="Ingrese el ID", ge=1),
             db: Session = Depends(get_db), current_cita: dict = Depends(has_access([3]))):
    cita = CitaRepository(db).get_cita(id)
    if not cita:
        return JSONResponse(content={
            "message": "La cita solicitada no fue encontrada",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return cita

@citas_router.post('/cita',
                   tags=['citas'],
                   response_model=Cita,
                   description="Crear una cita")
def create_cita(cita: CitaCreate = Body(...), db: Session = Depends(get_db), Cita: dict = Depends(has_access([2]))):
    return CitaRepository(db).create_cita(cita)

@citas_router.put('/cita/{id}',
                  tags=['citas'],
                  response_model=Cita,
                  description="Actualiza los datos de una cita específica.")
def update_cita(id: int = Path(..., title="El ID de la cita a actualizar", ge=1),
                cita: CitaCreate = Body(...), db: Session = Depends(get_db), Cita: dict = Depends(has_access([3]))):
    updated_cita = CitaRepository(db).update_cita(id, cita)
    if not updated_cita:
        return JSONResponse(content={
            "message": "La cita solicitada no fue encontrada",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return updated_cita

@citas_router.delete('/cita/{id}',
                     tags=['citas'],
                     response_model=Cita,
                     description="Elimina una cita específica")
def remove_cita(id: int = Path(..., title="El ID de la cita a eliminar", ge=1),
                db: Session = Depends(get_db), Cita: dict = Depends(has_access([3]))):
    removed_cita = CitaRepository(db).delete_cita(id)
    if not removed_cita:
        return JSONResponse(content={
            "message": "La cita solicitada no fue encontrada",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return removed_cita
