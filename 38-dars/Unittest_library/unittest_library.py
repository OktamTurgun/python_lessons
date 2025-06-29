"""
18-dars: Python unittest kutubxonasi bilan test yozish
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda unittest kutubxonasi yordamida:
 - Test klassi yaratish
 - assertEqual, assertTrue, assertIn kabi metodlar
 - Test holatlarini yozish va bajarish
 - Amaliy mashq: funksiya test qilish
"""

import unittest

# Test qilinadigan funksiya


def kvadrat(son):
    return son * son


def salom_ber(ism):
    return f"Salom, {ism.title()}!"


class TestKvadratFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(kvadrat(3), 9)
        self.assertEqual(kvadrat(10), 100)

    def test_negative_numbers(self):
        self.assertEqual(kvadrat(-4), 16)
        self.assertEqual(kvadrat(-1), 1)

    def test_zero(self):
        self.assertEqual(kvadrat(0), 0)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            kvadrat("test")
        with self.assertRaises(TypeError):
            kvadrat([1, 2])
        with self.assertRaises(TypeError):
            kvadrat(None)


class TestSalomBerFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(salom_ber("ali"), "Salom, Ali!")
        self.assertEqual(salom_ber("vali"), "Salom, Vali!")

    def test_case_insensitivity(self):
        self.assertEqual(salom_ber("ALi"), "Salom, Ali!")
        self.assertEqual(salom_ber("VaLi"), "Salom, Vali!")

    def test_includes_salom(self):
        self.assertIn("Salom", salom_ber("ali"))

    def test_invalid_types(self):
        with self.assertRaises(AttributeError):
            salom_ber(123)
        with self.assertRaises(AttributeError):
            salom_ber(None)
        with self.assertRaises(AttributeError):
            salom_ber(["ali"])


class TestMyFunctions(unittest.TestCase):
    def test_kvadrat(self):
        self.assertEqual(kvadrat(2), 4)
        self.assertEqual(kvadrat(-3), 9)
        self.assertNotEqual(kvadrat(5), 20)

    def test_salom_ber(self):
        self.assertEqual(salom_ber("ali"), "Salom, Ali!")
        self.assertIn("Salom", salom_ber("vali"))

    def test_kvadrat_types(self):
        with self.assertRaises(TypeError):
            kvadrat("ikki")
        with self.assertRaises(TypeError):
            kvadrat([2])

    def test_salom_ber_types(self):
        with self.assertRaises(AttributeError):
            salom_ber(123)
        with self.assertRaises(AttributeError):
            salom_ber(None)

    def test_kvadrat_zero(self):
        self.assertEqual(kvadrat(0), 0)

    def test_salom_ber_case(self):
        self.assertEqual(salom_ber("ALi"), "Salom, Ali!")
        self.assertEqual(salom_ber("VaLi"), "Salom, Vali!")


if __name__ == '__main__':
    unittest.main()
