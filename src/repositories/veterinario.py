from typing import List
from sqlalchemy.orm import Session
from src.schemas.veterinario import VeterinarioModel
from src.models.veterinario import Veterinario as VeterinarioModelDB

class VeterinarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_veterinarios(self, offset: int = 0, limit: int = 10) -> List[VeterinarioModel]:
        query = self.db.query(VeterinarioModelDB).offset(offset).limit(limit)
        return query.all()

    def get_veterinario(self, id: int) -> VeterinarioModel:
        return self.db.query(VeterinarioModelDB).filter(VeterinarioModelDB.id == id).first()

    def create_veterinario(self, veterinario: VeterinarioModel) -> VeterinarioModel:
        new_veterinario = VeterinarioModelDB(**veterinario.dict())
        self.db.add(new_veterinario)
        self.db.commit()
        self.db.refresh(new_veterinario)
        return new_veterinario

    def delete_veterinario(self, id: int) -> VeterinarioModel:
        element = self.db.query(VeterinarioModelDB).filter(VeterinarioModelDB.id == id).first()
        if element:
            self.db.delete(element)
            self.db.commit()
        return element

    def update_veterinario(self, id: int, veterinario: VeterinarioModel) -> VeterinarioModel:
        element = self.db.query(VeterinarioModelDB).filter(VeterinarioModelDB.id == id).first()
        if element:
            element.nombre = veterinario.nombre
            element.correo = veterinario.correo
            element.especialidad = veterinario.especialidad
            self.db.commit()
            self.db.refresh(element)
        return element
