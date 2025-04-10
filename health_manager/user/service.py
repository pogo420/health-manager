"""User service: For peocessing data from db and preparing the server response"""


from typing import Optional
from sqlmodel import Session
from user.schemas import UserData
from user.repository import UserRepository


class UserService:
    def __init__(self, session: Session):
        self._session: Session = session

    def get_user(self, user_id: str) -> Optional[UserData]:
        return UserRepository(session=self._session).get_user(user_id)
