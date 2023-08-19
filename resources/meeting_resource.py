from flask import request
from flask_restful import Resource

from managers.auth_manager import auth
from managers.meeting_manager import MeetingManager
from utils.decorators import validate_schema
from schemas.request.meeting_request import MeetingRequestSchema
from schemas.response.meeting_response import MeetingResponseSchema

class MeetingResource(Resource):
    @auth.login_required
    @validate_schema(MeetingRequestSchema)
    def post(self):
        req_body = request.get_json()
        meeting = MeetingManager.create_meeting(req_body)
        resp_schema = MeetingResponseSchema()
        return resp_schema.dump(meeting), 201
    
    @auth.login_required
    def get(self):
        current_user = auth.current_user()
        user_meetings = MeetingManager.select_meetings_by_user(current_user.id)
        resp_schema = MeetingResponseSchema()
        return resp_schema.dump(user_meetings, many=True), 200
