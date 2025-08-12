from pydantic import BaseModel, Field


class InvitationCode(BaseModel):
    code: str = Field(default=..., description="초대 코드")
    group_id: str = Field(default=..., description="그룹 ID")
    group_name: str = Field(default=..., description="그룹 이름")
    created_at: str = Field(default=..., description="초대 코드 생성일")
    expires_at: str = Field(default=..., description="초대 코드 만료일")
    use_count: int = Field(default=..., description="초대 코드 사용 횟수")
    max_uses: int | None = Field(
        default=None,
        description="초대 코드 최대 사용가능 횟수",
    )
