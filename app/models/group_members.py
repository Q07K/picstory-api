"""group members model(entity)"""

import uuid

from sqlalchemy import ForeignKey, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


# pylint:disable=not-callable, too-few-public-methods
class GroupMembersModel(Base):
    """database group members Model(Entity)"""

    __tablename__ = "group_members"
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        primary_key=True,
        index=True,
    )
    group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("groups.id"),
        primary_key=True,
        index=True,
    )
    role: Mapped[str] = mapped_column(
        String(length=50),
        nullable=False,
        default="member",
    )
    joined_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
