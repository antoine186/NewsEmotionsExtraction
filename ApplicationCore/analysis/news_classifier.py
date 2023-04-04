

class NewsClassifier:
    def __init__(self, nns, search_results):
        self.main_emo_classification_nn_model = nns.main_emo_classification_nn_model
        self.main_emo_classification_nn_tokenizer = nns.main_emo_classification_nn_tokenizer
        self.search_results = search_results

    def get_emo_percentage_breakdown_with_leading_results(self):
         for result in self.search_results:
             xyz = result
             
