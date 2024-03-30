from marshmallow import fields


from schemas.bases import BaseLandSchema


class LandResponseSchema(BaseLandSchema):
    photo_url = fields.String(required=True)
    id = fields.Integer(required=True)

class LandDetailsResponseSchema(BaseLandSchema):
    photo_url = fields.String(required=True)
    id = fields.Integer(required=True)
    owner_names = fields.String(required=True)
    land_views = fields.String(required=True)
