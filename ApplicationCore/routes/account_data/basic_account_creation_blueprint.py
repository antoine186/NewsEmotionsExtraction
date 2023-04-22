from flask import Blueprint, request, make_response
import json
from app_start_helper import db
from sqlalchemy import text

basic_account_creation_blueprint = Blueprint('basic_account_creation_blueprint', __name__)

@basic_account_creation_blueprint.route('/api/basic-account-create', methods=['POST'])
def basic_account_create():
    payload = request.data
    payload = json.loads(payload)

    add_basic_account_data_sp = 'CALL user_schema.add_basic_account_data(:primary_email,:password,:first_name,:last_name, \
        :date_of_birth,:telephone_number,:telephone_area_code)'
    
    get_user_id = 'SELECT user_schema.get_user_id(:username)'
    
    add_user_address_sp = 'CALL user_schema.add_user_address(:user_id,:country,:city,:state,:street_1,:street_2,:zipcode)'

    db.session.execute(text(add_basic_account_data_sp), {'first_name': payload['accountCreationData']['firstName'], 'last_name': payload['accountCreationData']['lastName'], \
                                                         'date_of_birth': payload['accountCreationData']['dateBirth'], 'primary_email': payload['accountCreationData']['emailAddress'], \
                                                            'telephone_number': payload['accountCreationData']['telephoneNumber'], 'telephone_area_code': payload['accountCreationData']['telephoneAreaCode'], \
                                                                'password': payload['accountCreationData']['password']})
    
    created_user_id = db.session.execute(text(get_user_id), {'username': payload['accountCreationData']['emailAddress']}).fetchall()

    if len(created_user_id) > 0:
        db.session.execute(text(add_user_address_sp), {})
