from flask import Blueprint, request, make_response
import json
from gnews import GNews
from datetime import datetime, timedelta
from operator import attrgetter
from app_start_helper import nn, model_max_characters_allowed, keyword_extractor_nn
from analysis.news_classifier import NewsClassifier
from Utils.json_encoder import GenericJsonEncoder
from app_start_helper import db
from sqlalchemy import text

emo_search_blueprint = Blueprint('emo_search_blueprint', __name__)

@emo_search_blueprint.route('/api/search', methods=['POST'])
def emo_search():
    try:
        payload = request.data
        payload = json.loads(payload)

        attributes = ('year', 'month', 'day')

        search_end_date = datetime.strptime(payload['dateInput'], '%Y-%m-%d')
        search_start_date = search_end_date - timedelta(days=7)

        search_end_date = attrgetter(*attributes)(search_end_date)
        search_start_date = attrgetter(*attributes)(search_start_date)

        google_news = GNews(language='en', country='US', start_date = search_start_date, end_date = search_end_date, max_results = 20)

        results = google_news.get_news(payload['searchInput'])

        news_classifier = NewsClassifier(nn, results, google_news, model_max_characters_allowed, keyword_extractor_nn, payload['searchInput'], \
                                        search_start_date, search_end_date)
        
        emo_breakdown_result_metadata = news_classifier.get_emo_percentage_breakdown_with_leading_results()

        if emo_breakdown_result_metadata != None:
            emo_breakdown_result_metadata_json_data = json.dumps(emo_breakdown_result_metadata, indent=4, cls=GenericJsonEncoder)

            get_user_id = 'SELECT user_schema.get_user_id(:username)'

            user_id = db.session.execute(text(get_user_id), {'username': payload['username']}).fetchall()

            delete_search_result_sp = 'CALL search_schema.delete_search_result(:user_id)'

            db.session.execute(text(delete_search_result_sp), {'user_id': user_id[0][0]})

            db.session.commit()

            save_search_result_sp = 'CALL search_schema.save_search_result(:user_id,:search_result_json)'

            db.session.execute(text(save_search_result_sp), {'user_id': user_id[0][0], 'search_result_json': emo_breakdown_result_metadata_json_data})

            db.session.commit()

            response = make_response(emo_breakdown_result_metadata_json_data)
        else:
            response = make_response(json.dumps('Error'))

        return response
    
    except Exception as e:
        response = make_response(json.dumps('Error'))

        return response
