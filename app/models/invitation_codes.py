"""invitations model(entity)"""

import uuid

from sqlalchemy import ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


# pylint:disable=not-callable, too-few-public-methods
class InvitationModel(Base):
    """database invitations Model(Entity)"""

    __tablename__ = "invitations"
    code: Mapped[str] = mapped_column(
        String(length=255),
        primary_key=True,
        index=True,
    )
    group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("groups.id"),
        nullable=False,
        index=True,
    )
    creator_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )
    expires_at: Mapped[TIMESTAMP | None] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
    )
    max_uses: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )
    use_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )

    # Relationships
    group = relationship(
        argument="GroupModel",
        back_populates="invitations",
    )
    creator = relationship(
        argument="UserModel",
        back_populates="created_invitation_codes",
    )
