from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CompraBase(BaseModel):
    fecha: datetime = Field(default_factory=datetime.utcnow, title="Fecha de la compra")
    valor_a_pagar: float = Field(..., title="Valor a pagar")
    metodo_de_pago: str = Field(..., title="Método de pago", max_length=30)
    producto_id: int = Field(..., title="ID del producto asociado")

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "fecha": "2024-05-19T15:00:00",
                "valor_a_pagar": 100.0,
                "metodo_de_pago": "Tarjeta de crédito",
                "producto_id": 1
            }
        }

class CompraCreate(CompraBase):
    pass

class Compra(CompraBase):
    id: Optional[int] = Field(default=None, title="ID de la compra")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "fecha": "2024-05-19T15:00:00",
                "valor_a_pagar": 100.0,
                "metodo_de_pago": "Tarjeta de crédito",
                "producto_id": 1
            }
        }
