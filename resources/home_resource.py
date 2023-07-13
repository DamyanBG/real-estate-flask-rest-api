from flask import request
from flask_restful import Resource

from managers.home_manager import HomeManager
from schemas.request.home_request import HomeRequestSchema
from schemas.response.home_response import HomeResponseSchema

class CreateHomeResource(Resource):
    def post(self):
        req_body = request.get_json()
        home = HomeManager.add_home(req_body)
        resp_schema = HomeResponseSchema()
        return resp_schema.dump(home)
    

class GetHomeResource(Resource):
    def get(self, home_id):
        home = HomeManager.select_home_by_id(home_id)
        resp_schema = HomeResponseSchema()
        return resp_schema.dump(home)