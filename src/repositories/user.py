from typing import List, Optional
from sqlalchemy.orm import Session
from src.schemas.user import User as UserSchema, UserCreate as UserCreateSchema
from src.models.user import UserModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, id: int) -> Optional[UserSchema]:
        element = self.db.query(UserModel).filter(UserModel.id == id).first()
        return UserSchema.from_orm(element) if element else None

    def get_user_by_email(self, email: str) -> Optional[UserSchema]:
        element = self.db.query(UserModel).filter(UserModel.email == email).first()
        return UserSchema.from_orm(element) if element else None

    def create_user(self, user: UserCreateSchema) -> UserSchema:
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return UserSchema.from_orm(new_user)

    def update_user(self, id: int, user: UserCreateSchema) -> Optional[UserSchema]:
        element = self.db.query(UserModel).filter(UserModel.id == id).first()
        if element:
            element.name = user.name
            element.email = user.email
            element.password = user.password
            element.is_active = user.is_active if user.is_active is not None else element.is_active
            element.id_rol = user.id_rol if user.id_rol is not None else element.id_rol
            self.db.commit()
            self.db.refresh(element)
            return UserSchema.from_orm(element)
        return None

    def delete_user(self, id: int) -> Optional[UserSchema]:
        element = self.db.query(UserModel).filter(UserModel.id == id).first()
        if element:
            self.db.delete(element)
            self.db.commit()
            return UserSchema.from_orm(element)
        return None

    def get_all_users(self) -> List[UserSchema]:
        elements = self.db.query(UserModel).all()
        return [UserSchema.from_orm(element) for element in elements]
