from db import db


class HomeFavorites(db.Model):
    __tablename__ = "home_favorites"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    owner = db.relationship("UserModel")
    home_id = db.Column(db.Integer, db.ForeignKey("homes.id"))
    home = db.relationship("HomeModel")
