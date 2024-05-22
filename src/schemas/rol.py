from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Role(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the role")
    name: str = Field(min_length=3, max_length=50, title="Name of the role")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Admin"
            }
        }