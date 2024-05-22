from typing import List
from sqlalchemy.orm import Session
from src.schemas.mascota import MascotaModel
from src.models.mascota import Mascota as MascotaModelDB

class MascotaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_mascotas(self) -> List[MascotaModel]:
        return self.db.query(MascotaModelDB).all()

    def get_mascota(self, id: int) -> MascotaModel:
        return self.db.query(MascotaModelDB).filter(MascotaModelDB.id == id).first()

    def create_mascota(self, mascota: MascotaModel) -> MascotaModel:
        new_mascota = MascotaModelDB(**mascota.dict())
        self.db.add(new_mascota)
        self.db.commit()
        self.db.refresh(new_mascota)
        return new_mascota

    def delete_mascota(self, id: int) -> MascotaModel:
        element = self.db.query(MascotaModelDB).filter(MascotaModelDB.id == id).first()
        if element:
            self.db.delete(element)
            self.db.commit()
        return element

    def update_mascota(self, id: int, mascota: MascotaModel) -> MascotaModel:
        element = self.db.query(MascotaModelDB).filter(MascotaModelDB.id == id).first()
        if element:
            element.nombre = mascota.nombre
            element.raza = mascota.raza
            element.edad = mascota.edad
            self.db.commit()
            self.db.refresh(element)
        return element
