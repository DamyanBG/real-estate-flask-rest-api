import enum


class RoleType(enum.Enum):
    user = "admin"
    seller = "seller"
    admin = "user"


class MeetingStatusType(enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
