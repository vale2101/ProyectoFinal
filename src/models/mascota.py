from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Mascota(Base):
    __tablename__ = "mascotas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(length=60), nullable=False)
    raza = Column(String(length=60), nullable=False)
    edad = Column(Integer, nullable=False)
    
    clientes = relationship("Cliente", back_populates="mascota")