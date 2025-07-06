"""Group role enums"""

from enum import Enum


class GroupRole(str, Enum):
    """Group member role enum"""

    ADMIN = "admin"
    MANAGER = "manager"
    MEMBER = "member"
