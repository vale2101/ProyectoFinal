from fastapi import APIRouter, Body, Path, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Generator, List
from src.schemas.mascota import MascotaModel
from src.repositories.mascota import MascotaRepository
from src.config.database import SessionLocal
from src.auth.has_access import has_access

mascotas_router = APIRouter()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@mascotas_router.get('/mascotas',
                     tags=['mascotas'],
                     response_model=List[MascotaModel],
                     description="Listar las mascotas")
def get_all_mascotas(db: Session = Depends(get_db), Mascota: dict = Depends(has_access([3]))):
    return MascotaRepository(db).get_mascotas()

@mascotas_router.get('/mascotas/{id}',
                     tags=['mascotas'],
                     response_model=MascotaModel,
                     description="Información de una mascota específica")
def get_mascota(id: int = Path(..., title="Ingrese el ID", ge=1),
                db: Session = Depends(get_db), Mascota: dict = Depends(has_access([3]))):
    mascota = MascotaRepository(db).get_mascota(id)
    if not mascota:
        return JSONResponse(content={
            "message": "La mascota solicitada no fue encontrada",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return mascota

@mascotas_router.post('/mascotas',
                      tags=['mascotas'],
                      response_model=MascotaModel,
                      description="Crear una mascota")
def create_mascota(mascota: MascotaModel = Body(...), db: Session = Depends(get_db), Mascota: dict = Depends(has_access([3]))):
    return MascotaRepository(db).create_mascota(mascota)

@mascotas_router.put('/mascotas/{id}',
                     tags=['mascotas'],
                     response_model=MascotaModel,
                     description="Actualiza los datos de una mascota específica.")
def update_mascota(id: int = Path(..., title="El ID de la mascota a actualizar", ge=1),
                   mascota: MascotaModel = Body(...), db: Session = Depends(get_db), Mascota: dict = Depends(has_access([3]))):
    updated_mascota = MascotaRepository(db).update_mascota(id, mascota)
    if not updated_mascota:
        return JSONResponse(content={
            "message": "La mascota solicitada no fue encontrada",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return updated_mascota

@mascotas_router.delete('/mascotas/{id}',
                        tags=['mascotas'],
                        response_model=MascotaModel,
                        description="Elimina una mascota específica")
def remove_mascota(id: int = Path(..., title="El ID de la mascota a eliminar", ge=1),
                   db: Session = Depends(get_db), Mascota: dict = Depends(has_access([3]))):
    removed_mascota = MascotaRepository(db).delete_mascota(id)
    if not removed_mascota:
        return JSONResponse(content={
            "message": "La mascota solicitada no fue encontrada",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return removed_mascota
