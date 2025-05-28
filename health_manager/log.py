"""Logging module for the rest server"""

import logging
import sys
from typing import Optional
from health_manager.config import get_settings

LOGGING_FORMATTER = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Creates and configures a logger for logging messages.

    Parameters:
        name (Optional[str]): The name of the logger. Defaults to None.

    Important:
        It takes log level from rest config

    Returns:
        logging.Logger: The configured logger object.
    """
    level = get_settings().log_level.value

    logger = logging.getLogger(name=name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(LOGGING_FORMATTER)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level=level)
    return logger
