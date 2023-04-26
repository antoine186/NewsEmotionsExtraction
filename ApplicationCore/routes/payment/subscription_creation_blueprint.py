# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
from ApplicationCore.config import stripe_api_key
stripe.api_key = stripe_api_key

from flask import Blueprint, request, make_response
import json
from app_start_helper import db
from sqlalchemy import text

subscription_creation_blueprint = Blueprint('subscription_creation_blueprint', __name__)

@subscription_creation_blueprint.route('/api/subscription_create', methods=['POST'])
def subscription_create():
    payload = request.data
    payload = json.loads(payload)

    customer_id = payload['stripeCustomerId']
    price_id = payload['priceId']

    try:
        # Create the subscription. Note we're expanding the Subscription's
        # latest invoice and that invoice's payment_intent
        # so we can pass it to the front end to confirm the payment
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[{
                'price': price_id,
            }],
            payment_behavior='default_incomplete',
            payment_settings={'save_default_payment_method': 'on_subscription'},
            expand=['latest_invoice.payment_intent'],
        )

        # DB operations here
        get_user_id = 'SELECT user_schema.get_user_id(:username)'

        user_id = db.session.execute(text(get_user_id), {'username': payload['accountCreationData']['emailAddress']}).fetchall()

        add_stripe_customer_sp = 'CALL payment_schema.add_stripe_customer(:user_id,:stripe_customer_id)'

        db.session.execute(text(add_stripe_customer_sp), {'user_id': user_id, 'stripe_customer_id': customer_id})
        db.session.commit()

        #
        get_internal_stripe_customer_id
        _user_id

        get_internal_stripe_customer_id = 'SELECT payment_schema.get_internal_stripe_customer_id(:user_id)'

        internal_stripe_customer_id = db.session.execute(text(get_internal_stripe_customer_id), {'user_id': user_id}).fetchall()

        add_stripe_subscription_sp = 'CALL payment_schema.add_stripe_subscription(:stripe_subscription_id,:internal_stripe_customer_id,:stripe_subscription_status)'

        db.session.execute(text(add_stripe_subscription_sp), {'stripe_subscription_id': subscription.id, 'internal_stripe_customer_id': \
                                                              internal_stripe_customer_id, 'stripe_subscription_status': subscription.payment_behavior})
        db.session.commit()

        operation_response = {
            "operation_success": True,
            "responsePayload": {
                "subscription_id": subscription.id,
                "client_secret": subscription.latest_invoice.payment_intent.client_secret
            },
            "error_message": "" 
        }
        response = make_response(json.dumps(operation_response))
        return response

    except Exception as e:
        operation_response = {
            "operation_success": False,
            "error_message": "" 
        }
        response = make_response(json.dumps(operation_response))
        return response
    