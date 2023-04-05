import sys
sys.path.append("ApplicationCore/analysis")

from analytical_classes.emo_breakdown_result import EmoBreakdownResult
from Utils.text_divider import text_divider
from analysis.analytical_utils.get_emo_breakdown_percentage import get_emo_breakdown_percentage
from analysis.analytical_utils.get_emo_breakdown_from_tranches import get_emo_breakdown_from_tranches


class NewsClassifier:
    def __init__(self, nn, search_results, google_news, model_max_characters_allowed):
        self.main_emo_classification_nn_model = nn.nn_model
        self.search_results = search_results
        self.google_news = google_news
        self.model_max_characters_allowed = model_max_characters_allowed

    def get_emo_percentage_breakdown_with_leading_results(self):
        nb_articles_skipped = 0
        emo_breakdown_results = []

        most_emo_dict = {
        'anger': {'score': 0, 'index': -1},
        'disgust': {'score': 0, 'index': -1},
        'joy': {'score': 0, 'index': -1},
        'sadness': {'score': 0, 'index': -1},
        'fear': {'score': 0, 'index': -1},
        'surprise': {'score': 0, 'index': -1},
        'neutral': {'score': 0, 'index': -1},
        }

        result_counter = 0

        for result in self.search_results:
            try:
                article = self.google_news.get_full_article(result['url'])
            except:
                nb_articles_skipped += 1
                continue

            if (article == None):
                nb_articles_skipped += 1
                continue

            if len(article.text) < self.model_max_characters_allowed:
                """
                input_ids = self.main_emo_classification_nn_tokenizer.encode(
                    article.text, return_tensors='pt')
                output = self.main_emo_classification_nn_model.generate(
                    input_ids=input_ids)

                decoded = [self.main_emo_classification_nn_tokenizer.decode(ids) for ids in output]
                label = decoded[0]
                """

                raw_emo_breakdown = self.main_emo_classification_nn_model(
                    article.text)
                emo_breakdown = raw_emo_breakdown[0]

                emo_breakdown_percentage, most_emo_dict = get_emo_breakdown_percentage(emo_breakdown, result_counter, most_emo_dict)

                emo_breakdown_result = EmoBreakdownResult(
                    article.title, result['description'], result['publisher']['title'], result['published date'], article.canonical_link, emo_breakdown_percentage)
                emo_breakdown_results.append(emo_breakdown_result)
                result_counter += 1
            else:
                tranches_list = text_divider(article.text, self.model_max_characters_allowed)

                emo_breakdown_result, most_emo_dict = get_emo_breakdown_from_tranches(result_counter, most_emo_dict, tranches_list, self.main_emo_classification_nn_model, article, result)
                emo_breakdown_results.append(emo_breakdown_result)

                result_counter += 1

        return emo_breakdown_results
