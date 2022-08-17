from flask import jsonify


def page_not_found(error):
    return jsonify({'errors': {'code': 404, 'message': 'Not found data'}}), 404


def bad_request(error):
    return jsonify({'errors': [{'code': error.code, 'message': error.description}], }), 400
