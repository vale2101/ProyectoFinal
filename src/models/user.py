from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=60))
    email = Column(String(length=64), unique=True, index=True)
    password = Column(String(length=64))
    is_active = Column(Boolean, default=True)
    id_rol = Column(Integer, ForeignKey('roles.id'))

    role = relationship("RoleModel", back_populates="users")