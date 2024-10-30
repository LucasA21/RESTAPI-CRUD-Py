# User Management API

Esta es una API RESTful de gestión de usuarios desarrollada con FastAPI y una base de datos MySQL. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un modelo de usuario.

## Características

- **Endpoints CRUD**: Gestión completa de usuarios mediante endpoints `/users`.
- **Encriptación de contraseñas**: Las contraseñas se almacenan en la base de datos de forma segura con encriptación usando `cryptography`.
- **Validación de datos**: Utiliza Pydantic para validar datos de entrada y asegurar que cumplan con el esquema definido.

## Requisitos

- Python 3.9 o superior
- MySQL 

## Instalación

1. **Clonar el repositorio**:

    ```bash
    git clone <https://github.com/LucasA21/RESTAPI-CRUD-Py.git>
    
    cd RESTAPI-CRUD-Py
    ```

2. **Crear un entorno virtual con Anaconda**:

    ```bash
    conda create -n nombre_entorno python=3.9
    conda activate nombre_entorno
    ```

3. **Instalar las dependencias**:

    ```bash
    pip install fastapi uvicorn sqlalchemy pymysql cryptography pydantic
    ```

4. **Configurar la base de datos**:

    En `config/db.py`, asegúrate de actualizar la URL de la base de datos con tu usuario, contraseña y nombre de la base de datos en MySQL. Ejemplo:

    ```python
    engine = create_engine("mysql+pymysql://usuario:password@localhost:3306/storedb")
    ```

## Ejecución de la aplicación

1. **Iniciar el servidor**:

    Ejecuta el siguiente comando para iniciar el servidor con Uvicorn:

    ```bash
    uvicorn app:app --reload
    ```

2. **Probar la API**:

    La API estará disponible en `http://127.0.0.1:8000`. Puedes probar los endpoints accediendo a la documentación interactiva generada por FastAPI en:

    - Documentación Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - Documentación Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints principales

- `GET /users` - Obtener todos los usuarios.
- `POST /users` - Crear un nuevo usuario.
- `GET /users/{id}` - Obtener un usuario por su ID.
- `PUT /users/{id}` - Actualizar un usuario existente.
- `DELETE /users/{id}` - Eliminar un usuario por su ID.

