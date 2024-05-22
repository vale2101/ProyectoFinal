from typing import List
from sqlalchemy.orm import Session
from src.schemas.cita import Cita as CitaSchema, CitaCreate
from src.models.citas import Cita as CitaModel

class CitaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_citas(self) -> List[CitaSchema]:
        return self.db.query(CitaModel).all()

    def get_cita(self, id: int) -> CitaSchema:
        return self.db.query(CitaModel).filter(CitaModel.id == id).first()

    def create_cita(self, cita: CitaCreate) -> CitaSchema:
        new_cita = CitaModel(**cita.dict())
        self.db.add(new_cita)
        self.db.commit()
        self.db.refresh(new_cita)
        return new_cita

    def delete_cita(self, id: int) -> CitaSchema:
        element = self.db.query(CitaModel).filter(CitaModel.id == id).first()
        if element:
            self.db.delete(element)
            self.db.commit()
        return element

    def update_cita(self, id: int, cita: CitaCreate) -> CitaSchema:
        element = self.db.query(CitaModel).filter(CitaModel.id == id).first()
        if element:
            element.fecha_hora = cita.fecha_hora
            element.descripcion = cita.descripcion
            element.veterinario_id = cita.veterinario_id
            self.db.commit()
            self.db.refresh(element)
        return element
