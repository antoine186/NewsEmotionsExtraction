# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
from ApplicationCore.config import stripe_api_key
stripe.api_key = stripe_api_key

from flask import Blueprint, request, make_response
import json
from app_start_helper import db
from sqlalchemy import text

delete_subscription_blueprint = Blueprint('setupintent_creation_blueprint', __name__)

@delete_subscription_blueprint.route('/api/delete_subscription', methods=['POST'])
def delete_subscription():
    payload = request.data
    payload = json.loads(payload)

    try:
        stripe.Subscription.delete(
            payload['stripeSubscriptionId'],
        )

        get_user_id = 'SELECT user_schema.get_user_id(:username)'

        user_id = db.session.execute(text(get_user_id), {'username': payload['username']}).fetchall()

        get_internal_stripe_customer_id = 'SELECT payment_schema.get_internal_stripe_customer_id(:user_id)'

        internal_stripe_customer_id = db.session.execute(text(get_internal_stripe_customer_id), {'user_id': user_id[0][0]}).fetchall()

        delete_subscription_sp = 'CALL payment_schema.delete_subscription(:internal_stripe_customer_id)'

        db.session.execute(text(delete_subscription_sp), {'internal_stripe_customer_id': internal_stripe_customer_id[0][0]})

        db.session.commit()

        operation_response = {
            "operation_success": True,
            "responsePayload": {
            },
            "error_message": ""
        }
        response = make_response(json.dumps(operation_response))
        return response
    except Exception as e:
        operation_response = {
            "operation_success": False,
            "responsePayload": {
            },
            "error_message": "" 
        }
        response = make_response(json.dumps(operation_response))
        return response
