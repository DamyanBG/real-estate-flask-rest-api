from flask_caching import Cache
from decouple import config

cache_config = {
    "CACHE_TYPE": config("CACHE_TYPE"),
    "CACHE_DEFAULT_TIMEOUT": config("CACHE_DEFAULT_TIMEOUT"),
    "CACHE_REDIS_HOST": config("CACHE_REDIS_HOST"),
    "CACHE_REDIS_PORT": config("CACHE_REDIS_PORT"),
    "CACHE_REDIS_DB": config("CACHE_REDIS_DB"),
    "CACHE_REDIS_PASSWORD": config("CACHE_REDIS_PASSWORD"),
}

cache = Cache(config=cache_config)
