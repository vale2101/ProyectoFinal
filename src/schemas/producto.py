from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductoModel(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the product")
    nombre: Optional[str] = Field(None, title="Name of the product", max_length=60)
    descripcion: Optional[str] = Field(None, title="Description of the product", max_length=400)
    precio: Optional[float] = Field(None, title="Price of the product")
    cantidad: Optional[int] = Field(None, title="Quantity of the product")

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Producto de ejemplo",
                "descripcion": "Descripción del producto de ejemplo",
                "precio": 99.99,
                "cantidad": 100
            }
        }