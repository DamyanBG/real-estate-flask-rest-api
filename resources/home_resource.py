from flask import request
from flask_restful import Resource
from redis_singleton import cache

from managers.home_manager import HomeManager
from managers.user_manager import UserManager
from managers.visitations_manager import VisitationManager
from schemas.response.visitation_response import VisitationResponseSchema
from schemas.request.home_request import HomeRequestSchema, HomeUpdateRequestSchema
from schemas.response.home_response import HomeResponseSchema, HomeDetailsResponseSchema
from utils.decorators import validate_schema


class HomeResource(Resource):
    @validate_schema(HomeRequestSchema)
    def post(self):
        req_body = request.get_json()
        home = HomeManager.add_home(req_body)
        resp_schema = HomeResponseSchema()
        return resp_schema.dump(home)

    @validate_schema(HomeUpdateRequestSchema)
    def put(self):
        req_body = request.get_json()
        home = HomeManager.update_home_by_id(req_body)
        resp_schema = HomeResponseSchema()
        return resp_schema.dump(home)
        
    

class GetHomeResource(Resource):
    def get(self, home_id):
        home = HomeManager.select_home_by_id(home_id)
        resp_schema = HomeResponseSchema()
        return resp_schema.dump(home)
    

class HomesResource(Resource):
    @cache.cached(timeout=50)
    def get(self):
        homes = HomeManager.select_all_homes()
        resp_schema = HomeResponseSchema()
        return resp_schema.dump(homes, many=True)
    

class HomesPaginatedResource(Resource):
    def get(self, page, rows_per_page):
        homes = HomeManager.select_paginated_homes(page, rows_per_page)
        resp_schema = HomeResponseSchema()
        return resp_schema.dump(homes, many=True)
    
    
class HomesPaginatedCachedResource(Resource):
    @cache.cached(timeout=50)
    def get(self, page, rows_per_page):
        homes = HomeManager.select_paginated_homes(page, rows_per_page)
        resp_schema = HomeResponseSchema()
        return resp_schema.dump(homes, many=True)
    

class HomeDetailsResource(Resource):
    def get(self, home_id):
        home_details = HomeManager.select_home_details(home_id)
        home_owner_names = UserManager.select_user_names(home_details.owner_id)
        home_details.owner_names = home_owner_names
        home_visitations = VisitationManager.select_home_visitations(home_details.id)
        home_details_resp_schema = HomeDetailsResponseSchema()
        home_details = home_details_resp_schema.dump(home_details)
        visitations_resp_schema = VisitationResponseSchema()
        visitations = visitations_resp_schema.dump(home_visitations, many=True)
        return {"home_details": home_details, "visitations": visitations}
