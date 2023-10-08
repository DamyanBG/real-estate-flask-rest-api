from config import create_app
from db import db
from flask import request


app, socketio = create_app()
app.config["INITIALIZED"] = False 

db.init_app(app)

@socketio.on('user_id')
def user_id(data):
    print(f"User {data} have been connected")
    print(request.sid)


@app.before_request
def init_request():
    if not app.config["INITIALIZED"]:
        db.create_all()
        app.config['INITIALIZED'] = True


if __name__ == "__main__":
    socketio.run(app)
