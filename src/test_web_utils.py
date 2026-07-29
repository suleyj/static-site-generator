import unittest
from web_utils import extract_title

class TestWebUtils(unittest.TestCase):

    def test_extract_title(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello") 
