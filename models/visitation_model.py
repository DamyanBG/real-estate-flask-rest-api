from sqlalchemy import func

from db import db


class VisitationModel(db.Model):
    __tablename__ = "visitations"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    date = db.Column(db.Date, nullable=False)
    start_hour = db.Column(db.DateTime, nullable=False)
    end_hour = db.Column(db.DateTime, nullable=False)
    organizator_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    organizator = db.relationship("UserModel")
    home_id = db.Column(db.Integer, db.ForeignKey("homes.id"))
    home = db.relationship("HomeModel")
    land_id = db.Column(db.Integer, db.ForeignKey("lands.id"))
    land = db.relationship("LandModel")
    address = db.Column(db.String(255), nullable=False)
