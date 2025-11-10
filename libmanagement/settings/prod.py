from dotenv import load_dotenv
import os
from .common import *

load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ['reza27.pythonanywhere.com']

REDIS_URL = os.getenv('REDIS_URL')

CELERY_BROKER_URL = REDIS_URL

REDIS_OPTIONS = {}
if REDIS_URL and REDIS_URL.startswith('rediss://'):
    REDIS_OPTIONS = {
        "SSL_CERT_REQS": None, 
        "SSL_CERTFILE": None, 
    }

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"ssl_cert_reqs": None},
        }
    }
}