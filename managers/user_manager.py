from psycopg2.errorcodes import UNIQUE_VIOLATION
from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.user_models import UserModel
from models.enums import RoleType 


class UserManager:
    @staticmethod
    def register_user(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = UserModel(**user_data, role=RoleType.user)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                # To find better error description, this is database error, not back end sever error
                raise InternalServerError("Server error")
        return user

    @staticmethod
    def register_seller(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = UserModel(**user_data, role=RoleType.seller)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                # To find better error description, this is database error, not back end sever error
                raise InternalServerError("Server error")
        return user

    @staticmethod
    def login_user(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def login_seller(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def login(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def login_admin(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def create_admin(data):
        data["password"] = generate_password_hash(data["password"])
        admin = UserModel(**data)
        db.session.add(admin)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                InternalServerError("Server error")
        return admin

    @staticmethod
    def select_user_names(user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        user_names = f"{user.first_name} {user.last_name}"
        return user_names
    
    @staticmethod
    def select_user_names_as_dict(user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        user_names = {
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        return user_names
