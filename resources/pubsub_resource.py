from flask import request
from flask_restful import Resource

class PostRequestHandler(Resource):
    def post(self):
        json_data = request.get_json()  # Getting JSON data from the request
        headers = request.headers  # Getting headers from the request
        print("Received JSON data:")
        print(json_data)
        print("Received Headers:")
        print(headers)
        return {'message': 'Received POST request'}, 200