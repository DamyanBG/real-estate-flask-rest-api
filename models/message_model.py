from db import db


class MessageModel(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    sender = db.relationship("UserModel")
    receiver_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    receiver = db.relationship("UserModel")
    text = db.Column(db.String(255), nullable=False)
