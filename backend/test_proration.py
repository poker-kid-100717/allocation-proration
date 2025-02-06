import unittest
from main import Investor
from proration import prorate_allocation

class TestProration(unittest.TestCase):

    def test_proration_simple(self):
        investors = [
            Investor(name="A", requested_amount=100, average_amount=100),
            Investor(name="B", requested_amount=25, average_amount=25),
        ]
        result = prorate_allocation(100, investors)
        self.assertAlmostEqual(result["A"], 80)
        self.assertAlmostEqual(result["B"], 20)

    def test_full_funding(self):
        investors = [
            Investor(name="A", requested_amount=50, average_amount=100),
            Investor(name="B", requested_amount=50, average_amount=100),
        ]
        result = prorate_allocation(200, investors)
        self.assertEqual(result["A"], 50)
        self.assertEqual(result["B"], 50)

    def test_excess_allocation(self):
        investors = [
            Investor(name="A", requested_amount=100, average_amount=100),
            Investor(name="B", requested_amount=50, average_amount=100),
        ]
        result = prorate_allocation(100, investors)
        self.assertAlmostEqual(result["A"], 50)
        self.assertAlmostEqual(result["B"], 50)

if __name__ == "__main__":
    unittest.main()
