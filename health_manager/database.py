"""File containing database connection logics"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from health_manager.config import get_settings
from health_manager.log import get_logger

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
