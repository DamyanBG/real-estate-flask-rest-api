from marshmallow import fields

from schemas.bases import BaseVisitationModel


class VisitationResponseSchema(BaseVisitationModel):
    id = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
