from models.chat_model import ChatModel

class ChatManager:
    @staticmethod
    def select_chat_history(current_user_id, chat_partner_id):
        current_user_messages = ChatModel.query.filter_by(sender_id=current_user_id, receiver_id=chat_partner_id).all()
        chat_partner_messages = ChatModel.query.filter_by(sender_id=chat_partner_id, receiver_id=current_user_id).all()
        return current_user_messages, chat_partner_messages
