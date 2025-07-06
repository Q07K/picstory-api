"""group members model(entity)"""

import uuid

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base
from app.enums import GroupRole


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
    role: Mapped[GroupRole] = mapped_column(
        SQLEnum(GroupRole),
        nullable=False,
        default=GroupRole.MEMBER,
    )
    joined_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
