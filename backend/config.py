# define your config here
import os

from starlette.datastructures import Secret

DEBUG = os.getenv("DEBUG", True)

DATABASE_URL = os.getenv("DATABASE_URL", None)
MAX_CONNECTIONS_COUNT = 10
MIN_CONNECTIONS_COUNT = 4

ALLOWED_HOSTS = [
    "*",
]

SECRET_KEY = Secret(os.getenv("SECRET_KEY", "application-secret"))



