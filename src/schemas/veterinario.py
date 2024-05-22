from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VeterinarioModel(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the product")
    nombre: Optional[str] = Field(None, title="Name", max_length=60)
    correo: EmailStr = Field(min_length=6, max_length=64, title="Email of the user")
    especialidad:  Optional[str] = Field(None, title="Name", max_length=60)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Nombre Veterinario",
                "correo": " Nombre@example.com",
                "especialidad": "Especialidad"
            }
        }