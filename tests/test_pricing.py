import unittest
from src.pricing_clean import calculate_total

class PricingTests(unittest.TestCase):
    def test_regular_price(self):
        self.assertEqual(calculate_total(100), 110.0)

    def test_discount_before_tax(self):
        self.assertEqual(calculate_total(100, discount_percent=10, tax_rate=0.10), 99.0)

    def test_full_discount(self):
        self.assertEqual(calculate_total(100, discount_percent=100), 0.0)

    def test_negative_subtotal_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total(-1)

    def test_discount_over_100_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total(100, discount_percent=120)

    def test_negative_discount_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total(100, discount_percent=-10)

    def test_negative_tax_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total(100, tax_rate=-0.1)

    def test_tax_over_100_percent_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total(100, tax_rate=1.5)

if __name__ == "__main__":
    unittest.main()
