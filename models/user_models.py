from db import db

from models.enums import RoleType


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(RoleType), nullable=False)