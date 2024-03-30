from db import db


class TempPhotoModel(db.Model):
    __tablename__ = "temp_photos"

    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(255))
