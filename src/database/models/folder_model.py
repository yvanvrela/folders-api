from extensions.database_extension import db


class FolderModel(db.Model):
    __tablename__ = 'folders'
    id = db.Column(db.Integer, primary_key=True)
    contribuyente_id = db.Column(db.Integer, db.ForeignKey('contribuyentes.id'))
    color = db.Column(db.String(50))
    time = db.Column(db.String(50))

    def __init__(self, contribuyente_id, color, time) -> None:
        self.contribuyente_id = contribuyente_id
        self.color = color
        self.time = time
