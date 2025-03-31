"""File containing database connection logics"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import get_settings
from log import get_logger

from contextlib import contextmanager

logger = get_logger(__name__)

api_settings = get_settings()
connect_args = {"check_same_thread": False}
engine = create_engine(api_settings.db_url, connect_args=connect_args)
DbSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


@contextmanager
def session():
    """Creates the db session for all commits"""
    db = DbSession()
    try:
        yield db
    finally:
        db.close()


