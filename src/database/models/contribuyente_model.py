from extensions.database_extension import db


class ContribuyenteModel(db.Model):
    __tablename__ = 'contribuyentes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ruc = db.Column(db.String(100), unique=True)

    def __init__(self, name, ruc) -> None:
        self.name = name
        self.ruc = ruc
