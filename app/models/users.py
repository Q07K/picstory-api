"""users model(entity)"""

import uuid

from sqlalchemy import Column, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


# pylint:disable=not-callable, too-few-public-methods
class UserModel(Base):
    """database users Model(Entity)"""

    __tablename__ = "users"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    username = Column(
        String(length=30),
        unique=True,
        index=True,
        nullable=False,
    )
    email = Column(
        String(length=255),
        unique=True,
        index=True,
        nullable=False,
    )
    hashed_password = Column(
        String(length=255),
        nullable=False,
    )
    profile_image_url = Column(
        String(length=2048),
        nullable=True,
        default=None,
    )
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
