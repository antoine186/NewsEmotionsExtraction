from flask import Blueprint, request, make_response
from sqlalchemy import text
from models.user_safe_view import UserSafeView
from app_start_helper import db
from Utils.create_secret_token import create_secret_token
import json

authentication_blueprint = Blueprint('authentication_blueprint', __name__)

@authentication_blueprint.route('/auth-login', methods=['POST'])
def login():
    payload = request.data
    payload = json.loads(payload)

    seconds = 7200

    credential_confirmed = db.session.execute(text('SELECT user_schema.check_username_password(:username,:password)'), {'username': payload['username'], 'password': payload['password']}).fetchall()

    if credential_confirmed[0][0] == 1:
        user_safe_view = UserSafeView.query.filter_by(username = payload['username']).first()
        secret_token_1 = create_secret_token()
        secret_token_2 = create_secret_token()

        session_token = {
            'username': payload['username'],
            'secret_token_1': secret_token_1,
            'secret_token_2': secret_token_2
        }

        response = make_response(json.dumps(True))
        response.set_cookie('user_session_cookie', json.dumps(session_token), max_age = seconds)

        return response

    response = make_response(json.dumps(False))
    return response
