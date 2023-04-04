class EmoBreakdownPercentage:
    def __init__(self, sadness, joy, love, anger, fear, surprise) -> None:
        self.sadness = sadness
        self.joy = joy
        self.love = love
        self.anger = anger
        self.fear = fear
        self.surprise = surprise

    def get_emo_breakdown_percentage(self):
        emo_percentages_dict = {
            "sadness": self.sadness,
            "joy": self.joy,
            "love": self.love,
            "anger": self.anger,
            "fear": self.fear,
            "surprise": self.surprise,
        }

        return emo_percentages_dict

"""
sadness 😢
joy 😃
love 🥰
anger 😡
fear 😱
surprise 😯
"""