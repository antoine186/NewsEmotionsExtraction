from flask import Blueprint, request

authentication_blueprint = Blueprint('authentication_blueprint', __name__)

@authentication_blueprint.route('/auth-login', methods=['GET'])
def login():
    args = request.args

    return "True"
