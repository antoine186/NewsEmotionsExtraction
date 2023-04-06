class EmoBreakdownResultMetadata:
    def __init__(self, emo_breakdown_results, nb_articles_skipped, average_emo_breakdown, most_angry_article, 
                 most_disgusted_article, sadest_article, happiest_article, most_fearful_article, most_surprised_article,
                 most_neutral_article) -> None:
        self.emo_breakdown_results = emo_breakdown_results
        self.nb_articles_skipped = nb_articles_skipped
        self.average_emo_breakdown = average_emo_breakdown

        self.most_angry_article = most_angry_article
        self.most_disgusted_article = most_disgusted_article
        self.sadest_article = sadest_article
        self.happiest_article = happiest_article
        self.most_fearful_article = most_fearful_article
        self.most_surprised_article = most_surprised_article
        self.most_neutral_article = most_neutral_article

    def get_emo_breakdown_result_metadata(self):
        emo_breakdown_result_metadata_dict = {
            'emo_breakdown_results': self.emo_breakdown_results,
            'nb_articles_skipped': self.nb_articles_skipped,
            'average_emo_breakdown': self.average_emo_breakdown,
            'most_angry_article': self.most_angry_article,
            'most_disgusted_article': self.most_disgusted_article,
            'sadest_article': self.sadest_article,
            'happiest_article': self.happiest_article,
            'most_fearful_article': self.most_fearful_article,
            'most_surprised_article': self.most_surprised_article,
            'most_neutral_article': self.most_neutral_article,
        }

        return emo_breakdown_result_metadata_dict