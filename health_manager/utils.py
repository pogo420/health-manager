"""File containing global utility logics"""
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


def error_response(status_code: int, message: BaseModel) -> JSONResponse:
    return JSONResponse(
        content=jsonable_encoder(message),
        status_code=status_code
    )


def success_response(status_code: int, message: BaseModel) -> JSONResponse:
    return JSONResponse(
        content=jsonable_encoder(message),
        status_code=status_code
    )
