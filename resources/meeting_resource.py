from flask import request
from flask_restful import Resource

from managers.auth_manager import auth
from managers.meeting_manager import MeetingManager
from managers.user_manager import UserManager
from managers.home_manager import HomeManager
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
        for user_meeting in user_meetings:
            print(user_meeting.home_id)
            home_title = HomeManager.select_home_title(user_meeting.home_id)
            print(home_title)
            meeting_partner_id = user_meeting.invited_id if user_meeting.invited_id != current_user.id else user_meeting.invitor_id
            user_meeting.meeting_partner_names = UserManager.select_user_names(meeting_partner_id)
            user_meeting.home_title = home_title
        resp_schema = MeetingResponseSchema()
        return resp_schema.dump(user_meetings, many=True), 200
