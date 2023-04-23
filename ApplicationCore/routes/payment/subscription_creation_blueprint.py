# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

from flask import Blueprint, request, make_response
import json
from app_start_helper import db
from sqlalchemy import text

basic_account_creation_blueprint = Blueprint('basic_account_creation_blueprint', __name__)

@basic_account_creation_blueprint.route('/api/basic-account-create', methods=['POST'])
def basic_account_create():
    payload = request.data
    payload = json.loads(payload)

    stripe.Customer.create(
    email="{{CUSTOMER_EMAIL}}",
    name="{{CUSTOMER_NAME}}",
    address={
        "city": "Brothers",
        "country": "US",
        "line1": "27 Fredrick Ave",
        "line2": "",
        "postal_code": "97712",
        "state": "CA",
    },
    )
