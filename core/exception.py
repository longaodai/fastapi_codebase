from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from core.response import ResponseError
from app.enums.error_code_enum import ErrorCodeEnum


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {}
    for err in exc.errors():
        loc = err.get("loc", [])
        if len(loc) > 1 and loc[0] == "body":
            field = loc[1]
            msg = err.get("msg")
            errors.setdefault(field, []).append(msg)

    response_error = ResponseError(
        message="Validation failed",
        error_code=ErrorCodeEnum.VALIDATION_ERROR.value,
        details=errors
    )
    return JSONResponse(status_code=422, content=response_error.dict())

async def http_exception_handler(request: Request, exc: HTTPException):
    if isinstance(exc.detail, dict):
        content = exc.detail
    else:
        content = ResponseError(
            message=str(exc.detail),
            error_code=str(exc.status_code),
            details=None
        ).dict()

    return JSONResponse(
        status_code=exc.status_code,
        content=content
    )

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )
