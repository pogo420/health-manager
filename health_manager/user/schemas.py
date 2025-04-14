"""File containing user data transfer objects
"""
from enum import Enum
from pydantic import BaseModel, Field


class Gender(Enum):
    Male = "male"
    Female = "female"
    Others = "others"


class UserData(BaseModel):
    """User data from client"""
    user_name: str = Field(nullable=False)
    gender: Gender = Field(nullable=True)
    height: int = Field(gt=0, nullable=True)
    birth_year: int = Field(gt=0, nullable=True)


class UserDbData(UserData):
    """User data in db - single row"""
    user_id: str = Field(nullable=False)
