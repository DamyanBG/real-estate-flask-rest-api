from marshmallow import fields, Schema
from marshmallow import Schema, fields, validate

from schemas.bases import BaseMessageSchema
from schemas.response.user_response import UserNamesSchema


class MessageResponseSchema(BaseMessageSchema):
    id = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)


class ChatHistoryResponseSchema(Schema):
    current_user_messages = fields.Nested(MessageResponseSchema, many=True)
    chat_partner_messages = fields.Nested(MessageResponseSchema, many=True)
    chat_partner_names = fields.Nested(UserNamesSchema)
