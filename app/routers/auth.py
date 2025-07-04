from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.crud.crud_users import create_user, get_user_by_email
from app.database.database import get_db
from app.models.users import UserModel
from app.schemas.auth import LoginRequest, RefreshTokenRequest, Token
from app.schemas.base_response import SuccessResponse
from app.schemas.users import UserBase, UserCreate
from app.services.auth_service import (
    authenticate_user,
    create_tokens,
    refresh_user_tokens,
)

router = APIRouter(prefix="/v1/auth", tags=["authentication"])


@router.post(
    path="/register",
    response_model=SuccessResponse[UserBase],
    summary="Register a new user",
    responses={
        200: {"description": "User successfully registered"},
        400: {"description": "Username already registered"},
    },
)
async def register(
    data: UserCreate,
    session: Session = Depends(dependency=get_db),
) -> SuccessResponse[UserBase]:
    """
    Register a new user account.

    - **username**: Unique username for the user
    - **email**: Valid email address (must be unique)
    - **password**: User's password (will be hashed)

    Returns the created user information without sensitive data.
    """
    existing_user = get_user_by_email(session=session, email=data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    hashed_password = get_password_hash(password=data.password)

    model = create_user(
        session=session,
        model=UserModel(
            username=data.username,
            email=data.email,
            hashed_password=hashed_password,
        ),
    )

    return SuccessResponse[UserBase](
        code="user.created",
        message="User successfully registered",
        data=UserBase(
            username=model.username,
            email=model.email,
        ),
    )


@router.post(
    path="/login",
    response_model=SuccessResponse[Token],
    summary="User login with OAuth2",
    responses={
        200: {"description": "User successfully logged in"},
        401: {"description": "Incorrect email or password"},
    },
)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(dependency=get_db),
) -> SuccessResponse[Token]:
    """
    Login user using OAuth2 password flow.

    - **username**: User's email address (OAuth2 standard uses 'username' field)
    - **password**: User's password

    Returns access token and refresh token for API authentication.
    """
    user = authenticate_user(
        session=session,
        email=form_data.username,  # Oauth2 username field is used for email
        password=form_data.password,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    tokens = create_tokens(user=user)

    return SuccessResponse[Token](
        code="user.logged_in",
        message="User successfully logged in",
        data=tokens,
    )


@router.post(
    path="/login-json",
    response_model=SuccessResponse[Token],
    summary="User login with JSON data",
    responses={
        200: {"description": "User successfully logged in"},
        401: {"description": "Incorrect email or password"},
    },
)
async def login_json(
    data: LoginRequest,
    session: Session = Depends(dependency=get_db),
) -> SuccessResponse[Token]:
    """
    Login user using JSON request body.

    - **email**: User's email address
    - **password**: User's password

    Returns access token and refresh token for API authentication.
    Alternative to OAuth2 form-based login for JSON-based clients.
    """
    user = authenticate_user(
        session=session,
        email=data.email,
        password=data.password,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    tokens = create_tokens(user=user)

    return SuccessResponse[Token](
        code="user.logged_in",
        message="User successfully logged in",
        data=tokens,
    )


@router.post(
    path="/refresh-token",
    response_model=SuccessResponse[Token],
    summary="Refresh access token",
    responses={
        200: {"description": "Token successfully refreshed"},
        401: {"description": "Invalid or expired refresh token"},
    },
)
async def refresh_token(
    data: RefreshTokenRequest,
    session: Session = Depends(dependency=get_db),
) -> SuccessResponse[Token]:
    """
    Refresh user's access token using a valid refresh token.

    - **refresh_token**: Valid refresh token

    This endpoint uses the refresh token to generate new access and refresh tokens
    without requiring the user to re-enter their credentials.

    Returns new access token and refresh token.
    """
    tokens = refresh_user_tokens(
        session=session,
        refresh_token=data.refresh_token,
    )
    if not tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return SuccessResponse[Token](
        code="user.token_refreshed",
        message="User token successfully refreshed",
        data=tokens,
    )
