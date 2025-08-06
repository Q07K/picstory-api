"""challenge winners model(entity)"""

import uuid

from sqlalchemy import ForeignKey, Integer, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


# pylint:disable=not-callable, too-few-public-methods
class ChallengeWinnerModel(Base):
    """database challenge winners Model(Entity)"""

    __tablename__ = "challenge_winners"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    challenge_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("challenges.id"),
        nullable=False,
        index=True,
    )
    post_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("posts.id"),
        nullable=False,
        index=True,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )
    rank: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )

    # Relationships
    challenge = relationship(
        argument="ChallengeModel",
        back_populates="winners",
    )
    post = relationship(
        argument="PostModel",
        back_populates="challenge_winner",
    )
    user = relationship(
        argument="UserModel",
        back_populates="challenge_winners",
    )
