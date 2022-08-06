from flask import Flask
from extensions import config_extension, routes_extension, handlers_extension


def create_app() -> Flask:
    app = Flask(__name__)

    config_extension.register_config(app)
    routes_extension.register_routes(app)
    handlers_extension.register_handlers(app)

    return app
