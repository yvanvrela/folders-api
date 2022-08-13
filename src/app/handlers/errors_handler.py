from flask import jsonify


def page_not_found(error):
    return jsonify({'error': 'Not found page'}), 404


def bad_request(error):
    return jsonify({'errors': [{'code': error.code, 'message': error.description}], }), 400
