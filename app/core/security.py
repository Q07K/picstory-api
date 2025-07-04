from datetime import datetime, timedelta, timezone

import bcrypt
from jose import jwt
from passlib.context import CryptContext

from app.config import settings

# 패스워드 해싱 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """일반 비밀번호와 해시된 비밀번호가 일치하는지 확인합니다.

    Parameters
    ----------
    plain_password : str
        일반 비밀번호.
    hashed_password : str
        해시된 비밀번호.

    Returns
    -------
    bool
        비밀번호가 일치하면 True, 그렇지 않으면 False.
    """
    return bcrypt.checkpw(
        password=bytes(plain_password, encoding="utf-8"),
        hashed_password=bytes(hashed_password, encoding="utf-8"),
    )


def get_password_hash(password: str) -> str:
    """일반 비밀번호를 해싱합니다.

    Parameters
    ----------
    password : str
        일반 비밀번호.

    Returns
    -------
    str
        해시된 비밀번호.
    """
    return bcrypt.hashpw(
        password=bytes(password, encoding="utf-8"),
        salt=bcrypt.gensalt(),
    )


def create_token(
    data: dict,
    expires_delta: timedelta | None = None,
) -> str:
    """JWT 토큰을 생성합니다.

    Parameters
    ----------
    data : dict
        토큰에 포함될 데이터.
    expires_delta : timedelta | None, optional
        토큰의 만료 시간 (기본값은 None).

    Returns
    -------
    str
        생성된 JWT 토큰.
    """
    to_encode = data.copy()

    expire = datetime.now(tz=timezone.utc)
    if expires_delta:
        expire += expires_delta
    else:
        expire += timedelta(minutes=settings.access_token_expire_minutes)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=settings.secret_key,
        algorithm=settings.algorithm,
    )
    return encoded_jwt


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
) -> str:
    """액세스 토큰을 생성합니다.

    Parameters
    ----------
    data : dict
        토큰에 포함될 데이터.
    expires_delta : timedelta | None, optional
        토큰의 만료 시간 (기본값은 None).

    Returns
    -------
    str
        생성된 액세스 토큰.
    """
    to_encode = data.copy()
    to_encode.update({"type": "access"})
    return create_token(data=to_encode, expires_delta=expires_delta)


def create_refresh_token(
    data: dict,
    expires_delta: timedelta | None = None,
) -> str:
    """리프레시 토큰을 생성합니다.

    Parameters
    ----------
    data : dict
        토큰에 포함될 데이터.
    expires_delta : timedelta | None, optional
        토큰의 만료 시간 (기본값은 None).

    Returns
    -------
    str
        생성된 리프레시 토큰.
    """
    to_encode = data.copy()
    to_encode.update({"type": "refresh"})
    return create_token(data=to_encode, expires_delta=expires_delta)
