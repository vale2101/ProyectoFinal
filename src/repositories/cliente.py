from typing import List
from sqlalchemy.orm import Session
from src.schemas.cliente import ClienteModel
from src.models.cliente import Cliente as ClienteModelDB

class ClienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_clientes(self) -> List[ClienteModel]:
        clientes = self.db.query(ClienteModelDB).all()
        return clientes

    def get_cliente(self, id: int) -> ClienteModel:
        cliente = self.db.query(ClienteModelDB).filter(ClienteModelDB.id == id).first()
        return cliente

    def create_cliente(self, cliente: ClienteModel) -> ClienteModel:
        new_cliente = ClienteModelDB(**cliente.dict())
        self.db.add(new_cliente)
        self.db.commit()
        self.db.refresh(new_cliente)
        return new_cliente

    def delete_cliente(self, id: int) -> ClienteModel:
        element = self.db.query(ClienteModelDB).filter(ClienteModelDB.id == id).first()
        if element:
            self.db.delete(element)
            self.db.commit()
        return element

    def update_cliente(self, id: int, cliente: ClienteModel) -> ClienteModel:
        element = self.db.query(ClienteModelDB).filter(ClienteModelDB.id == id).first()
        if element:
            element.nombre = cliente.nombre
            element.apellido = cliente.apellido
            element.telefono = cliente.telefono
            element.mascota_id = cliente.mascota_id
            self.db.commit()
            self.db.refresh(element)
            element.nombre_mascota = element.nombre_mascota
        return element
