from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_caching import Cache

from db import db
from resources.routes import routes


class DevApplicationConfiguration:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@{config('DB_HOST')}/{config('DB_NAME')}"
    )
    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 300
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0

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
    cache = Cache(app)
    CORS(app)
    api = Api(app)
    [api.add_resource(*r) for r in routes]
    return app
