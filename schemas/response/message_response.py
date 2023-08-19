from marshmallow import Schema, fields, validate

from schemas.bases import BaseMessageModel


class MessageResponseSchema(BaseMessageModel):
    id = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)


class InterlocutorResponseSchema(Schema):
    id = fields.Integer(required=True)
    names = fields.String(required=True)
