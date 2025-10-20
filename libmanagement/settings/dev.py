from .common import *
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured
import dj_database_url

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

if not SECRET_KEY:
    raise ImproperlyConfigured("The SECRET_KEY environment variable is not set. Please set it in your .env file or environment.")


DEBUG = True


DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}