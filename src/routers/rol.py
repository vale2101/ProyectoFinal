from fastapi import APIRouter, Body, Path, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Generator, List
from src.schemas.rol import Role as RoleSchema
from src.repositories.rol import RoleRepository
from src.config.database import SessionLocal
from src.auth.has_access import has_access

roles_router = APIRouter()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@roles_router.get('/roles',
                  tags=['roles'],
                  response_model=List[RoleSchema],
                  description="Listar los roles")
def get_all_roles(db: Session = Depends(get_db), Role: dict = Depends(has_access([1]))):
    return RoleRepository(db).get_roles()

@roles_router.get('/roles/{id}',
                  tags=['roles'],
                  response_model=RoleSchema,
                  description="Información de un rol específico")
def get_role(id: int = Path(..., title="Ingrese el ID del rol", ge=1),
             db: Session = Depends(get_db), Role: dict = Depends(has_access([1]))):
    role = RoleRepository(db).get_role(id)
    if not role:
        return JSONResponse(content={
            "message": "El rol solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return role

@roles_router.post('/roles',
                   tags=['roles'],
                   response_model=RoleSchema,
                   description="Crear un nuevo rol")
def create_role(role: RoleSchema = Body(...), db: Session = Depends(get_db), Role: dict = Depends(has_access([1]))):
    return RoleRepository(db).create_role(role)

@roles_router.put('/roles/{id}',
                  tags=['roles'],
                  response_model=RoleSchema,
                  description="Actualizar los datos de un rol específico")
def update_role(id: int = Path(..., title="El ID del rol a actualizar", ge=1),
                role: RoleSchema = Body(...), db: Session = Depends(get_db), Role: dict = Depends(has_access([1]))):
    updated_role = RoleRepository(db).update_role(id, role)
    if not updated_role:
        return JSONResponse(content={
            "message": "El rol solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return updated_role

@roles_router.delete('/roles/{id}',
                     tags=['roles'],
                     response_model=RoleSchema,
                     description="Eliminar un rol específico")
def remove_role(id: int = Path(..., title="El ID del rol a eliminar", ge=1),
                db: Session = Depends(get_db), Role: dict = Depends(has_access([1]))):
    removed_role = RoleRepository(db).delete_role(id)
    if not removed_role:
        return JSONResponse(content={
            "message": "El rol solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return removed_role
