from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from redis_singleton import cache

from db import db
from resources.routes import routes


DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_NAME = config('DB_NAME')

VAR_TO_PRINT = config("TEST", default="default_test")


class DevApplicationConfiguration:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}/{DB_NAME}"
    )


# class TestApplicationConfiguration:
#     DEBUG = True
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = (
#         f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
#         f"@localhost:{config('DB_PORT')}/{config('TEST_DB_NAME')}"
#     )


def create_app(config="config.DevApplicationConfiguration"):
    app = Flask(__name__)
    app.config.from_object(DevApplicationConfiguration)
    migrate = Migrate(app, db)
    cache.init_app(app)
    print("starting")
    print(VAR_TO_PRINT)
    CORS(app)
    api = Api(app)
    [api.add_resource(*r) for r in routes]
    return app
