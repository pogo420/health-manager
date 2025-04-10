"""Data access layer for user related endpoints.

It contains low level db queries written via [sqlmodel](https://sqlmodel.tiangolo.com/) orm.
sqlmodel is written with sqlalchemy and pydantic.
"""
from typing import Optional
from sqlmodel import Session, select

from user.exceptions import UserReadException, UserWriteException
from log import get_logger
from user.models import User
from user.schemas import UserData


log = get_logger(__name__)


class UserRepository:
    """Class manages user related low level queries.

    Attributes:
        session: Db session, used via context manager.
    """
    def __init__(self, session: Session):
        self._session: Session = session

    def get_user(self, user_id: str) -> Optional[UserData]:
        """Returns the user data from db

        Args:
            user_id: User identification string

        Returns:
            UserData object. It has retrived user information.
            Method returns None if no data is returned.

        Raises:
            UserReadException: Any issues in qerying data.
        """
        log.debug(f"getting user info from db for user_id:{user_id}")
        with self._session as db_session:
            try:
                user_data_raw: Optional[User] = db_session\
                    .exec(select(User).where(User.user_id == user_id)).one_or_none()
            except Exception as e:
                raise UserReadException(f"issue in reading user_id:{user_id}, details:{e}")
            # If no user info
            if user_data_raw is None:
                return None

            return UserData(
                user_id=user_id,
                user_name=user_data_raw.user_name,
                gender=user_data_raw.gender,
                height=user_data_raw.height,
                birth_year=user_data_raw.birth_year
            )

    def add_user(self, user_id: str, user_data: UserData) -> User:
        """Method adds user data into db

        Args:
            user_id: Unique user identifier.
            user_data: UserData object containing user information.

        Returns:
            user: User object containing user data written into server.

        Raises:
            UserWriteException: Any issues in writing data. 
        """
        user = User(
            user_id=user_id,
            user_name=user_data.user_name,
            gender=user_data.gender,
            height=user_data.height,
            birth_year=user_data.birth_year
            )
        with self._session as db_session:
            try:
                db_session.add(user)
                db_session.commit()
                db_session.refresh(user)
            except Exception as e:
                raise UserWriteException(f"issue in writing user_id:{user_id}, details:{e}")

        return user
