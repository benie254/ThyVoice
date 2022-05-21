import unittest
from app.models import Blog


class BlogTest(unittest.TestCase):
    """
    test behavior of Pitch class
    """

    def setUp(self):
        """
        runs before every test
        """

        self.new_pitch = Blog('The Dream and The Dreamer', 'A world of dreams', 'If I could remember a time when I dreamed, it would be my last','poetry')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))
