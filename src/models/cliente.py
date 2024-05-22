from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.mascota import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(length=60), nullable=False)
    apellido = Column(String(length=60), nullable=False)
    telefono = Column(String(length=15), nullable=False)
    mascota_id = Column(Integer, ForeignKey('mascotas.id'), nullable=False)

    mascota = relationship("Mascota", back_populates="clientes")
