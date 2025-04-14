"""Global rest api dependencies.
"""
from sqlmodel import Session
from config import Settings, get_settings
from database import session
from schemas import AppInfo


def get_app_info() -> AppInfo:
    """Function provides the rest application information"""
    settings = get_settings()
    app_info = AppInfo(app_name=settings.app_name,
                       app_version=settings.app_version,
                       app_env=settings.app_env)
    return app_info


def get_api_settings() -> Settings:
    """Function to provide rest server settings"""
    return get_settings()


def get_db_session() -> Session:
    """Function provides db session as dependency"""
    return session()
