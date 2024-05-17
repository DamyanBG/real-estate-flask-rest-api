from marshmallow import fields, Schema

from schemas.bases import BaseMeetingSchema


class MeetingResponseSchema(BaseMeetingSchema):
    id = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
    meeting_partner_names = fields.String()
    home_title = fields.String()


class HomeWithMeetingsRespSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    home_meetings = fields.Nested(MeetingResponseSchema, many=True)
