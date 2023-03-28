from flask import Blueprint, request
from sqlalchemy import text
from models.user import User
from app_start_helper import db
import json

authentication_blueprint = Blueprint('authentication_blueprint', __name__)

@authentication_blueprint.route('/auth-login', methods=['POST'])
def login():
    payload = request.data
    payload = json.loads(payload)

    result = db.session.execute(text('SELECT user_schema.check_username_password(:username,:password)'), {'username': payload['username'], 'password': payload['password']}).fetchall()

    if result[0][0] == 1:
        return json.dumps(True)

    return json.dumps(False)
