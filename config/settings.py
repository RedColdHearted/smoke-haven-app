from .common import *

from dotenv import dotenv_values

config = dotenv_values(".env")

SECRET_KEY = config.get("DJANGO_SECRET")

DEBUG = bool(config.get("DEBUG"))

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]