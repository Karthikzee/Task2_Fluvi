from beanie import Document
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4


class User(Document):
    """
    Schema for User Document
    """
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "user"

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@gmail.com",
            }
        }


class UpdateUser(BaseModel):
    """
    User update schema
    """
    name: Optional[str]
    email: Optional[str]
