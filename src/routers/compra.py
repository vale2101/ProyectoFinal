from fastapi import APIRouter, Body, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Generator
from src.schemas.compra import CompraCreate, Compra as CompraSchema
from src.repositories.compra import CompraRepository
from src.config.database import SessionLocal
from src.auth.has_access import has_access

compras_router = APIRouter()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@compras_router.post('/compras',
                     tags=['compras'],
                     response_model=CompraSchema,
                     description="Crear una compra")
def create_compra(compra: CompraCreate = Body(...), db: Session = Depends(get_db), Compra: dict = Depends(has_access([2]))):
    try:
        return CompraRepository(db).create_compra(compra)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
