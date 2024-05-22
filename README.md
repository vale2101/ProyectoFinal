# Proyecto final
Valeria Herrera Parra - Katherin Castaño Pineda
valeria.herrerap@autonoma.edu.co - katherine.castanop@autonoma.edu.co

# Descripcion
El sistema de respaldo para servicios veterinarios facilita la gestión de citas y la adquisición de productos de forma eficiente.


# Inicializar el proyecto
venv\Scripts\activate.bat  #inicializar variables de entorno

uvicorn main:app --reload  #correr el proyecto

# Endpoints

# Productos 
Get http://127.0.0.1:8000/producto

Post http://127.0.0.1:8000/producto

Put http://127.0.0.1:8000/producto/3

Delete http://127.0.0.1:8000/producto/2

# Compra
Post http://127.0.0.1:8000/compras

# Veterinario
Get http://127.0.0.1:8000/veterinario

Post http://127.0.0.1:8000/veterinario

Put http://127.0.0.1:8000/veterinario/3

Delete http://127.0.0.1:8000/veterinario/2

# Usuario
Get http://127.0.0.1:8000/usuario

Put http://127.0.0.1:8000/usuario/3

Delete http://127.0.0.1:8000/usuario/2

# MASCOTA
Get http://127.0.0.1:8000/mascota

Post http://127.0.0.1:8000/mascota

Put http://127.0.0.1:8000/mascota/3

Delete http://127.0.0.1:8000/mascota/2

# Cliente
Get http://127.0.0.1:8000/cliente

Post http://127.0.0.1:8000/cliente

Put http://127.0.0.1:8000/cliente/3

Delete http://127.0.0.1:8000/cliente/2

# Roles
Get http://127.0.0.1:8000/roles

Post http://127.0.0.1:8000/roles

Put http://127.0.0.1:8000/roles/3

Delete http://127.0.0.1:8000/roles/2

# CITAS
Get http://127.0.0.1:8000/cita

Post http://127.0.0.1:8000/cita

Put http://127.0.0.1:8000/cita/3

Delete http://127.0.0.1:8000/cita/2

# AUTH
Post http://127.0.0.1:8000/auth/login

Post http://127.0.0.1:8000/auth/register










