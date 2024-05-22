from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from src.models.producto import Base, Producto
from datetime import datetime

class Compra(Base):
    __tablename__ = "compras"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime, default=datetime.utcnow, nullable=False)
    valor_a_pagar = Column(Float, nullable=False)
    metodo_de_pago = Column(String(length=30), nullable=False)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    
    producto = relationship("Producto", back_populates="compras")
