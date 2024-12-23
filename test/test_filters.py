import unittest
from filters import filter_tournaments

class TestFilters(unittest.TestCase):
    def setUp(self):
        self.tournaments = [
            {"date": "12/21/24", "type": "RCO", "location": "TUH"},
            {"date": "12/22/24", "type": "COED", "location": "BOS"},
            {"date": "12/21/24", "type": "COED", "location": "TUH"},
        ]

    def test_filter_by_date(self):
        result = filter_tournaments(self.tournaments, date="12/21/24")
        self.assertEqual(len(result), 2)

    def test_filter_by_type(self):
        result = filter_tournaments(self.tournaments, type="COED")
        self.assertEqual(len(result), 2)

    def test_filter_by_location(self):
        result = filter_tournaments(self.tournaments, location="TUH")
        self.assertEqual(len(result), 2)

    def test_combined_filters(self):
        result = filter_tournaments(self.tournaments, date="12/21/24", type="RCO", location="TUH")
        self.assertEqual(len(result), 1)

if __name__ == "__main__":
    unittest.main()
