from fastapi import FastAPI
from src.models.rol import Base
from src.routers.rol import roles_router
from src.routers.producto import productos_router
from src.routers.veterinario import veterinarios_router
from src.config.database import Base, engine
from src.models.veterinario import Base, Veterinario
from src.models.citas import Base
from src.routers.cita import citas_router
from src.models.mascota import Base
from src.routers.mascota import mascotas_router
from src.models.cliente import Base
from src.routers.cliente import clientes_router
from src.models.compra import Base
from src.routers.compra import compras_router
from src.routers.auth import auth_router
from src.models.user import Base
from src.routers.user import users_router

#################################################
app = FastAPI()
app.title = "Proyecto Final"
app.summary = "Gestion de informacion en una veterinaria"
app.version = "0.0.2"
app.contact = {
    "name": "Valeria Herrera Parra - Katherin Castaño",
    "email": "valeria.herrerap@autonoma.edu.co",
}
#################################################


# Define un endpoint de prueba para verificar que la aplicación funciona
@app.get("/")
def read_root():
    return {"message": "Welcome to the Producto API"}

#Rutas
app.include_router(router=productos_router)
app.include_router(router=veterinarios_router)
app.include_router(router=roles_router)
app.include_router(router=citas_router)
app.include_router(router=mascotas_router)
app.include_router(router=clientes_router)
app.include_router(router=users_router)
app.include_router(router=compras_router)
app.include_router(auth_router, prefix="/auth", tags=["auth"])

print("Creando todas las tablas...")
Base.metadata.create_all(bind=engine)