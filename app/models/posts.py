"""posts model(entity)"""

import uuid

from sqlalchemy import ForeignKey, Integer, String, TIMESTAMP, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


# pylint:disable=not-callable, too-few-public-methods
class PostModel(Base):
    """database posts Model(Entity)"""

    __tablename__ = "posts"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )
    group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("groups.id"),
        nullable=False,
        index=True,
    )
    challenge_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("challenges.id"),
        nullable=True,
        index=True,
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    image_url: Mapped[str] = mapped_column(
        String(length=2048),
        nullable=False,
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
    user = relationship(argument="UserModel", back_populates="posts")
    group = relationship(argument="GroupModel", back_populates="posts")
    likes = relationship(argument="LikeModel", back_populates="post")
    comments = relationship(argument="CommentModel", back_populates="post")
    challenge = relationship(argument="ChallengeModel", back_populates="posts")
    challenge_winner = relationship(
        argument="ChallengeWinnerModel", back_populates="post", uselist=False
    )
