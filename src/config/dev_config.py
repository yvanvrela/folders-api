from os import getenv

from .base_config import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
