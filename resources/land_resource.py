from flask import request
from flask_restful import Resource

from utils.decorators import validate_schema
from managers.land_manager import LandManager
from managers.user_manager import UserManager
from managers.visitations_manager import VisitationManager
from schemas.response.land_response import LandResponseSchema, LandDetailsResponseSchema
from schemas.response.visitation_response import VisitationResponseSchema
from schemas.request.land_request import LandRequestSchema


class LandResource(Resource):
    @validate_schema(LandRequestSchema)
    def post(self):
        req_body = request.get_json()
        land = LandManager.create_land(req_body)
        resp_schema = LandResponseSchema()
        return resp_schema.dump(land)
    

class LandsResource(Resource):
    def get(self):
        lands = LandManager.select_all_lands()
        resp_schema = LandResponseSchema()
        return resp_schema.dump(lands, many=True)
    

class LandDetalisResource(Resource):
    def get(self, land_id):
        land = LandManager.select_land_by_id(land_id)
        land.owner_names = UserManager.select_user_names(land.owner_id)
        visitations = VisitationManager.select_land_visitations(land.id)
        land_resp_schema = LandDetailsResponseSchema()
        land_resp_data = land_resp_schema.dump(land)
        visitations_resp_schema = VisitationResponseSchema()
        visitations_resp_data = visitations_resp_schema.dump(visitations, many=True)
        return {"land": land_resp_data, "visitations": visitations_resp_data}
