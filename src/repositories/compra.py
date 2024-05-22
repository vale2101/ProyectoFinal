from sqlalchemy.orm import Session
from src.models.compra import Compra as CompraModel
from src.models.producto import Producto as ProductoModel
from src.schemas.compra import CompraCreate

class CompraRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_compra(self, compra: CompraCreate) -> CompraModel:
        new_compra = CompraModel(**compra.dict())
        producto = self.db.query(ProductoModel).filter(ProductoModel.id == compra.producto_id).first()
        if producto and producto.cantidad > 0:
            producto.cantidad -= 1
            new_compra.valor_a_pagar = producto.precio
            self.db.add(new_compra)
            self.db.commit()
            self.db.refresh(new_compra)
            self.db.refresh(producto)
        else:
            raise ValueError("Producto no encontrado o sin stock")
        return new_compra
