from db import db
from models.meeting_model import MeetingModel

class MeetingManager:
    @staticmethod
    def create_meeting(meeting_data):
        meeting = MeetingModel(**meeting_data)
        db.session.add(meeting)
        db.session.commit()
        return meeting

    @staticmethod
    def select_meetings_by_user(user_id):
        user_meetings = MeetingModel.query.filter((MeetingModel.invitor_id == user_id) | (MeetingModel.invited_id == user_id)).all()
        return user_meetings
