import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # creating three test cases and verify them
        response1 = sentiment_analyzer("")
        label1 = response1['label']