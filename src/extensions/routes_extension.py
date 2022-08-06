from flask import Flask
from app.routes.folders_route import folder


def register_routes(app: Flask) -> None:
    app.register_blueprint(folder, url_prefix='/api/folders')
