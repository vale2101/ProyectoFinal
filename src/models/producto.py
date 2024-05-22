from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(length=60), nullable=False)
    descripcion = Column(String(length=400))
    precio = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)

    compras = relationship("Compra", back_populates="producto")

    def disminuir_cantidad(self):
        if self.cantidad > 0:
            self.cantidad -= 1
        else:
            raise ValueError("No hay suficiente stock para este producto")

