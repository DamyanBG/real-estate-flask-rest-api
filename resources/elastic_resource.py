from flask import request
from flask_restful import Resource

class ElasticResource(Resource):
    def get(self, home_id):
        print(home_id)
        return "OK"