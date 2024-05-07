from flask_restful import Resource

from managers.chat_manager import ChatManager
from managers.user_manager import UserManager
from managers.auth_manager import auth
from schemas.response.message_response import ChatHistoryResponseSchema


class ChatHistory(Resource):
    @auth.login_required
    def get(self, chat_partner_id):
        current_user = auth.current_user()
        chat_partner_names = UserManager.select_user_names_as_dict(chat_partner_id)
        print(chat_partner_names)
        current_user_messages, chat_partner_messages = ChatManager.select_chat_history(current_user.id, chat_partner_id)
        resp_schema = ChatHistoryResponseSchema()
        response_data = {
            "current_user_messages": current_user_messages,
            "chat_partner_messages": chat_partner_messages,
            "chat_partner_names": chat_partner_names,
        }
        resp = resp_schema.dump(response_data)
        print(resp)
        return resp
    