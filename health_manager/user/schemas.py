"""File containing user data transfer objects
"""
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Gender(Enum):
    Male = "male"
    Female = "female"
    Others = "others"


class UserData(BaseModel):
    """User data from client"""
    user_name: str
    gender: Optional[Gender]
    height: Optional[int] = Field(gt=0)
    birth_year: Optional[int] = Field(gt=0)


class UserDbData(UserData):
    """User data in db - single row"""
    user_id: str
