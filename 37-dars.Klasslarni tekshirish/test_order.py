"""
Created on Sat Jun 28 00:00:37 2025

37-dars. Klasslarni tekshirish 

@author: uktam
"""
import unittest
from product import Product
from order import Order


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.phone = Product("Phone", 1000, 5)
        self.case = Product("Case", 50, 10)
        self.order = Order()

    def test_add_product_valid(self):
        self.order.add_product(self.phone, 2)
        self.assertEqual(len(self.order.items), 1)
        self.assertEqual(self.phone.get_quantity(), 3)

    def test_add_product_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.order.add_product(self.phone, 6)

    def test_add_product_zero(self):
        with self.assertRaises(ValueError):
            self.order.add_product(self.phone, 0)

    def test_total(self):
        self.order.add_product(self.phone, 1)
        self.order.add_product(self.case, 2)
        self.assertEqual(self.order.total(), 1100)

    def test_summary(self):
        self.order.add_product(self.case, 3)
        summary = self.order.summary()
        self.assertIn("Case x 3 = $150", summary)


if __name__ == "__main__":
    unittest.main()
