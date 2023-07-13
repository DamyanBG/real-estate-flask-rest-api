import enum


class RoleType(enum.Enum):
    user = "user"
    seller = "seller"
    admin = "admin"


class MeetingStatusType(enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
