from flask import request
from flask_socketio import send, emit

from config import create_app
from db import db
from search import es


app, socketio = create_app()
app.config["INITIALIZED"] = False

db.init_app(app)

@socketio.on('user_id')
def user_id(data):
    print(f"User {data} have been connected")
    print(request.sid)


@socketio.on('sync_message')
def message(data):
    print(data)
    emit("sync_message", data, broadcast=True)


@app.before_request
def init_request():
    if not app.config["INITIALIZED"]:
        db.create_all()
        try:
            es.reindex_homes()
        except Exception as e:
            print(e)
        app.config["INITIALIZED"] = True


if __name__ == "__main__":
    app.run()
