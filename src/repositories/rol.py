from typing import List, Optional
from sqlalchemy.orm import Session
from src.schemas.rol import Role as RoleSchema
from src.models.rol import RoleModel as RoleModelDB

class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_roles(self) -> List[RoleSchema]:
        query = self.db.query(RoleModelDB)
        return query.all()

    def get_role(self, id: int) -> Optional[RoleSchema]:
        element = self.db.query(RoleModelDB).filter(RoleModelDB.id == id).first()
        return RoleSchema.from_orm(element) if element else None

    def create_role(self, role: RoleSchema) -> RoleSchema:
        new_role = RoleModelDB(**role.dict())
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)
        return RoleSchema.from_orm(new_role)

    def delete_role(self, id: int) -> Optional[RoleSchema]:
        element = self.db.query(RoleModelDB).filter(RoleModelDB.id == id).first()
        if element:
            self.db.delete(element)
            self.db.commit()
        return RoleSchema.from_orm(element) if element else None

    def update_role(self, id: int, role: RoleSchema) -> Optional[RoleSchema]:
        element = self.db.query(RoleModelDB).filter(RoleModelDB.id == id).first()
        
        if element:
            element.name = role.name
            self.db.commit()
            self.db.refresh(element)
        return RoleSchema.from_orm(element) if element else None
