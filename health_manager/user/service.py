"""User service: For processing data from db and preparing the server response.

User service is middle layer between routes and data access layer.

TODO:
    - updating user service.
    - adding Uts for current code.
"""


from typing import Optional
from sqlalchemy.orm import Session
from user.exceptions import UserInvalidException, UserReadException
from user.utils import generate_user_id
from user.schemas import UserData, UserDbData
from user.repository import UserRepository
from log import get_logger

logger = get_logger()


class UserService:
    """UserService does data processing before and after db queries.

    Attributes:
        _session: Db session to be used in data access layer.
    """
    def __init__(self, session: Session):
        self._session: Session = session

    def get_user(self, user_id: str) -> Optional[UserDbData]:
        """Method calls DAL api to get user data.

        Args:
            user_id: Unique user identifier.

        Returns:
            User information received from DAL api

        Raises:
            None
        """
        try:
            return UserRepository(session=self._session).get_user(user_id)
        except UserInvalidException:
            logger.info(f"User information not found, for user_id: {user_id}")
        except UserReadException as e:
            logger.info(f"Issue in querying for user_id: {user_id}, details: {e}")
        return None

    def delete_user(self, user_id: str) -> None:
        """Method calls DAL api to DELETE a partipular user.

        Args:
            user_id: Unique user identifier.

        Returns:
            None

        Raises:
            UserReadException: Any issues in qerying user id.
            UserDeleteException: Any issues in deleting data.
            UserInvalidException: If user do not exist or invalid.
        """
        return UserRepository(session=self._session).delete_user(user_id)

    def add_user(self, user_data: UserData) -> UserDbData:
        """Method adds user in db via DAL api

        Args:
            user_data: UserData object containing user information

        Returns:
            User object, which signifies a added row from User table

        Raises:
            UserWriteException: Any issues in writing data.
        """
        user_id: str = generate_user_id()
        return UserRepository(session=self._session).add_user(user_id=user_id, user_data=user_data)
