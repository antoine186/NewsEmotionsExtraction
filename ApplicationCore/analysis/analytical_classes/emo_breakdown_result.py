class EmoBreakdownResult:
    def __init__(self, title, description, publisher, published_date, url, emo_breakdown, extracted_keywords) -> None:
        self.title = title
        self.description = description
        self.publisher = publisher
        self.published_date = published_date
        self.url = url
        self.emo_breakdown = emo_breakdown
        self.extracted_keywords = extracted_keywords
