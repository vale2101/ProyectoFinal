from fastapi import APIRouter, Body, Path, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List, Generator
from src.schemas.user import User as UserSchema, UserCreate as UserCreateSchema
from src.repositories.user import UserRepository
from src.config.database import SessionLocal
from src.auth.jwt_handler import JWTHandler
from src.auth.has_access import has_access

users_router = APIRouter()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@users_router.get('/users', 
                  tags=['users'], 
                  response_model=List[UserSchema],
                  description="Obtener todos los usuarios")
def get_all_users(db: Session = Depends(get_db), user: dict = Depends(has_access([1]))):
    return UserRepository(db).get_all_users()

@users_router.put('/user/{id}',
                  tags=['users'],
                  response_model=UserSchema,
                  description="Actualizar un usuario")
def update_user(id: int, user: UserCreateSchema = Body(...), db: Session = Depends(get_db), current_user: dict = Depends(has_access([1]))):
    updated_user = UserRepository(db).update_user(id, user)
    if not updated_user:
        return JSONResponse(content={
            "message": "El usuario solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return updated_user

@users_router.delete('/user/{id}',
                     tags=['users'],
                     response_model=UserSchema,
                     description="Eliminar un usuario")
def delete_user(id: int, db: Session = Depends(get_db), user: dict = Depends(has_access([1]))):
    deleted_user = UserRepository(db).delete_user(id)
    if not deleted_user:
        return JSONResponse(content={
            "message": "El usuario solicitado no fue encontrado",
            "data": None
        }, status_code=status.HTTP_404_NOT_FOUND)
    return deleted_user
