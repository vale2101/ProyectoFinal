from typing import List
from sqlalchemy.orm import Session
from src.schemas.producto import ProductoModel
from src.models.producto import Producto as ProductoModelDB

class ProductoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_productos(self) -> List[ProductoModel]:
        query = self.db.query(ProductoModelDB)
        return query.all()

    def get_producto(self, id: int) -> ProductoModel:
        element = self.db.query(ProductoModelDB).filter(ProductoModelDB.id == id).first()
        return element

    def create_producto(self, producto: ProductoModel) -> ProductoModel:
        new_producto = ProductoModelDB(**producto.dict())
        self.db.add(new_producto)
        self.db.commit()
        self.db.refresh(new_producto)
        return new_producto

    def delete_producto(self, id: int) -> ProductoModel:
        element = self.db.query(ProductoModelDB).filter(ProductoModelDB.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def update_producto(self, id: int, producto: ProductoModel) -> ProductoModel:
        element = self.db.query(ProductoModelDB).filter(ProductoModelDB.id == id).first()
        
        if element:
            element.nombre = producto.nombre
            element.descripcion = producto.descripcion
            element.precio = producto.precio
            element.cantidad = producto.cantidad
            self.db.commit()
            self.db.refresh(element)
        return element
