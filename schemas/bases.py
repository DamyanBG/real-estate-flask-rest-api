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
    area = fields.String(required=True, validate=validate.Length(min=2, max=255))
    bathrooms = fields.String(required=True, validate=validate.Length(max=255))
    garages = fields.String(required=True, validate=validate.Length(max=255))
    bedrooms = fields.String(required=True, validate=validate.Length(max=255))
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
    start_time = fields.Time(required=True)
    end_time = fields.Time(required=True)
    invitor_id = fields.Integer(required=True)
    invited_id = fields.Integer(required=True)
    status = fields.Enum(MeetingStatusType)
    home_id = fields.Integer(allow_none=True)
    land_id = fields.Integer(allow_none=True)


class BaseMessageSchema(Schema):
    sender_id = fields.Integer(required=True)
    receiver_id = fields.Integer(required=True)
    text = fields.String(required=True, validate=validate.Length(min=1, max=255))


class BaseVisitationModel(Schema):
    date = fields.Date(required=True)
    start_hour = fields.Time(required=True)
    end_hour = fields.Time(required=True)
    organizator_id = fields.Integer(required=True)
    address = fields.String(required=True, validate=validate.Length(min=2, max=255))
    home_id = fields.Integer(allow_none=True)
    land_id = fields.Integer(allow_none=True)
