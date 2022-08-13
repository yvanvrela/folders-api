from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def register_database_config(app: Flask):
    db.init_app(app)
    ma.init_app(app)
    from database.models.contribuyente_model import ContribuyenteModel
    from database.models.folder_model import FolderModel
    migrate.init_app(app, db, directory='src/database/migrations')
