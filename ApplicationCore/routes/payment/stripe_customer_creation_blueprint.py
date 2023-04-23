# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
from ApplicationCore.config import stripe_api_key
stripe.api_key = stripe_api_key

from flask import Blueprint, request, make_response
import json
from app_start_helper import db
from sqlalchemy import text

stripe_customer_creation_blueprint = Blueprint('stripe_customer_creation_blueprint', __name__)

@stripe_customer_creation_blueprint.route('/api/stripe-customer-create', methods=['POST'])
def stripe_customer_create():
    payload = request.data
    payload = json.loads(payload)

    new_stripe_customer = stripe.Customer.create(
    email=payload['accountCreationData']['emailAddress'],
    name=payload['accountCreationData']['firstName'] + " " + payload['accountCreationData']['lastName'],
    address={
        "city": payload['accountCreationData']['selectedCityName'],
        "country": payload['accountCreationData']['selectedCountryCode'],
        "line1": payload['accountCreationData']['addressLine1'],
        "line2": payload['accountCreationData']['addressLine2'],
        "postal_code": payload['accountCreationData']['zipCode'],
        "state": payload['accountCreationData']['selectedStateCode'],
    },
    )

    operation_response = {
        "operation_success": True,
        "responsePayload": {
            "stripe_customer_id": new_stripe_customer.id
        },
        "error_message": "" 
    }
    response = make_response(json.dumps(operation_response))
    return response
    