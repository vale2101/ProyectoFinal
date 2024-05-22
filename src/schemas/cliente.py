from pydantic import BaseModel, Field
from typing import Optional

class ClienteModel(BaseModel):
    id: Optional[int] = Field(default=None, title="ID del cliente")
    nombre: str = Field(..., title="Nombre del cliente", max_length=60)
    apellido: str = Field(..., title="Apellido del cliente", max_length=60)
    telefono: str = Field(..., title="Teléfono del cliente", max_length=15)
    mascota_id: int = Field(..., title="ID de la mascota")

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Juan",
                "apellido": "Pérez",
                "telefono": "1234567890",
                "mascota_id": 1
            }
        }
