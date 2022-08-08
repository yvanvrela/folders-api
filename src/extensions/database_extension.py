from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def register_database_config(app: Flask):
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from database.models.contribuyente_model import ContribuyenteModel
        from database.models.folder_model import FolderModel
        db.create_all()
        db.session.commit()
