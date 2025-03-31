"""Data access layer for user related endpoints.
Low level db queries.
"""
from typing import Optional
from log import get_logger
from user.models import User
from user.schemas import UserData
from sqlmodel import Session, select

log = get_logger(__name__)


class UserRepository:
    """Class handling user related low level queries."""
    def __init__(self, session: Session):
        self._session: Session = session

    def get_user(self, user_id: str) -> Optional[UserData]:
        """Returns the user data from db"""
        log.debug(f"getting user info from db for user_id:{user_id}")
        with self._session as db_session:
            user_data_raw = db_session.exec(select(User).where(User.user_id == user_id)).one_or_none()
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
