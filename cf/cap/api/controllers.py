from flask import Blueprint, request, jsonify

from services import toService

apiController = Blueprint('apiController', __name__)


@apiController.route('/controller', methods=['GET'])
def controller():
    print(request.args)
    value = request.args.get('value', type=str)

    if value is None:
        return jsonify({'error': 'missing value: "value"}'}), 400

    return toService(value), 200, {}
