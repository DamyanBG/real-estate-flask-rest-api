from marshmallow import fields


from schemas.bases import BaseLandSchema


class LandResponseSchema(BaseLandSchema):
    photo_url = fields.String(required=True)
    id = fields.Integer(required=True)
