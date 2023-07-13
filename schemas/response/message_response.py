from marshmallow import fields

from schemas.bases  import BaseMessageModel

class MessageResponseModel(BaseMessageModel):
    id = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
