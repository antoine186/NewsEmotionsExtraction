from flask import Blueprint, request, make_response
import json
from gnews import GNews
from datetime import datetime, timedelta
from operator import attrgetter

emo_search_blueprint = Blueprint('emo_search_blueprint', __name__)

@emo_search_blueprint.route('/api/search', methods=['POST'])
def login():
    payload = request.data
    payload = json.loads(payload)

    attributes = ('year', 'month', 'day')

    search_end_date = datetime.strptime(payload['dateInput'], '%Y-%m-%d')
    search_start_date = search_end_date - timedelta(days=7)

    search_end_date = attrgetter(*attributes)(search_end_date)
    search_start_date = attrgetter(*attributes)(search_start_date)

    google_news = GNews(language='en', country='US', start_date = search_start_date, end_date = search_end_date)
    results = google_news.get_news(payload['searchInput'])
