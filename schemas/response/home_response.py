from marshmallow import fields, Schema

from schemas.bases import BaseHomeSchema


class HomeDetailsResponseSchema(BaseHomeSchema):
    photo_url = fields.String(required=True)
    id = fields.Integer(required=True)
    owner_names = fields.String(required=True)
    home_views = fields.String(required=True)


class LocationSchema(fields.Dict):
    lat = fields.Float(required=True)
    lon = fields.Float(required=True)


class PinSchema(Schema):
    location = LocationSchema()


class HomeResponseSchema(BaseHomeSchema):
    photo_url = fields.String(required=True)
    id = fields.Integer(required=True)
    location = LocationSchema()
