from db import db


class HomeModel(db.Model):
    __tablename__ = "homes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    neighborhood = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    price = db.Column(db.String(255), nullable=False)
    bathrooms = db.Column(db.String(255))
    garages = db.Column(db.String(255))
    bedrooms = db.Column(db.String(255))
    area = db.Column(db.String(255))
    year = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    longitude = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    owner = db.relationship("UserModel")
    home_views = db.Column(db.String(255), default="0")
