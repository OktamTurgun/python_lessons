"""
Created on Fri Jun 22:11:14 2025

37-dars. Klasslarni tekshirish 

@author: uktam
"""
import unittest
from product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Laptop", 1200, 10)

    def test_get_info(self):
        self.assertEqual(self.product1.get_info(), "Laptop - 1200 (10 dona)")

    def test_price_valid(self):
        self.product1.set_price(1500)
        self.assertEqual(self.product1.get_price(), 1500)

    def test_set_price_invalid(self):
        with self.assertRaises(ValueError):
            self.product1.set_price(-100)

    def test_update_price_positive(self):
        self.product1.update_price(200)
        self.assertEqual(self.product1.get_price(), 1400)

    def test_update_price_negative_valid(self):
        self.product1.update_price(-200)
        self.assertEqual(self.product1.get_price(), 1000)

    def test_update_price_negative(self):
        with self.assertRaises(ValueError):
            self.product1.update_price(-1300)

    def test_set_quantity_valid(self):
        self.product1.set_quantity(20)
        self.assertEqual(self.product1.get_quantity(), 20)

    def test_set_quantity_invalid(self):
        with self.assertRaises(ValueError):
            self.product1.set_quantity(-5)

    def test_update_quantity_positive(self):
        self.product1.update_quantity(5)
        self.assertEqual(self.product1.get_quantity(), 15)

    def test_update_quantity_negative_valid(self):
        self.product1.update_quantity(-5)
        self.assertEqual(self.product1.get_quantity(), 5)

    def test_update_quantity_to_negative(self):
        with self.assertRaises(ValueError):
            self.product1.update_quantity(-15)

    def test_apply_discount_valid(self):
        self.product1.applay_discount(10)
        self.assertAlmostEqual(self.product1.get_price(), 1080.0)

    def test_apply_discount_invalid(self):
        with self.assertRaises(ValueError):
            self.product1.applay_discount(150)

    def test_restock_valid(self):
        self.product1.restock(5)
        self.assertEqual(self.product1.get_quantity(), 15)

    def test_restock_invalid(self):
        with self.assertRaises(ValueError):
            self.product1.restock(0)

    def test_sell_valid(self):
        self.product1.sell(4)
        self.assertEqual(self.product1.get_quantity(), 6)

    def test_sell_invalid_negative(self):
        with self.assertRaises(ValueError):
            self.product1.sell(0)

    def test_sell_insufficient_quantity(self):
        with self.assertRaises(ValueError):
            self.product1.sell(20)


if __name__ == "__main__":
    unittest.main()
