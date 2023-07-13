from marshmallow import fields

from schemas.bases import BaseLandSchema


class LandRequestSchema(BaseLandSchema):
    photo = fields.String(required=True)
