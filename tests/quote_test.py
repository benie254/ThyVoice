import unittest
from app.models import Quote


class QuotesTestCase(unittest.TestCase):
    """
    Test behavior of the Quotes class
    """

    def setUp(self):
        """
        Runs before every test
        """

        self.new_quote = Quote('Python-Flask is such an experience', 'Jared K.','https://quotesapi.test.com')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Quote))
