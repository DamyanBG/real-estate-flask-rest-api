from db import db
from models.meeting_model import MeetingModel

from sqlalchemy.sql import text


class MeetingManager:
    @staticmethod
    def create_meeting(meeting_data):
        meeting = MeetingModel(**meeting_data)
        db.session.add(meeting)
        db.session.commit()
        return meeting

    @staticmethod
    def select_meetings_by_user(user_id):
        user_meetings = MeetingModel.query.filter(
            (MeetingModel.invitor_id == user_id) | (MeetingModel.invited_id == user_id)
        ).all()
        return user_meetings
    
    @staticmethod
    def select_user_homes_with_meetings(user_id):
        query = text("""
            SELECT
                h.id,
                h.title,
                (SELECT json_agg(
                    json_build_object(
                        'id', id,
                        'date', date,
                        'start_time', start_time,
                        'end_time', end_time
                    )
                ) 
                    FROM meetings
                    WHERE home_id = h.id) AS home_meetings
            FROM homes h
            JOIN meetings m
            ON h.id = m.home_id
            WHERE m.invitor_id = :user_id
            OR m.invited_id = :user_id
            GROUP BY h.id, h.title;
        """)
        conn = db.engine.connect()
        query_result = conn.execute(query, {"user_id": user_id})
        rows = query_result.all()
        result = [row._asdict() for row in rows]
        conn.close()
        return result
