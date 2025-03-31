"""Global rest api dependencies
"""
from config import get_settings
from schemas import AppInfo


def get_app_info() -> AppInfo:
    """Function provides the rest application information"""
    settings = get_settings()
    app_info = AppInfo(app_name=settings.app_name,
                       app_version=settings.app_version,
                       app_env=settings.app_env)
    return app_info
