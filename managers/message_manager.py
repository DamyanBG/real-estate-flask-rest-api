from models.message_model import MessageModel
from managers.user_manager import UserManager
from db import db

class MessageManager:
    @staticmethod
    def create_message(message_data):
        message = MessageModel(**message_data)
        db.session.add(message)
        db.session.commit()
        return message
    
    @staticmethod
    def select_message_history(user_id, interlocutor_id):
        sent_messages = MessageModel.query.filter_by(sender_id=user_id, receiver_id=interlocutor_id).all()
        received_messages = MessageModel.query.filter_by(sender_id=interlocutor_id, receiver_id=user_id).all()
        print(sent_messages)
        print(received_messages)
        return sent_messages, received_messages
    

    @staticmethod
    def select_chat_interlocutors(user_id):
        receivers_query_result = MessageModel.query.with_entities(MessageModel.receiver_id).filter_by(sender_id=user_id).all()
        receivers_ids = [result[0] for result in receivers_query_result]
        print(receivers_ids)
        senders_query_result = MessageModel.query.with_entities(MessageModel.sender_id).filter_by(receiver_id=user_id).all()
        senders_ids = [result[0] for result in senders_query_result]
        interlocutors_ids = set(receivers_ids + senders_ids)
        interlocutors = [
            {
                "id": interlocutor_id,
                "names": UserManager.select_user_names(interlocutor_id)
            }
            for interlocutor_id in interlocutors_ids
        ]
        return interlocutors
