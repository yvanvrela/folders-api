from flask import Flask
from app.routes.folders_route import folder
from app.routes.contribuyentes_route import contribuyente


def register_routes(app: Flask) -> None:
    app.register_blueprint(folder, url_prefix='/api/folders')
    app.register_blueprint(contribuyente, url_prefix='/api/contribuyentes')
