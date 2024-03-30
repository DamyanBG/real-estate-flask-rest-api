from db import db


class LandModel(db.Model):
    __tablename__ = "lands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    place = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    size = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    longitude = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    owner = db.relationship("UserModel")
    photo_url = db.Column(db.String(255))
    land_views = db.Column(db.String(255), default="0")
