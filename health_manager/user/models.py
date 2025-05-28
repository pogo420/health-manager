"""Database models for User endpoints. Following tables are covered:
* User table
"""
from sqlalchemy import Column, String, Integer
from health_manager.database import Base


class User(Base):
    """User table definition"""
    __tablename__ = "user"

    user_id: str = Column(String, primary_key=True, index=True, nullable=False)
    user_name: str = Column(String, nullable=False)
    gender: str = Column(String, nullable=True)
    height: int = Column(Integer, nullable=True)
    birth_year: int = Column(Integer, nullable=True)
