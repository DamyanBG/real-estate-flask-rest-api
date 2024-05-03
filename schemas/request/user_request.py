from marshmallow import fields, validate

from schemas.bases import BaseUserSchema


class UserRegisterSchema(BaseUserSchema):
    phone_number = fields.String(
        required=True, validate=validate.Length(min=6, max=255)
    )
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))


class UserLoginSchema(BaseUserSchema):
    pass
