from flask import Blueprint, jsonify, request, abort
from database.models.contribuyente_model import ContribuyenteModel
from database.models.folder_model import FolderModel
from database.schemas.folder_schema import FolderShema, ValidationError
from extensions.database_extension import db


folder = Blueprint('api_folder', __name__)

folder_schema = FolderShema()
folders_schema = FolderShema(many=True)


@folder.route('/', methods=['GET'])
def get_folders():
    try:
        all_folders = FolderModel.query.all()

        result = folders_schema.dump(all_folders)

        return jsonify({'folders': result}), 200
    except:
        return jsonify({'message': 'Error'}), 500


@folder.route('/<id>', methods=['GET'])
def get_folder(id):
    folder = FolderModel.query.filter_by(id=id).first()
    if not folder:
        return jsonify({'message': 'Folder does not exist'}), 400

    return folder_schema.jsonify(folder), 200


@folder.route('/', methods=['POST'])
def add_folder():
    try:
        json_data = request.get_json()
        if not json_data:
            return jsonify({'message': 'Not input data provided'}), 400

        try:
            data = folder_schema.load(json_data)
        except ValidationError as err:
            return jsonify(err.messages), 422

        # Verify contribuyente id
        contribuyente = ContribuyenteModel.query.filter_by(
            id=data['contribuyente_id']).first()
        if not contribuyente:
            return jsonify({'message': 'Contribuyente does not exist'}), 400

        new_folder = FolderModel(
            data['contribuyente_id'], data['color'], data['time'])

        db.session.add(new_folder)
        db.session.commit()

        response = {
            'message': 'Folder registered successfully',
            'folder': folder_schema.dump(new_folder),
        }

        return jsonify(response), 201
    except:
        return jsonify({'message': 'Error'}), 500


@folder.route('/<id>', methods=['PUT'])
def update_folder(id):

    json_data = request.get_json()

    if not json_data:
        return jsonify({'message': 'Not input data provided'}), 400

    # Validate and deserialize input
    try:
        data = folder_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422

    folder = FolderModel.query.filter_by(id=id).first()
    if not folder:
        return jsonify({'message': 'Folder does not exist'}), 400

    contribuyente = ContribuyenteModel.query.filter_by(
        id=data['contribuyente_id']).first()
    if not contribuyente:
        return jsonify({'message': 'Contribuyente does not exist'}), 400

    folder.contribuyente_id = data['contribuyente_id']
    folder.color = data['color']
    folder.time = data['time']

    db.session.commit()

    response = {
        'message': 'Folder updated successfully',
        'folder': folder_schema.dump(folder),
    }
    return jsonify(response), 200


@folder.route('/<id>', methods=['DELETE'])
def delete_folder(id):

    folder = FolderModel.query.filter_by(id=id).first()
    if not folder:
        abort(404)

    db.session.delete(folder)
    db.session.commit()

    response = {
        'message': 'Folder deleted successfully',
        'folder': folder_schema.dump(folder)
    }
    return jsonify(response), 200
