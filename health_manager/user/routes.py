"""User routes definition
"""
from fastapi import APIRouter

router = APIRouter(
    prefix="/user"
)


@router.get("/{user_id}")
async def get_user(user_id: str):
    return {"message": f"received user id is:{user_id}"}
