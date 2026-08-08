import unittest
from build_listing import extract_date, format_date

class TestBuildListing(unittest.TestCase):

    def test_date_extract(self):
        md = '''hello 
        2024-02-02'''
        date = extract_date(md)
        self.assertEqual(date, "2024-02-02") 

    def test_format_date(self):
        date = "2026-08-04"
        self.assertEqual(format_date(date), "Aug 04 2026")
