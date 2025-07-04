from sqlalchemy.orm import Session

from app.models.users import UserModel


def create_user(session: Session, model: UserModel) -> UserModel:
    session.add(instance=model)
    session.commit()
    session.refresh(instance=model)
    return model


def get_user_by_email(session: Session, email: str) -> UserModel | None:
    return session.query(UserModel).filter(UserModel.email == email).first()


def get_user_by_id(session: Session, user_id: str) -> UserModel | None:
    return session.query(UserModel).filter(UserModel.id == user_id).first()
