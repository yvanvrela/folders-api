from flask import jsonify

def page_not_found(error):
    return jsonify({'message':'Not found page'}), 404
