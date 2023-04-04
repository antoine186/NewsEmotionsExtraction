
class NewsClassifier:
    def __init__(self, nn, search_results, google_news, model_max_tokens_allowed):
        self.main_emo_classification_nn_model = nn.nn_model
        self.search_results = search_results
        self.google_news = google_news
        self.model_max_tokens_allowed = model_max_tokens_allowed

    def get_emo_percentage_breakdown_with_leading_results(self):
        nb_articles_skipped = 0

        for result in self.search_results:
            article = self.google_news.get_full_article(result['url'])

            if len(article.text) < self.model_max_tokens_allowed:
                """
                input_ids = self.main_emo_classification_nn_tokenizer.encode(
                    article.text, return_tensors='pt')
                output = self.main_emo_classification_nn_model.generate(
                    input_ids=input_ids)

                decoded = [self.main_emo_classification_nn_tokenizer.decode(ids) for ids in output]
                label = decoded[0]
                """

                raw_emo_breakdown = self.main_emo_classification_nn_model(article.text)

                print(raw_emo_breakdown)
            else:
                nb_articles_skipped += 1
                continue
