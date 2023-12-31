from marshmallow import fields

from schemas.bases import BaseMeetingSchema


class MeetingResponseSchema(BaseMeetingSchema):
    id = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
