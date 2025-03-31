"""User routes definition
"""
from typing import Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session
from log import get_logger
from dependencies import get_db_session

from user.service import UserService
from user.schemas import UserData

log = get_logger(__name__)
db_session: Session = Depends(get_db_session)

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/{user_id}", response_model=Optional[UserData])
def get_user(user_id: str, db_session: Session = db_session):
    """Getting user information"""
    log.debug(f"Handling user get request for id: {user_id}")
    user: UserData = UserService(db_session).get_user(user_id)
    log.debug(f"user info for id: {user_id}, is: {user}")
    return user
