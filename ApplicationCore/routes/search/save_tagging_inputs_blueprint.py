from flask import Blueprint, request, make_response
import json
from app_start_helper import db
from sqlalchemy import text
from Utils.json_encoder import GenericJsonEncoder

save_tagging_inputs_blueprint = Blueprint('save_tagging_inputs_blueprint', __name__)

@save_tagging_inputs_blueprint.route('/api/save-tagging-inputs', methods=['POST'])
def save_tagging_inputs():
    payload = request.data
    payload = json.loads(payload)

    try:
        get_user_id = 'SELECT user_schema.get_user_id(:username)'

        user_id = db.session.execute(text(get_user_id), {'username': payload['username']}).fetchall()

        tagging_input_list_json = json.dumps(payload['taggingInputList'], indent=4, cls=GenericJsonEncoder)

        save_tagging_input_sp = 'CALL search_schema.save_tagging_input(:user_id,:tagging_input_list)'

        db.session.execute(text(save_tagging_input_sp), {'user_id': user_id[0][0], 'tagging_input_list': tagging_input_list_json})

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
