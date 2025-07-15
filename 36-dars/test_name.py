import unittest
from name import get_full_name


class TestName(unittest. TestCase):
    def test_full_name(self):
        result = get_full_name("anvar", "botirov")
        self.assertEqual(result, "Anvar Botirov")
        # self.assertEqual(get_full_name("anvar", "botirov"), "Anvar Botirov") # Kodni qisqaroq yozish

    def test_otasi_ism(self):
        name = get_full_name("anvar", "botirov", "majidovich")
        self.assertEqual(name, 'Anvar Majidovich Botirov')


if __name__ == '__main__':
    unittest.main()
