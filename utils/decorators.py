from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth_manager import auth


def validate_schema(schema_name):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            data = request.get_json()
            schema = schema_name()
            errors = schema.validate(data)
            if errors:
                raise BadRequest("You are not sending validate data")
            return func(*args, **kwargs)

        return decorated_func

    return wrapper


def permission_required(permission):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            user = auth.current_user()
            if not user.role == permission:
                raise Forbidden("You do not have access to this resource")
            return func(*args, **kwargs)

        return decorated_func

    return wrapper
