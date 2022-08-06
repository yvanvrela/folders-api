from os import getenv


class BaseConfig:
    SECRET_KEY = getenv('SECRET_KEY')

