from models.chat_model import ChatModel
from db import db

class ChatManager:
    @staticmethod
    def select_chat_history(current_user_id, chat_partner_id):
        current_user_messages = ChatModel.query.filter_by(sender_id=current_user_id, receiver_id=chat_partner_id).all()
        chat_partner_messages = ChatModel.query.filter_by(sender_id=chat_partner_id, receiver_id=current_user_id).all()
        return current_user_messages, chat_partner_messages

    @staticmethod
    def create_message(text, current_user_id, chat_partner_id):
        chat_message = ChatModel(text=text, sender_id=current_user_id, receiver_id=chat_partner_id)
        db.session.add(chat_message)
        db.session.commit()
        return chat_message
