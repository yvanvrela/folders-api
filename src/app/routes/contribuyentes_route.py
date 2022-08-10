from flask import Blueprint, jsonify, request
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
    try:
        all_contribuyentes = ContribuyenteModel.query.all()

        result = contribuyentes_schema.dump(all_contribuyentes)
        
        return jsonify({'contribuyentes':result}), 200
    except:
        return jsonify({'message': 'Not data'}), 500


@contribuyente.route('/add', methods=['Post'])
def add_contribuyente():
    name = request.json['name']
    ruc = request.json['ruc']

    new_contribuyente = ContribuyenteModel(name, ruc)

    db.session.add(new_contribuyente)
    db.session.commit()

    response = {
        'message':'Contribuyente registered successfully',
        'contribuyente':contribuyente_schema.dump(new_contribuyente)
    }

    return jsonify(response), 201
