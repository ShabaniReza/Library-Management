from .common import *


DEBUG = False

ALLOWED_HOSTS = ['reza27.pythonanywhere.com']

REDIS_URL = os.getenv('REDIS_URL')

CELERY_BROKER_URL = REDIS_URL

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