"""invitation codes model(entity)"""

import uuid

from sqlalchemy import ForeignKey, INT, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


# pylint:disable=not-callable, too-few-public-methods
class InvitationCode(Base):
    """database invitation codes Model(Entity)"""

    __tablename__ = "invitation_codes"
    code: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
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
    expired_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        index=True,
    )
    max_uses: Mapped[int] = mapped_column(
        INT,
        nullable=False,
        default=3,
    )
    current_uses: Mapped[int] = mapped_column(
        INT,
        nullable=False,
        default=0,
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
    group = relationship(
        argument="GroupModel",
        back_populates="invitation_codes",
    )
    creator = relationship(
        argument="UserModel",
        back_populates="created_invitation_codes",
    )
