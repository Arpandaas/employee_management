# exceptions/handlers.py

from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exception import (
    UserNotFoundException
)


async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": "User not found"
        }
    )