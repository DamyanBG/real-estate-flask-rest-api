from marshmallow import fields

from schemas.bases import BaseHomeSchema


class HomeRequestSchema(BaseHomeSchema):
    photo = fields.String(required=True)
