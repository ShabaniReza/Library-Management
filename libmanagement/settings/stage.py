from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'librarymanagement',
        'HOST': 'mysql',
        'USER': 'root',
        'PASSWORD': 'set password',
        'PORT': '3306'
    }
}

CELERY_BROKER_URL = 'redis://redis:6379/1'


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}