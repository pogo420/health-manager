"""Utlity specific to user endpoints

Few utility methods are garaged here
    - generating user_id
    - adding Uts for current code.
"""
from uuid import uuid4


def generate_user_id() -> str:
    """Function generates user id via uuid4 protocol

    Returns:
        32 bit uuid
    """
    return uuid4().hex
