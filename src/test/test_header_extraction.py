import unittest

from src.extraction import extract_title


class TestHeaderExtraction(unittest.TestCase):
    def test_extraction(self):
        title = extract_title("""
# test 
        """)

        self.assertEqual(title, "test")
