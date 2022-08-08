from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from database.models.contribuyente_model import ContribuyenteModel
from database.schemas.contribuyente_schema import ContribuyenteSchema
from extensions.database_extension import db


contribuyente = Blueprint('api_contribuyente', __name__)
# Schema for one contribuyentes
contribuyente_schema = ContribuyenteSchema()
# Schema for all contribuyentes
contribuyentes_schema = ContribuyenteSchema(many=True)


@contribuyente.route('/', methods=['GET'])
def get_contribuyentes():

    all_contribuyentes = ContribuyenteModel.query.all()
    print(all_contribuyentes)
    result = contribuyentes_schema.dump(all_contribuyentes)
    return jsonify(result)


@contribuyente.route('/add', methods=['Post'])
def add_contribuyente():
    name = request.json['name']
    ruc = request.json['ruc']

    new_contribuyente = ContribuyenteModel(name, ruc)

    db.session.add(new_contribuyente)
    db.session.commit()

    return contribuyente_schema.jsonify(new_contribuyente)
