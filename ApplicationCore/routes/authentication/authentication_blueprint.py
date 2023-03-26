from flask import Blueprint, request
from models.user import User

authentication_blueprint = Blueprint('authentication_blueprint', __name__)

@authentication_blueprint.route('/auth-login', methods=['GET'])
def login():
    args = request.args

    '''
    new_test_user = User(
        username = 'batman',
        password = '123',
        first_name = 'bat',
        last_name = 'man',
        primary_email = 'bat@man.com',
        date_of_birth = '2000-01-01',
        telephone_number = '123123',
        telephone_area_code = '33'
    )
    '''

    all_results = User.query.all()

    return "True"
