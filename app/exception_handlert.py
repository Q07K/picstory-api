from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from app.schemas.base_response import ErrorDetail, ErrorResponse


async def custom_exception_response(
    _: Request,
    exc: HTTPException,
) -> JSONResponse:
    """Exception handling function

    Parameters
    ----------
    _ : Request
        Request object
    exc : HTTPException
        Raised HTTP Exception

    Returns
    -------
    JSONResponse
        Custom 응답 형식
    """
    response = ErrorResponse(
        error=ErrorDetail(
            code=f"error.{exc.status_code}",
            message=exc.detail,
            details=None,
        )
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump(),
    )
