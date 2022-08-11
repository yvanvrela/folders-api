from flask import Blueprint, jsonify, request
from database.models.folder_model import FolderModel
from database.schemas.folder_schema import FolderShema
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
    try:
        folder = FolderModel.query.get(id)
        return folder_schema.jsonify(folder), 200
    except:
        return jsonify({'message': 'Error'}), 500


@folder.route('/', methods=['POST'])
def add_folder():
    try:
        data = request.get_json()

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
    try:
        folder_reference = FolderModel.query.get(id)
        data = request.get_json()

        # TODO: Update

        contribuyente_id = data['contrinuyente_id']
        color = data['color']
        time = data['time']

        folder_reference.contribuyente_id = contribuyente_id
        folder_reference.color = color
        folder_reference.time = time

        db.session.commit()

        response = {
            'message': 'Folder updated successfully',
            'folder': folder_schema.dump(folder),
        }
        return jsonify(response), 200
    except:
        return jsonify({'message': 'Error'}), 500
