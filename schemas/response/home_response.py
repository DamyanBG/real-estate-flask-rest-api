from marshmallow import fields

from schemas.bases import BaseHomeSchema


class HomeResponseSchema(BaseHomeSchema):
    photo_url = fields.String(required=True)
    id = fields.Integer(required=True)
