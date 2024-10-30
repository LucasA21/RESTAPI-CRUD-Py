from pydantic import BaseModel

class User(BaseModel):
    id: str = None
    name: str
    email: str
    password: str