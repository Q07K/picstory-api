from fastapi import APIRouter

from app.schemas.base_response import SuccessResponse

router = APIRouter(prefix="/v1/groups", tags=["group-invitations"])



@router.get(
    path="/{group_id}/invitations",
    response_model=SuccessResponse[],
)
def get_group_invitations(group_id: str):
    """생성된 그룹 초대 코드 목록을 조회합니다.

    - **group_id**: 조회할 그룹의 ID
    """

@router.post(
    path="/{group_id}/invitations",
    response_model=SuccessResponse[],
)
def create_group_invitation(group_id: str):
    """그룹 초대 코드를 생성합니다.

    - **group_id**: 생성할 그룹의 ID
    """

@router.delete(
    path="/{group_id}/invitations/{invitation_id}",
    response_model=SuccessResponse[],
)
def delete_group_invitation(group_id: str, invitation_id: str):
    """생성된 그룹 초대 코드를 삭제합니다.

    - **group_id**: 삭제할 그룹의 ID
    - **invitation_id**: 삭제할 초대 코드의 ID
    """

@router.post(
    path="/{group_id}/invitations/{invitation_id}/email",
    response_model=SuccessResponse[],
)
def send_group_invitation(group_id: str, invitation_id: str):
    """생성된 그룹 초대 코드를 이메일로 전송합니다.

    - **group_id**: 전송할 그룹의 ID
    - **invitation_id**: 전송할 초대 코드의 ID
    """
