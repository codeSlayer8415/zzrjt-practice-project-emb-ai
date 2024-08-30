import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # creating three test cases and verify them
        response = sentiment_analyzer("I Love working with python")
        label = response['label']
        self.assertEqual(label,"SENT_POSITIVE")
        # case2
        response2 = sentiment_analyzer("I hate working with Pyhton")
        label2 = response2['label']
        self.assertEqual(label2,"SENT_NEGATIVE")
        # case3
        response3 = sentiment_analyzer("I am neutral on Python")
        label3 = response3['label']
        self.assertEqual(label3,"SENT_NEUTRAL")

unittest.main()