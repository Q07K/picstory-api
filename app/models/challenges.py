"""challenges model(entity)"""

import uuid

from sqlalchemy import Enum, String, TIMESTAMP, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


# pylint:disable=not-callable, too-few-public-methods
class ChallengeModel(Base):
    """database challenges Model(Entity)"""

    __tablename__ = "challenges"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    title: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    start_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
    )
    end_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
    )
    status: Mapped[str] = mapped_column(
        Enum(
            "UPCOMING",
            "ACTIVE",
            "COMPLETED",
            name="challenge_status",
        ),
        nullable=False,
        default="UPCOMING",
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
    posts = relationship(
        argument="PostModel",
        back_populates="challenge",
    )
    winners = relationship(
        argument="ChallengeWinnerModel",
        back_populates="challenge",
    )
