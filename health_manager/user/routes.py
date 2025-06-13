"""User routes definitions.

Currently we have sync endpoints for:
- getting user data.

TODO:
    - updating user route.
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from health_manager.schemas import ErrorMessage, SuccessMessage
from health_manager.utils import error_response, success_response
from health_manager.user.exceptions import (UserDeleteException, UserIdDataException,
                                            UserInvalidException,
                                            UserReadException,
                                            UserWriteException)
from health_manager.log import get_logger
from health_manager.dependencies import get_db_session
from health_manager.user.service import UserService
from health_manager.user.schemas import UserData, UserDbData

log = get_logger(__name__)
db_session: Session = Depends(get_db_session)

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/{user_id}", responses={
    200: {"model": UserDbData},
    404: {"model": ErrorMessage},
    500: {"model": ErrorMessage}
})
def get_user(user_id: str, db_session: Session = db_session):
    """Route for providing user information
    """
    log.info(f"Handling user get request for id: {user_id}")

    user: UserDbData
    try:
        user: UserDbData = UserService(db_session).get_user(user_id)
    except UserInvalidException:
        log.error(f"User_id:{user_id} do not exist.")
        return error_response(
            status_code=status.HTTP_404_NOT_FOUND,
            message=ErrorMessage(detail=f"User_id:{user_id} do not exist.")
            )
    except UserReadException:
        log.error(f"Issue in querying data for user_id:{user_id}")
        return error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=ErrorMessage(detail=f"Issue in querying data for user_id:{user_id}")
            )
    else:
        log.debug(f"User info for id: {user_id}, is: {user}")
        return user


@router.post("/", responses={
    200: {"model": UserDbData},
    500: {"model": ErrorMessage}
})
def add_user(payload: UserData, db_session: Session = db_session):
    """Route adds a new user into db"""
    log.info(f"Trying to create a user with payload: {payload}")
    user: UserDbData
    try:
        user = UserService(db_session).add_user(payload)
    except UserIdDataException:
        log.error(f"User_id generation issues for payload:{payload}")
        return error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=ErrorMessage(detail=f"User_id generation issues for payload:{payload}")
            )
    except UserWriteException:
        log.error(f"Issue in updating db for payload:{payload}")
        return error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=ErrorMessage(detail=f"Issue in updating db for payload:{payload}")
            )
    return user


@router.delete("/{user_id}", responses={
    200: {"model": SuccessMessage},
    404: {"model": ErrorMessage},
    500: {"model": ErrorMessage}
})
def delete_user(user_id: str, db_session: Session = db_session):
    """Endpoint to delete a user"""
    try:
        UserService(db_session).delete_user(user_id=user_id)
    except UserDeleteException:
        log.error(f"Not able to delete the user id: {user_id}")
        return error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=ErrorMessage(detail=f"Issue in querying data for user_id:{user_id}")
            )
    except UserInvalidException:
        log.error(f"User_id:{user_id} do not exist.")
        return error_response(
            status_code=status.HTTP_404_NOT_FOUND,
            message=ErrorMessage(detail=f"User_id:{user_id} do not exist.")
            )
    else:
        # if no issues
        return success_response(
            status_code=status.HTTP_200_OK,
            message=SuccessMessage(detail=f"User_id:{user_id} deleted")
        )
