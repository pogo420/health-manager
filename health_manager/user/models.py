"""Database models for User endpoints. Following tables are covered:
* User table
"""
from sqlmodel import SQLModel, Field
from user.schemas import Gender


class User(SQLModel, table=True):
    """User table definition"""
    _tablename__ = "user"

    user_id: str = Field(primary_key=True, nullable=False)
    user_name: str = Field(nullable=False)
    gender: Gender = Field(nullable=True)
    height: int = Field(gt=0, nullable=True)
    birth_year: int = Field(gt=0, nullable=True)
