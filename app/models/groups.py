"""groups model(entity)"""

# pylint:disable=not-callable, too-few-public-methods
import uuid

from sqlalchemy import ForeignKey, String, TIMESTAMP, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class GroupModel(Base):
    """database groups Model(Entity)"""

    __tablename__ = "groups"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    creator_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(column="users.id"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(
        String(length=100),
        unique=True,
        index=True,
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(
        Text,
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
    creator = relationship(
        argument="UserModel",
        back_populates="created_groups",
    )
    posts = relationship(
        argument="PostModel",
        back_populates="group",
    )
    invitation_codes = relationship(
        argument="InvitationCode",
        back_populates="group",
    )
