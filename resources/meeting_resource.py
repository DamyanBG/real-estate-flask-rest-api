from flask import request
from flask_restful import Resource

from managers.auth_manager import auth
from managers.meeting_manager import MeetingManager
from managers.user_manager import UserManager
from managers.home_manager import HomeManager
from schemas.request.meeting_request import MeetingRequestSchema
from schemas.response.meeting_response import MeetingResponseSchema, HomeWithMeetingsRespSchema
from utils.decorators import validate_schema


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
        # user_homes_with_meetings = MeetingManager.select_user_homes_with_meetings(current_user.id)
        # print(user_homes_with_meetings)
        mocked_resp = [{'id': 9, 'title': 'Amazing Place', 'home_meetings': [{'id': 2, 'date': '2024-06-04', 'start_time': '10:47:00', 'end_time': '12:47:00', 'meeting_partner_names': 'Tihomir  Zhelyazkov'}, {'id': 5, 'date': '2024-05-22', 'start_time': '14:00:00', 'end_time': '16:00:00', 'meeting_partner_names': 'Tihomir  Zhelyazkov'}]}, {'id': 10, 'title': 'Testov Dvor', 'home_meetings': [{'id': 3, 'date': '2024-05-21', 'start_time': '17:10:00', 'end_time': '20:10:00', 'meeting_partner_names': 'Tihomir  Zhelyazkov'}, {'id': 4, 'date': '2024-05-22', 'start_time': '10:00:00', 'end_time': '12:00:00', 'meeting_partner_names': 'Tihomir  Zhelyazkov'}]}]
        resp_schema = HomeWithMeetingsRespSchema()
        return resp_schema.dump(mocked_resp, many=True), 200
