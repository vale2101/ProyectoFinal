from pydantic import BaseModel, Field
from typing import Optional

class MascotaModel(BaseModel):
    id: Optional[int] = Field(default=None, title="ID de la mascota")
    nombre: Optional[str] = Field(None, title="Nombre de la mascota", max_length=60)
    raza: Optional[str] = Field(None, title="Raza de la mascota", max_length=60)
    edad: Optional[int] = Field(None, title="Edad de la mascota")

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Fido",
                "raza": "Labrador",
                "edad": 3
            }
        }
