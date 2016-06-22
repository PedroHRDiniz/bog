from nltk.sentiment.vader import SentimentIntensityAnalyzer
class SentimentParser:
    _sid = SentimentIntensityAnalyzer()
    def parse(self, text):
        return self._sid.polarity_scores(text)