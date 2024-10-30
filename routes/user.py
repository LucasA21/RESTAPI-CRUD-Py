from fastapi import APIRouter, Response
from models.user import users
from config.db import conn
from schemas.user import User
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)


user = APIRouter()

@user.get("/users")
def get_users():
    result =  conn.execute(users.select()).fetchall()
    users_list = [dict(row._mapping) for row in result]
    return jsonable_encoder(users_list)

@user.post("/users")
def create_user(user : User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    conn.commit()
    created_user = conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
    return jsonable_encoder(dict(created_user._mapping)) if created_user else None

@user.get("/users/{id}")
def get_user(id:str):
    user = conn.execute(users.select().where(users.c.id == id)).first()
    return jsonable_encoder(dict(user._mapping)) if user else None

@user.delete("/users/{id}")
def delete_user(id:str):
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/{id}")
def update_user(id:str, user : User):
    conn.execute(users.update().values(name = user.name, email = user.email, 
                                       password = f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    conn.commit()
    user = conn.execute(users.select().where(users.c.id == id)).first()
    return jsonable_encoder(dict(user._mapping)) if user else None