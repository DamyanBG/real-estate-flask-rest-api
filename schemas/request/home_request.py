from marshmallow import fields

from schemas.bases import BaseHomeSchema


class HomeRequestSchema(BaseHomeSchema):
    photo = fields.String()
    photo_id = fields.String()


class HomeUpdateRequestSchema(BaseHomeSchema):
    id = fields.Integer(required=True)
    photo = fields.String()
