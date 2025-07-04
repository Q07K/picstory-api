from datetime import timedelta

from sqlalchemy.orm import Session

from app.config import settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    verify_password,
    verify_token,
)
from app.crud.crud_users import get_user_by_email
from app.models.users import UserModel
from app.schemas.auth import Token


def authenticate_user(
    session: Session,
    email: str,
    password: str,
) -> None | UserModel:
    """사용자의 이메일과 비밀번호를 확인하여 인증된 사용자를 반환합니다.

    Parameters
    ----------
    session : Session
        데이터베이스 세션 객체.
    email : str
        사용자의 이메일 주소.
    password : str
        사용자의 비밀번호.

    Returns
    -------
    None | UserModel
        인증된 사용자 모델 객체를 반환하거나, 인증 실패 시 None을 반환.
    """
    user = get_user_by_email(session=session, email=email)
    if not user:
        return None

    try:
        verify_password(
            plain_password=password,
            hashed_password=user.hashed_password,
        )
        return user

    except ValueError:
        return None


def refresh_user_tokens(
    session: Session,
    refresh_token: str,
) -> None | Token:
    """리프레시 토큰을 사용하여 새로운 액세스 토큰과 리프레시 토큰을 생성합니다.

    Parameters
    ----------
    session : Session
        데이터베이스 세션 객체.
    refresh_token : str
        유효한 리프레시 토큰.

    Returns
    -------
    None | Token
        새로운 토큰 정보를 반환하거나, 인증 실패 시 None을 반환.
    """
    # 리프레시 토큰 검증
    payload = verify_token(token=refresh_token, token_type="refresh")
    if not payload:
        return None

    # 사용자 정보 확인
    email = payload.get("sub")
    if not email:
        return None

    user = get_user_by_email(session=session, email=email)
    if not user:
        return None

    # 새로운 토큰 생성
    return create_tokens(user=user)


def create_tokens(user: UserModel) -> Token:
    access_token_expires = timedelta(
        minutes=settings.access_token_expire_minutes,
    )
    refresh_token_expires = timedelta(
        days=settings.refresh_token_expire_days,
    )

    access_token = create_access_token(
        data={"sub": user.email, "username": user.username},
        expires_delta=access_token_expires,
    )
    refresh_token = create_refresh_token(
        data={"sub": user.email},
        expires_delta=refresh_token_expires,
    )

    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
    )
