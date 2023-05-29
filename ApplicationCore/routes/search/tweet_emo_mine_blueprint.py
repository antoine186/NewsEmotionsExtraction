from flask import Blueprint, request, make_response
import json
from app_start_helper import db
from sqlalchemy import text

tweet_emo_mine_blueprint = Blueprint('tweet_emo_mine_blueprint', __name__)

@tweet_emo_mine_blueprint.route('/api/tweet_emo_mine', methods=['POST'])
def tweet_emo_mine():
    try:
        payload = request.data
        payload = json.loads(payload)

        get_user_id = 'SELECT user_schema.get_user_id(:username)'

        user_id = db.session.execute(text(get_user_id), {'username': payload['username']}).fetchall()

        check_still_charting = 'SELECT search_schema.check_still_charting(:user_id)'

        still_charting = db.session.execute(text(check_still_charting), {'user_id': user_id[0][0]}).fetchall()
        
        if still_charting[0][0] != None:
            operation_response = {
                "operation_success": True,
                "responsePayload": {
                    "still_searching": still_charting[0][0]
                },
                "error_message": ""
            }
            response = make_response(json.dumps(operation_response))
            return response
        else:
            operation_response = {
                "operation_success": False,
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
