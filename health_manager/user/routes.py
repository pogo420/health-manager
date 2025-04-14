"""User routes definitions.

Currently we have sync endpoints for:
- getting user data.
- deleting user data.
- adding user.

TODO:
    - updating user route.
    - deleting user data.
    - adding user.
    - adding Uts for current code.
"""
from typing import Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session
from log import get_logger
from dependencies import get_db_session

from user.service import UserService
from user.schemas import UserData, UserDbData

log = get_logger(__name__)
db_session: Session = Depends(get_db_session)

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/{user_id}", response_model=Optional[UserDbData])
def get_user(user_id: str, db_session: Session = db_session):
    """Getting user information"""
    log.info(f"Handling user get request for id: {user_id}")
    user: UserDbData = UserService(db_session).get_user(user_id)
    log.debug(f"User info for id: {user_id}, is: {user}")
    return user


@router.post("/{user_id}", response_model=Optional[UserDbData])
def add_user(user: UserData, db_session: Session = db_session):
    """Getting user information"""
    log.info(f"Trying to add user: {user}")
    user_response: UserDbData = UserService(db_session).add_user(user_data=user)
    log.debug(f"User data added: {user_response}")
    return user_response
