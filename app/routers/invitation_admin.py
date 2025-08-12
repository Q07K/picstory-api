from fastapi import APIRouter

from app.schemas.base_response import SuccessResponse

router = APIRouter(prefix="/v1/admin/invitations", tags=["invitations"])


@router.get(
    path="/",
    response_model=SuccessResponse[],
)
def get_invitations():
    """생성된 초대 코드 목록을 조회합니다."""


@router.delete(
    path="/{invitation_id}",
    response_model=SuccessResponse[],
)
def delete_invitation(invitation_id: str):
    """생성된 초대 코드를 삭제합니다.

    - **invitation_id**: 삭제할 초대 코드의 ID
    """

@router.post(
    path="/{invitation_id}/email",
    response_model=SuccessResponse[],
)
def send_invitation(invitation_id: str):
    """생성된 초대 코드를 이메일로 전송합니다.

    - **invitation_id**: 전송할 초대 코드의 ID
    """

