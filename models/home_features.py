from db import db


class HomeFeaturesModel(db.Model):
    __tablename__ = "home_features"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    home_id = db.Column(db.Integer, db.ForeignKey("homes.id"))
    home = db.relationship("HomeModel")
