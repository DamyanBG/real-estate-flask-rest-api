from flask import request
from flask_restful import Resource

from managers.auth_manager import AuthManager, auth
from managers.user_manager import UserManager
from schemas.request.user_request import (
    UserRegisterSchema,
    UserLoginSchema
)
from schemas.response.user_response import UserResponseSchema
from utils.decorators import validate_schema


class RegisterUser(Resource):
    @validate_schema(UserRegisterSchema)
    def post(self):
        user = UserManager.register_user(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class LoginUser(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        request_body = request.get_json()
        user = UserManager.login_user(request_body)
        token = AuthManager.encode_token(user)
        return {"token": token, "id": user.id, "role": "user"}, 200


class RegisterSeller(Resource):
    @validate_schema(UserRegisterSchema)
    def post(self):
        user = UserManager.register_seller(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token, "user_id": user.id}, 201


class LoginSeller(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        user = UserManager.login_seller(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token, "id": user.id, "role": "seller"}, 200
    

class Login(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        user = UserManager.login(request.get_json())
        role = user.role.value
        print(role)
        token = AuthManager.encode_token(user)
        return {"token": token, "id": user.id, "role": role}, 200
    

class LoginAdmin(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        user = UserManager.login_admin(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200


class UserInfo(Resource):
    @auth.login_required
    def get(self):
        current_user = auth.current_user()
        del current_user.password
        user_schema = UserResponseSchema()
        return user_schema.dump(current_user)


class Logout(Resource):
    @auth.login_required
    def get(self):
        return 200
