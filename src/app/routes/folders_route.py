from flask import Blueprint, jsonify

folder = Blueprint('api_folder', __name__)

@folder.route('/', methods=['GET'])
def get_folders():
    try:
        return jsonify({'message':'All folders'})
    except:
        return jsonify({'message':'Error folders'})