"""Data access layer for user related endpoints.

It contains low level db queries written via sqlalchemy.
Data access level only having debug queries.

TODO:
    - update user db query.
"""
from typing import Optional
from sqlalchemy.orm import Session

from health_manager.user.exceptions import (UserDeleteException,
                                            UserInvalidException,
                                            UserReadException,
                                            UserUpdateException,
                                            UserWriteException)
from health_manager.log import get_logger
from health_manager.user.models import User
from health_manager.user.schemas import UserData


log = get_logger(__name__)


class UserRepository:
    """Class manages user related low level queries.

    Only debug logs are enabled in User data access layer.

    Attributes:
        _session: Db session, used via context manager.
    """
    def __init__(self, session: Session):
        self._session: Session = session

    def get_user(self, user_id: str) -> Optional[User]:
        """Returns the user data from db

        Args:
            user_id: User identification string

        Returns:
            User object. It has retrived user information.

        Raises:
            UserInvalidException: if user data not found.
            UserReadException: Any issues in qerying data.
        """
        with self._session as db_session:
            try:
                log.debug(f"Getting user info from db for user_id:{user_id}")
                user_data_raw: Optional[User] = db_session\
                    .query(User).where(User.user_id == user_id).one_or_none()
            except Exception as e:
                log.debug(f"Issue in reading user_id:{user_id}")
                raise UserReadException(f"Issue in reading user_id:{user_id}, details:{e}")
            # If no user info
            if user_data_raw is None:
                log.debug(f"User with user_id:{user_id} not found.")
                raise UserInvalidException(f"User_id:{user_id} is invalid")

            return user_data_raw

    def add_user(self, user_id: str, user_data: UserData) -> Optional[User]:
        """Method adds user data into db

        Args:
            user_id: Unique user identifier.
            user_data: UserDbData object containing user information.

        Returns:
            user: User object containing user data written into server.

        Raises:
            UserWriteException: Any issues in writing data.
        """
        user = User(
            user_id=user_id,
            user_name=user_data.user_name,
            gender=user_data.gender.value,
            height=user_data.height,
            birth_year=user_data.birth_year
            )
        with self._session as db_session:
            try:
                log.debug(f"Trying to add user data: {user} into db")
                db_session.add(user)
            except Exception as e:
                log.debug(f"Issue in adding user data: {user} into db")
                raise UserWriteException(f"issue in writing user_id:{user_id}, details:{e}")
            else:
                db_session.commit()
                db_session.refresh(user)
                log.debug(f"Adding user data: {user} into db successful")
                return user

    def delete_user(self, user_id: str) -> None:
        """Deletes the user data from db

        Args:
            user_id: User identification string

        Returns:
            None

        Raises:
            UserDeleteException: Any issues in deleting data.
        """
        with self._session as db_session:
            try:
                # attempting delete
                log.debug(f"Deleting user with user_id:{user_id}")
                user_data_raw: Optional[User] = db_session\
                    .exec(User.where(User.user_id == user_id)).one_or_none()
                db_session.delete(user_data_raw)
            except Exception as e:
                log.debug(f"Issue in deleting user with user_id:{user_id}")
                raise UserDeleteException(f"User with user_id:{user_id}, could not be deleted, details: {e}")
            else:
                # commiting if delete sucessful
                db_session.commit()

    def update_user(self, user_id: str, update_user_dict: dict) -> Optional[User]:
        """Method updates user data in db

        Args:
            user_id: User identification string
            update_dict: A dictionary of following:
                key: User model parameter(user table column)
                value: new value of the table column

        Important:
            update_user_dict should contain columns, whoes data we want to change.
            Example: {User.birth_year: 9089, User.user_name: "sam"}

        Returns:
            Updated user data

        Raises:
            UserUpdateException: Incase of issues in updating db
        """
        user: User = User()
        with self._session as db_session:
            try:
                log.debug(f"Attempting to update user_id:{user_id}, with {update_user_dict}")
                db_session.query(User).where(User.user_id == user_id).update(
                    update_user_dict
                )
            except Exception as e:
                log.debug(f"Issue in updating user:{user_id} with {update_user_dict}, details: {e}")
                raise UserUpdateException(f"Issue in updating user:{user_id} with {update_user_dict}, details: {e}")
            else:
                log.debug(f"Updating user_id:{user_id}, with {update_user_dict}")
                db_session.commit()
                db_session.refresh(user)
                return user
