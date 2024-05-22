from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the user")
    name: str = Field(min_length=4, max_length=60, title="Name of the user")
    email: EmailStr = Field(min_length=6, max_length=64, title="Email of the user")
    password: str = Field(max_length=64, title="Password of the user")
    is_active: bool = Field(default=True, title="Status of the user")
    id_rol: Optional[int] = Field(default=None, title="Role ID of the user")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Pepe Pimentón",
                "email": "pepe@base.net",
                "password": "xxx",
                "is_active": True,
                "id_rol": 2
            }
        }

class UserCreate(BaseModel):
    name: str = Field(min_length=4, max_length=60, title="Name of the user")
    email: EmailStr = Field(min_length=6, max_length=64, title="Email of the user")
    password: str = Field(max_length=64, title="Password of the user")
    id_rol: Optional[int] = Field(default=None, title="Role ID of the user")

class UserLogin(BaseModel):
    email: EmailStr = Field(min_length=6, max_length=64, alias="username", title="Email of the user")
    password: str = Field(min_length=4, title="Password of the user")
