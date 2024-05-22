from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.models.veterinario import Base, Veterinario

class Cita(Base):
    __tablename__ = "citas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime, nullable=False)
    descripcion = Column(String(length=255), nullable=False)
    veterinario_id = Column(Integer, ForeignKey('veterinario.id'), nullable=False)

    veterinario = relationship("Veterinario", back_populates="citas")

    @property
    def nombre_veterinario(self):
        return self.veterinario.nombre if self.veterinario else None
