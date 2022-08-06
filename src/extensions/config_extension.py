from flask import Flask
from config import configurations


def register_config(app: Flask) -> None:
    app.config.from_object(configurations['development'])
