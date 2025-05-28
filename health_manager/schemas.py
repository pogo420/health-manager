"""Common schemas of the rest api. All data trasfer objects are present here.
"""
from enum import Enum
from pydantic import BaseModel


class AppEnv(Enum):
    """Enum for env values"""
    dev = "dev"
    prod = "prod"
    local = "local"


class LogLevel(Enum):
    """Enum for log levels"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class AppInfo(BaseModel):
    """Data class for rest application information"""
    app_name: str
    app_version: str
    app_env: AppEnv


class ErrorMessage(BaseModel):
    """Structure of all error message in application"""
    detail: str


class SuccessMessage(BaseModel):
    """Structure of all generic success message in application"""
    detail: str
