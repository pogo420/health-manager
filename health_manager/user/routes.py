"""User routes definition
"""
from fastapi import APIRouter, Depends
from sqlmodel import Session
from log import get_logger
from dependencies import get_db_session

log = get_logger(__name__)
db_session: Session = Depends(get_db_session)

router = APIRouter(
    prefix="/user"
)


@router.get("/{user_id}")
async def get_user(user_id: str, db_session: Session = db_session):
    log.debug("handling user get request")
    return {"message": f"received user id is:{user_id}"}
