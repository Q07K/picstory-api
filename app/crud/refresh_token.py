from sqlalchemy.orm import Session

from app.models.refresh_tokens import RefreshTokenModel


def create_refresh_token(
    session: Session,
    model: RefreshTokenModel,
) -> RefreshTokenModel:
    session.add(instance=model)
    session.commit()
    session.refresh(instance=model)
    return model
