from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CitaBase(BaseModel):
    fecha_hora: datetime = Field(..., title="Fecha y hora de la cita")
    descripcion: str = Field(..., title="Descripción de la cita", max_length=255)
    veterinario_id: int = Field(..., title="ID del veterinario")

class CitaCreate(CitaBase):
    pass

class Cita(CitaBase):
    id: Optional[int] = Field(default=None, title="ID de la cita")
    nombre_veterinario: Optional[str] = Field(None, title="Nombre del veterinario")

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "fecha_hora": "2024-05-20T14:30:00",
                "descripcion": "Consulta de rutina",
                "veterinario_id": 1,
                "nombre_veterinario": "Dr. Juan Pérez"
            }
        }
