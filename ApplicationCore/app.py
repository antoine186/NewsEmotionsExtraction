import sys
sys.path.append('ApplicationCore')
sys.path.append('ApplicationCore/routes')
sys.path.append('ApplicationCore/scheduled_jobs')
from scheduled_jobs.session_kick import session_kick
from scheduled_jobs.apscheduler_start_cleanup import apscheduler_start_cleanup
from scheduled_jobs.tagging_update import tagging_update

from app_start_helper import app, db
from main_pages.main_page_blueprint import main_page_blueprint
from authentication.authentication_blueprint import authentication_blueprint
from authentication.session_authentication_blueprint import session_authentication_blueprint
from search.emo_search_blueprint import emo_search_blueprint
from account_data.basic_account_creation_blueprint import basic_account_creation_blueprint
from payment.stripe_customer_creation_blueprint import stripe_customer_creation_blueprint
from payment.subscription_creation_blueprint import subscription_creation_blueprint
from payment.get_subscription_status_blueprint import get_subscription_status_blueprint
from payment.get_subscription_id_blueprint import get_subscription_id_blueprint
from payment.store_new_subscription_blueprint import store_new_subscription_blueprint
from payment.update_subscription_status_blueprint import update_subscription_status_blueprint
from account_data.delete_account_blueprint import delete_account_blueprint
from payment.retrieve_subscription_details_blueprint import retrieve_subscription_details_blueprint
from account_data.retrieve_account_data_blueprint import retrieve_account_data_blueprint
from payment.setupintent_creation_blueprint import setupintent_creation_blueprint
from payment.get_stripe_customer_id_blueprint import get_stripe_customer_id_blueprint
from payment.delete_subscription_blueprint import delete_subscription_blueprint
from authentication.forgot_password_blueprint import forgot_password_blueprint
from authentication.password_reset_blueprint import password_reset_blueprint
from search.get_previous_search_result_blueprint import get_previous_search_result_blueprint
from search.tagging_search_blueprint import tagging_search_blueprint
from search.get_tagging_inputs_blueprint import get_tagging_inputs_blueprint
from search.save_tagging_inputs_blueprint import save_tagging_inputs_blueprint
from search.update_tagging_inputs_blueprint import update_tagging_inputs_blueprint
from search.get_previous_tagging_result_blueprint import get_previous_tagging_result_blueprint
from search.delete_tag_blueprint import delete_tag_blueprint
from search.delete_tagging_inputs_blueprint import delete_tagging_inputs_blueprint
from search.progression_charting_blueprint import progression_charting_blueprint
from search.get_previous_charting_blueprint import get_previous_charting_blueprint
from search.linking_blueprint import linking_blueprint
from search.get_previous_linking_blueprint import get_previous_linking_blueprint

# app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(main_page_blueprint)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(session_authentication_blueprint)
app.register_blueprint(emo_search_blueprint)
app.register_blueprint(basic_account_creation_blueprint)
app.register_blueprint(stripe_customer_creation_blueprint)
app.register_blueprint(subscription_creation_blueprint)
app.register_blueprint(get_subscription_status_blueprint)
app.register_blueprint(get_subscription_id_blueprint)
app.register_blueprint(store_new_subscription_blueprint)
app.register_blueprint(update_subscription_status_blueprint)
app.register_blueprint(delete_account_blueprint)
app.register_blueprint(retrieve_subscription_details_blueprint)
app.register_blueprint(retrieve_account_data_blueprint)
#app.register_blueprint(setupintent_creation_blueprint)
app.register_blueprint(get_stripe_customer_id_blueprint)
app.register_blueprint(delete_subscription_blueprint)
app.register_blueprint(forgot_password_blueprint)
app.register_blueprint(password_reset_blueprint)
app.register_blueprint(get_previous_search_result_blueprint)
app.register_blueprint(tagging_search_blueprint)
app.register_blueprint(get_tagging_inputs_blueprint)
app.register_blueprint(save_tagging_inputs_blueprint)
app.register_blueprint(update_tagging_inputs_blueprint)
app.register_blueprint(get_previous_tagging_result_blueprint)
app.register_blueprint(delete_tag_blueprint)
app.register_blueprint(delete_tagging_inputs_blueprint)
app.register_blueprint(progression_charting_blueprint)
app.register_blueprint(get_previous_charting_blueprint)
app.register_blueprint(linking_blueprint)
app.register_blueprint(get_previous_linking_blueprint)

with app.app_context():
    db.init_app(app)

    session_kick()
    tagging_update()
    apscheduler_start_cleanup()

if __name__ == '__main__':
    app.debug = True
    app.run()
