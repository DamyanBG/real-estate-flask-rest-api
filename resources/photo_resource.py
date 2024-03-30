from flask_restful import Resource
from flask import request

from utils.decorators import validate_schema
from managers.photo_manager import TempPhotoManager
from schemas.request.photo_request import PhotoRequestSchema
from schemas.response.photo_response import PhotoResponse


class TempPhotoResource(Resource):
    @validate_schema(PhotoRequestSchema)
    def post(self):
        photo_data = request.get_json()
        photo = TempPhotoManager.create_photo(photo_data)
        photo_schema = PhotoResponse()
        respone = photo_schema.dump(photo), 201
        return respone
    