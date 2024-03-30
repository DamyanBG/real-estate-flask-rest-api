from marshmallow import fields

from schemas.bases import BaseHomeSchema


class HomeResponseSchema(BaseHomeSchema):
    photo_url = fields.String(required=True)
    id = fields.Integer(required=True)

class HomeDetailsResponseSchema(BaseHomeSchema):
    photo_url = fields.String(required=True)
    id = fields.Integer(required=True)
    owner_names = fields.String(required=True)
    home_views = fields.String(required=True)
