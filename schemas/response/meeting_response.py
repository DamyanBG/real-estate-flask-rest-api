from marshmallow import fields, Schema



class BaseMeetingResp(Schema):
    date = fields.String(required=True)
    start_time = fields.String(required=True)
    end_time = fields.String(required=True)
    # invitor_id = fields.Integer(required=True)
    # invited_id = fields.Integer(required=True)
    # status = fields.Enum(MeetingStatusType)
    home_id = fields.Integer(allow_none=True)
    # land_id = fields.Integer(allow_none=True)


class MeetingResponseSchema(BaseMeetingResp):
    id = fields.Integer(required=True)
    meeting_partner_names = fields.String()


class HomeWithMeetingsRespSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    home_meetings = fields.Nested(MeetingResponseSchema, many=True)
