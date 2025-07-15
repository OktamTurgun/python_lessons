"""
Created on Wed Jun 28 07:21:14 2025

37-dars. Klasslarni tekshirish 

@author: uktam
"""
import unittest
from cart import Cart
from product import Product


class TestCartWithProduct(unittest. TestCase):
    def setUp(self):
        self.cart1 = Cart()
        self.apple = Product("Apple", 2.5, 100)
        self.banana = Product("Banana", 1.0, 50)
        self.milk = Product("Milk", 3.5, 75)

    def test_add_product(self):
        self.cart1.add(self.apple, 3)
        self.assertEqual(self.cart1.items[self.apple], 3)

    def test_add_product_twice(self):
        self.cart1.add(self.apple, 5)
        self.cart1.add(self.apple, 3)
        self.assertEqual(self.cart1.items[self.apple], 8)

    def test_add_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.cart1.add(self.apple, 0)

    def test_remove_exiting(self):
        self.cart1.add(self.apple, 1)
        self.cart1.remove(self.apple)
        self.assertNotIn(self.apple, self.cart1.items)

    def test_remove_nonexistent(self):
        with self.assertRaises(ValueError):
            self.cart1.remove(self.milk)

    def test_update_quantity(self):
        self.cart1.add(self.milk, 2)
        self.cart1.update(self.milk, 5)
        self.assertEqual(self.cart1.items[self.milk], 5)

    def test_update_zero(self):
        self.cart1.add(self.apple, 2)
        self.cart1.update(self.apple, 0)
        self.assertNotIn(self.apple, self.cart1.items)

    def test_update_invalid_quantity(self):
        self.cart1.add(self.apple, 3)
        with self.assertRaises(ValueError):
            self.cart1.update(self.apple, -2)

    def test_update_noexistent(self):
        with self.assertRaises(ValueError):
            self.cart1.update(self.banana, 1)

    def test_total_items(self):
        self.cart1.add(self.apple, 2)
        self.cart1.add(self.banana, 3)
        self.cart1.add(self.milk, 1)
        self.assertEqual(self.cart1.total_items(), 6)

    def test_clear_cart(self):
        self.cart1.add(self.banana, 2)
        self.cart1.clear()
        self.assertEqual(len(self.cart1.items), 0)


if __name__ == '__main__':
    unittest.main()


'''
    def test_clear_cart(self):
        self.cart.add(self.apple, 1)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)

if __name__ == "__main__":
    unittest.main()
'''
