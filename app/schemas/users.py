from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(default=..., description="사용자 이름")
    email: str = Field(default=..., description="사용자 이메일")


class UserCreate(UserBase):
    password: str = Field(default=..., description="사용자 비밀번호")
    invitation_code: str = Field(default=..., description="초대 코드")
