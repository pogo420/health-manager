"""File containing database connection logics"""

from sqlmodel import SQLModel, Session, create_engine
from config import get_settings
from user.models import User  # noqa: F401; Required to create tables

api_settings = get_settings()
connect_args = {"check_same_thread": False}
engine = create_engine(api_settings.db_url, connect_args=connect_args)


def init_db():
    """Creating all tables based on the models"""
    SQLModel.metadata.create_all(engine)


def session():
    """Creates the db session for all commits"""
    with Session(engine) as session:
        yield session
