"""Exceptions for user endpoints"""


class UserBaseException(Exception):
    def __init__(self, message: str = ""):
        pass


class UserReadException(UserBaseException):
    """Exception for reading user values"""
    pass


class UserWriteException(UserBaseException):
    """Exception for writing user values"""
    pass


class UserInvalidException(UserBaseException):
    """Exception for invalid user"""
    pass


class UserDeleteException(UserBaseException):
    """Exception for invalid user"""
    pass


class UserUpdateException(UserBaseException):
    """Exception for invalid user"""
    pass


class UserIdDataException(UserBaseException):
    "Invalid user id"
    pass
