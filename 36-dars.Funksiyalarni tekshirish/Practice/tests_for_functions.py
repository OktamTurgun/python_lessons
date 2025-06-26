import unittest
from functions import max_num, capitalize_words, extract_even_nums, is_fibonacci


class TestMaxNum(unittest.TestCase):
    def test_mux_num(self):
        self.assertEqual(max_num(12, 7, 24), 24)
        self.assertEqual(max_num(10, 20, 30), 30)
        self.assertEqual(max_num(30, 20, 10), 30)
        self.assertEqual(max_num(20, 30, 10), 30)
        self.assertEqual(max_num(-1, -5, -10), -1)
        self.assertEqual(max_num(5, 5, 5), 5)

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words(['kofta', 'shim', 'kurtka']), [
                         'Kofta', 'Shim', 'Kurtka'])
        self.assertEqual(capitalize_words([]), [])
        self.assertEqual(capitalize_words(['anor', 'olma']), ['Anor', 'Olma'])
        self.assertEqual(capitalize_words(['uzbekistan']), ['Uzbekistan'])

    def test_even_nums(self):
        self.assertEqual(extract_even_nums(
            [4, 13, 26, 10, 1, 0]), [4, 26, 10, 0])
        self.assertEqual(extract_even_nums([]), [])
        self.assertEqual(extract_even_nums([1, 3, 5]), [])
        self.assertEqual(extract_even_nums([-2, -1, 0, 1, 2]), [-2, 0, 2])
        self.assertEqual(extract_even_nums([8]), [8])
        self.assertEqual(extract_even_nums([7]), [])

    def test_is_fibonachchi(self):
        self.assertTrue(is_fibonacci(5))
        self.assertFalse(is_fibonacci(7))
        self.assertTrue(is_fibonacci(0))
        self.assertTrue(is_fibonacci(2))
        self.assertTrue(is_fibonacci(6765))

        # False qaytarishi kerak bo'lgan holatlar
        self.assertFalse(is_fibonacci(4))
        self.assertFalse(is_fibonacci(7))
        self.assertFalse(is_fibonacci(10))
        self.assertFalse(is_fibonacci(-3))

        # False qaytarishi kerak bo'lgan holatlar
        self.assertFalse(is_fibonacci(4))
        self.assertFalse(is_fibonacci(7))
        self.assertFalse(is_fibonacci(10))
        self.assertFalse(is_fibonacci(-3))


if __name__ == '__main__':
    unittest.main()
