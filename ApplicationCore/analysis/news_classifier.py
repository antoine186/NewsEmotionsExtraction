
class NewsClassifier:
    def __init__(self, nns, search_results, google_news):
        self.main_emo_classification_nn_model = nns.nn_model
        self.main_emo_classification_nn_tokenizer = nns.nn_tokenizer
        self.search_results = search_results
        self.google_news = google_news

    def get_emo_percentage_breakdown_with_leading_results(self):
        for result in self.search_results:
            article = self.google_news.get_full_article(result['url'])
            print(len(article.text))

            input_ids = self.main_emo_classification_nn_tokenizer.encode(
                article.text, return_tensors='pt')
            output = self.main_emo_classification_nn_model.generate(
                input_ids=input_ids, max_length=2)
