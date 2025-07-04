from typing import Any

from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    code: str = Field(default=..., description="오류 코드")
    message: str = Field(default=..., description="오류 메시지")
    details: dict[str, Any] | None = Field(
        default=None,
        description="추가적인 오류 세부 정보",
    )


class ErrorResponse(BaseModel):
    success: bool = Field(default=False, description="요청 성공 여부")
    error: ErrorDetail = Field(default=..., description="오류 세부 정보")


class SuccessResponse[T](BaseModel):
    success: bool = Field(default=True, description="요청 성공 여부")
    code: str = Field(default=..., description="요청 성공 코드")
    message: str | None = Field(
        default=None,
        description="요청에 대한 추가 메시지",
    )
    data: T | None = Field(default=None, description="요청 결과 데이터")
