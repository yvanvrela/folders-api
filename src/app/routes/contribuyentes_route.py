from flask import Blueprint, jsonify, request, abort
from database.models.contribuyente_model import ContribuyenteModel
from database.schemas.contribuyente_schema import ContribuyenteSchema, ValidationError
from extensions.database_extension import db


contribuyente = Blueprint('api_contribuyente', __name__)
# Schema for one contribuyentes
contribuyente_schema = ContribuyenteSchema()
# Schema for all contribuyentes
contribuyentes_schema = ContribuyenteSchema(many=True)


@contribuyente.route('/', methods=['GET'])
def get_contribuyentes():

    all_contribuyentes = ContribuyenteModel.query.all()
    if not all_contribuyentes:
        abort(404)

    result = contribuyentes_schema.dump(all_contribuyentes)

    return jsonify({'contribuyentes': result}), 200


@contribuyente.route('/<id>', methods=['GET'])
def get_contribuyente(id):

    contribuyente = ContribuyenteModel.query.get(id)
    if not contribuyente:
        abort(400, description='Contribuyente does not exist')

    return jsonify({'contribuyente': contribuyente_schema.dump(contribuyente)}), 200


@contribuyente.route('/', methods=['POST'])
def add_contribuyente():
    json_data = request.get_json()
    if not json_data:
        abort(400, description='Not input data provided')

    try:
        data = contribuyente_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    find_contribuyente = ContribuyenteModel.query.filter_by(
        ruc=data['ruc']).first()
    if find_contribuyente:
        abort(400, description='Contribuyente already exists')

    new_contribuyente = ContribuyenteModel(data['name'], data['ruc'])
    db.session.add(new_contribuyente)
    db.session.commit()

    response = {
        'message': 'Contribuyente registered successfully',
        'contribuyente': contribuyente_schema.dump(new_contribuyente),
    }

    return jsonify(response), 201


@contribuyente.route('/<id>', methods=['PUT'])
def update_contribuyente(id):
    json_data = request.get_json()
    if not json_data:
        abort(400, description='Not data provided')

    # Validate Schema and deserialize input
    try:
        data = contribuyente_schema.load(json_data)
    except ValidationError as err:
        return jsonify({'errors': err.messages_dict}), 422

    contribuyente = ContribuyenteModel.query.filter_by(
        id=id).first()
    if not contribuyente:
        abort(400, description='Contribuyente does not exist')

    contribuyente.name = data['name']
    contribuyente.ruc = data['ruc']

    db.session.commit()

    response = {
        'message': 'Contribuyente updated successfully',
        'contribuyente': contribuyente_schema.dump(contribuyente)
    }
    return jsonify(response), 200


@contribuyente.route('/<id>', methods=['DELETE'])
def delete_contribuyente(id):
    contribuyente = ContribuyenteModel.query.filter_by(id=id).first()
    if not contribuyente:
        abort(404)

    db.session.delete(contribuyente)
    db.session.commit()

    response = {
        'message': 'Contribuyented deleted successfully',
        'contribuyente': contribuyente_schema.dump(contribuyente),
    }
    return jsonify(response)
