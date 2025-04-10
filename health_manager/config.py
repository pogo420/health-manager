"""Global rest server configurations
"""
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from schemas import LogLevel, AppEnv


class Settings(BaseSettings):
    """Data class for rest server configuration"""
    app_name: str
    app_version: str
    app_env: AppEnv
    log_level: LogLevel
    db_url: str
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    """Function retuns the rest config as python object.
    It's loaded only onces in the lifetime of rest server.
    If any change is done in the env file, restart the server.
    """
    return Settings()
