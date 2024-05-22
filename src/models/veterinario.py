from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Veterinario(Base):
    __tablename__ = "veterinario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(length=60), nullable=False)
    correo = Column(String(length=64), unique=True, index=True)
    especialidad = Column(String(length=64), unique=True, index=True)

    citas = relationship("Cita", back_populates="veterinario")