import unittest
from is_prime import is_prime


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2), '2 tub son')
        self.assertTrue(is_prime(3), '3 tub son')
        self.assertTrue(is_prime(5), '5 tub son')
        self.assertTrue(is_prime(17), '17 tub son')

    def test_not_prime(self):
        self.assertFalse(is_prime(1), '1 tub son emas')
        self.assertFalse(is_prime(4), '4 tub son emas')
        self.assertFalse(is_prime(267), '267 tub son emas')


if __name__ == '__main__':
    unittest.main()
