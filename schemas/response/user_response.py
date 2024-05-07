from marshmallow import Schema, fields, validate

from schemas.bases import BaseUserSchema


class UserResponseSchema(BaseUserSchema):
    pass


class UserNamesSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    