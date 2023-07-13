from marshmallow import Schema, fields, validate

from models.enums import MeetingStatusType


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))


class BaseHomeSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=2, max=255))
    city = fields.String(required=True, validate=validate.Length(min=2, max=255))
    neighborhood = fields.String(
        required=True, validate=validate.Length(min=2, max=255)
    )
    price = fields.String(required=True, validate=validate.Length(min=2, max=255))
    size = fields.String(required=True, validate=validate.Length(min=2, max=255))
    year = fields.String(required=True, validate=validate.Length(min=2, max=255))
    description = fields.String(required=True, validate=validate.Length(min=2, max=255))
    address = fields.String(validate=validate.Length(min=2, max=255))
    longitude = fields.String(validate=validate.Length(min=2, max=255))
    latitude = fields.String(validate=validate.Length(min=2, max=255))
    owner_id = fields.Integer(required=True, allow_none=False)


class BaseLandSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    place = fields.String(required=True, validate=validate.Length(min=2, max=255))
    price = fields.String(required=True, validate=validate.Length(min=2, max=255))
    size = fields.String(required=True, validate=validate.Length(min=2, max=255))
    description = fields.String(required=True, validate=validate.Length(min=2, max=255))
    longitude = fields.String(validate=validate.Length(min=2, max=255))
    latitude = fields.String(validate=validate.Length(min=2, max=255))
    owner_id = fields.Integer(required=True)


class BaseMeetingSchema(Schema):
    date = fields.Date(required=True)
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)
    invitor_id = fields.Integer(required=True)
    invited_id = fields.Integer(required=True)
    status = fields.Enum(MeetingStatusType)


class BaseMessageModel(Schema):
    sender_id = fields.Integer(required=True)
    receiver_id = fields.Integer(required=True)
    text = fields.String(required=True, validate=validate.Length(min=1, max=255))


class BaseVisitationModel(Schema):
    date = fields.Date(required=True)
    start_hour = fields.DateTime(required=True)
    end_hour = fields.DateTime(required=True)
    organizator_id = fields.Integer(required=True)
    address = fields.String(required=True, validate=validate.Length(min=2, max=255))
    home_id = fields.Integer()
    land_id = fields.Integer()
