"""users model(entity)"""

import uuid

from sqlalchemy import String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


# pylint:disable=not-callable, too-few-public-methods
class UserModel(Base):
    """database users Model(Entity)"""

    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    username: Mapped[str] = mapped_column(
        String(length=30),
        unique=True,
        index=True,
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(length=255),
        unique=True,
        index=True,
        nullable=False,
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )
    profile_image_url: Mapped[str | None] = mapped_column(
        String(length=2048),
        nullable=True,
        default=None,
    )
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationships
    created_groups = relationship(
        argument="GroupModel",
        back_populates="creator",
    )
    posts = relationship(
        argument="PostModel",
        back_populates="user",
    )
    likes = relationship(
        argument="LikeModel",
        back_populates="user",
    )
    comments = relationship(
        argument="CommentModel",
        back_populates="user",
    )
    created_invitation_codes = relationship(
        argument="InvitationCode",
        back_populates="creator",
    )
