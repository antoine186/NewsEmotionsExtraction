from flask import Blueprint, request, make_response
import json
from app_start_helper import db
from sqlalchemy import text
from datetime import datetime, timedelta
from operator import attrgetter
from gnews import GNews
from analysis.news_classifier import NewsClassifier
from app_start_helper import nn, model_max_characters_allowed, keyword_extractor_nn
from Utils.json_encoder import GenericJsonEncoder

tagging_search_blueprint = Blueprint('tagging_search_blueprint', __name__)

@tagging_search_blueprint.route('/api/tagging-search', methods=['POST'])
def tagging_search():
    payload = request.data
    payload = json.loads(payload)

    get_user_id = 'SELECT user_schema.get_user_id(:username)'

    user_id = db.session.execute(text(get_user_id), {'username': payload['username']}).fetchall()

    get_existing_tagging_query_id = 'SELECT search_schema.get_existing_tagging_query_id(:user_id,:tagging_query)'

    existing_tagging_query_id = db.session.execute(text(get_existing_tagging_query_id), {'user_id': user_id[0][0], 'tagging_query': payload['searchInput']}).fetchall()

    if existing_tagging_query_id[0][0] == None:
        save_tagging_query_sp = 'CALL search_schema.save_tagging_query(:user_id,:tagging_query)'
        db.session.execute(text(save_tagging_query_sp), {'user_id': user_id[0][0], 'tagging_query': payload['searchInput']})

        db.session.commit()

    attributes = ('year', 'month', 'day')

    search_end_date = datetime.strptime(payload['searchDate'], '%Y-%m-%d')
    search_start_date = datetime.strptime(payload['dayBeforeSearchDate'], '%Y-%m-%d')
    comparison_start_date = search_start_date - timedelta(days=1)

    search_end_date = attrgetter(*attributes)(search_end_date)
    search_start_date = attrgetter(*attributes)(search_start_date)
    comparison_start_date = attrgetter(*attributes)(comparison_start_date)

    google_news = GNews(language='en', country='US', start_date = search_start_date, end_date = search_end_date, max_results = 20)
    comparison_google_news = GNews(language='en', country='US', start_date = comparison_start_date, end_date = search_start_date, max_results = 20)
    results = google_news.get_news(payload['searchInput'])
    comparison_results = comparison_google_news.get_news(payload['searchInput'])

    try:
        news_classifier = NewsClassifier(nn, results, google_news, model_max_characters_allowed, keyword_extractor_nn, payload['searchInput'], \
                                        search_start_date, search_end_date)
        comparison_news_classifier = NewsClassifier(nn, comparison_results, google_news, model_max_characters_allowed, keyword_extractor_nn, payload['searchInput'], \
                                        comparison_start_date, search_start_date)
        emo_breakdown_result_metadata = news_classifier.get_emo_percentage_breakdown_with_leading_results()
        comparison_emo_breakdown_result_metadata = comparison_news_classifier.get_emo_percentage_breakdown_with_leading_results()
        emo_breakdown_result_metadata.previous_average_emo_breakdown = emo_breakdown_result_metadata.average_emo_breakdown
        
        if emo_breakdown_result_metadata != None:
            emo_breakdown_result_metadata_json_data = json.dumps(emo_breakdown_result_metadata, indent=4, cls=GenericJsonEncoder)

            if existing_tagging_query_id[0][0] == None:

                get_existing_tagging_query_id = 'SELECT search_schema.get_existing_tagging_query_id(:user_id,:tagging_query)'

                existing_tagging_query_id = db.session.execute(text(get_existing_tagging_query_id), {'user_id': user_id[0][0], 'tagging_query': payload['searchInput']}).fetchall()

                save_tagging_result_sp = 'CALL search_schema.save_tagging_result(:tagging_query_id,:tagging_result_json)'
                db.session.execute(text(save_tagging_result_sp), {'tagging_query_id': existing_tagging_query_id[0][0], 'tagging_result_json': emo_breakdown_result_metadata_json_data})

                db.session.commit()
            else:
                update_tagging_result_sp = 'CALL search_schema.update_tagging_result(:tagging_query_id,:tagging_result_json)'

                db.session.execute(text(update_tagging_result_sp), {'tagging_query_id': existing_tagging_query_id[0][0], 'tagging_result_json': emo_breakdown_result_metadata_json_data})

                db.session.commit()
        else:
            emo_breakdown_result_metadata_json_data = 'No results'

            get_user_id = 'SELECT user_schema.get_user_id(:username)'

            user_id = db.session.execute(text(get_user_id), {'username': payload['username']}).fetchall()

            get_existing_tagging_query_id = 'SELECT search_schema.get_existing_tagging_query_id(:user_id,:tagging_query)'

            existing_tagging_query_id = db.session.execute(text(get_existing_tagging_query_id), {'user_id': user_id[0][0], 'tagging_query': payload['searchInput']}).fetchall()

            if existing_tagging_query_id[0][0] == None:
                save_tagging_query_sp = 'CALL search_schema.save_tagging_query(:user_id,:tagging_query)'
                db.session.execute(text(save_tagging_query_sp), {'user_id': user_id[0][0], 'tagging_query': payload['searchInput']})

                db.session.commit()

                get_existing_tagging_query_id = 'SELECT search_schema.get_existing_tagging_query_id(:user_id,:tagging_query)'

                existing_tagging_query_id = db.session.execute(text(get_existing_tagging_query_id), {'user_id': user_id[0][0], 'tagging_query': payload['searchInput']}).fetchall()

                save_tagging_result_sp = 'CALL search_schema.save_tagging_result(:tagging_query_id,:tagging_result_json)'
                db.session.execute(text(save_tagging_result_sp), {'tagging_query_id': existing_tagging_query_id[0][0], 'tagging_result_json': emo_breakdown_result_metadata_json_data})

                db.session.commit()
            else:
                update_tagging_result_sp = 'CALL search_schema.update_tagging_result(:tagging_query_id,:tagging_result_json)'

                db.session.execute(text(update_tagging_result_sp), {'tagging_query_id': existing_tagging_query_id[0][0], 'tagging_result_json': emo_breakdown_result_metadata_json_data})

                db.session.commit()

        response = make_response(json.dumps(True))
    except:
        response = make_response(json.dumps('Error'))

    return response
