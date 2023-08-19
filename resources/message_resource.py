from flask import request
from flask_restful import Resource

from managers.auth_manager import auth
from managers.message_manager import MessageManager
from utils.decorators import validate_schema
from schemas.request.message_request import MessageRequestSchema 
from schemas.response.message_response import MessageResponseSchema, InterlocutorResponseSchema


class MessageResource(Resource):
    @auth.login_required
    @validate_schema(MessageRequestSchema)
    def post(self):
        req_body = request.get_json()
        message = MessageManager.create_message(req_body)
        resp_schema = MessageResponseSchema()
        return resp_schema.dump(message), 201


class ChatHistoryResource(Resource):
    @auth.login_required
    def get(self, interlocutor_id):
        print(interlocutor_id)
        current_user = auth.current_user()
        sent_messages, received_messages = MessageManager.select_message_history(current_user.id, interlocutor_id)
        resp_schema = MessageResponseSchema()
        return {
            "sent_messages": resp_schema.dump(sent_messages, many=True),
            "received_messages": resp_schema.dump(received_messages, many=True),
        }, 200


class ChatInterlocutorsResource(Resource):
    @auth.login_required
    def get(self):
        current_user = auth.current_user()
        chat_interlocutors = MessageManager.select_chat_interlocutors(current_user.id)
        resp_schema = InterlocutorResponseSchema()
        print(chat_interlocutors)
        return resp_schema.dump(chat_interlocutors, many=True), 200
