from marshmallow import Schema, fields

class PhotoRequestSchema(Schema):
    photo_base64 = fields.String(required=True)