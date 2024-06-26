from sqlalchemy import func

from db import db


from models.enums import MeetingStatusType


class MeetingModel(db.Model):
    __tablename__ = "meetings"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    invitor_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    invitor = db.relationship("UserModel", foreign_keys=[invitor_id])
    invited_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    invited = db.relationship("UserModel", foreign_keys=[invited_id])
    status = db.Column(db.Enum(MeetingStatusType), nullable=False, default=MeetingStatusType.pending)
    home_id = db.Column(db.Integer, db.ForeignKey("homes.id"))
    home = db.relationship("HomeModel")
    land_id = db.Column(db.Integer, db.ForeignKey("lands.id"))
    land = db.relationship("LandModel")
