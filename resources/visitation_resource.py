from flask import request
from flask_restful import Resource


from utils.decorators import validate_schema
from managers.visitations_manager import VisitationManager
from schemas.response.visitation_response import VisitationResponseSchema
from schemas.request.visitation_request import VisitationRequestSchema


class VisitationResource(Resource):
    @validate_schema(VisitationRequestSchema)
    def post(self):
        req_body = request.get_json()
        visitation = VisitationManager.create_visitation(req_body)
        resp_schema = VisitationResponseSchema()
        return resp_schema.dump(visitation), 201
