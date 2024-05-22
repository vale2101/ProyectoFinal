from fastapi import APIRouter, Body, Path, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Generator, List
from src.schemas.veterinario import VeterinarioModel
from src.repositories.veterinario import VeterinarioRepository
from src.config.database import SessionLocal
from src.auth.has_access import has_access

veterinarios_router = APIRouter()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@veterinarios_router.get('/veterinario',
                         tags=['veterinarios'],
                         response_model=List[VeterinarioModel],
                         description="Listar los veterinarios")
def get_all_veterinarios(db: Session = Depends(get_db), Veterinario: dict = Depends(has_access([1]))):
    return VeterinarioRepository(db).get_veterinarios()

@veterinarios_router.get('/veterinario/{id}',
                         tags=['veterinarios'],
                         response_model=VeterinarioModel,
                         description="Información de un veterinario en específico")
def get_veterinario(id: int = Path(..., title="Ingrese el ID", ge=1),
                    db: Session = Depends(get_db), Veterinario: dict = Depends(has_access([1]))):
    veterinario = VeterinarioRepository(db).get_veterinario(id)
    if not veterinario:
        return JSONResponse(content={
            "message": "El veterinario solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return veterinario

@veterinarios_router.post('/veterinario',
                          tags=['veterinarios'],
                          response_model=VeterinarioModel,
                          description="Crear un veterinario")
def create_veterinario(veterinario: VeterinarioModel = Body(...), db: Session = Depends(get_db), Veterinario: dict = Depends(has_access([1]))):
    return VeterinarioRepository(db).create_veterinario(veterinario)

@veterinarios_router.put('/veterinario/{id}',
                         tags=['veterinarios'],
                         response_model=VeterinarioModel,
                         description="Actualiza los datos de un veterinario específico.")
def update_veterinario(id: int = Path(..., title="El ID del veterinario a actualizar", ge=1),
                       veterinario: VeterinarioModel = Body(...), db: Session = Depends(get_db), Veterinario: dict = Depends(has_access([1]))):
    updated_veterinario = VeterinarioRepository(db).update_veterinario(id, veterinario)
    if not updated_veterinario:
        return JSONResponse(content={
            "message": "El veterinario solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return updated_veterinario

@veterinarios_router.delete('/veterinario/{id}',
                            tags=['veterinarios'],
                            response_model=VeterinarioModel,
                            description="Elimina un veterinario específico")
def remove_veterinario(id: int = Path(..., title="El ID del veterinario a eliminar", ge=1),
                       db: Session = Depends(get_db), Veterinario: dict = Depends(has_access([1]))):
    removed_veterinario = VeterinarioRepository(db).delete_veterinario(id)
    if not removed_veterinario:
        return JSONResponse(content={
            "message": "El veterinario solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return removed_veterinario
