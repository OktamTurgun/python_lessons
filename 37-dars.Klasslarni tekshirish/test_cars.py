# import unittest
# from cars import Car


# class TestCar(unittest.TestCase):
#     """Car classini tekshirish uchun test"""

#     def setUp(self):
#         make = "GM"
#         model = "Malibu"
#         year = 2024
#         self.km = 5000
#         self.price = 40000
#         self.avto1 = Car(make, model, year)
#         self.avto2 = Car(make, model, year, price=self.price)

#     def test_create(self):
#         # Qiymatlar mavjudligini assertIsNotNone methodi bilan tekshirish
#         self.assertIsNotNone(self.avto1.make)
#         self.assertIsNotNone(self.avto1.model)
#         self.assertIsNotNone(self.avto1.year)
#         # Qiyamat mavjudamsligini assertIsNone methodi bilan tekshirish
#         self.assertIsNone(self.avto1.price)
#         # Qiymat tengligini assertEquals methodi bilan tekshirish
#         self.assertEqual("0 km", self.avto1.get_km())
#         # avto2 narhini tekshiramiz
#         self.assertEqual(self.price, self.avto2.price)

# def test_set_price(self):
#   new_price = 45000
#   self.avto2.set_price(new_price)

import unittest
from cars import Car


class TestCar(unittest.TestCase):
    """Car klassini test qilish"""

    def setUp(self):
        make = "GM"
        model = "Malibu"
        year = 2024
        self.km = 5000
        self.price = 40000
        self.avto1 = Car(make, model, year)
        self.avto2 = Car(make, model, year, price=self.price)

    def test_create(self):
        """Obyekt yaratish testi"""
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        self.assertIsNone(self.avto1.price)
        self.assertEqual(0, self.avto1.get_km())
        self.assertEqual(self.price, self.avto2.price)

    def test_set_price(self):
        """Narh belgilash testi"""
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(self.avto2.price, new_price)
        self.assertEqual(new_price, self.avto2.price)

    def test_add_km(self):
        """KM qo‘shish testi"""
        # Musbat qiymat berib ko'ramiz
        self.avto1.add_km(1500)
        self.assertEqual(self.avto1.get_km(), 1500)
        self.avto2.add_km(self.km)
        self.assertEqual(self.km, self.avto2.get_km())
        self.avto1.add_km(1500)
        self.assertEqual(3000, self.avto1.get_km())
        # manfiy qiymat berib ko'ramiz
        new_km = -2000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

    def test_add_negative_km(self):
        """Manfiy KM xatolik testi"""
        with self.assertRaises(ValueError):
            self.avto1.add_km(-100)

    def test_get_info(self):
        """Avto haqida ma’lumot testi"""
        self.avto2.add_km(3000)
        expected_info = "GM Malibu, 2024-yil, 3000 km yurgan. Narh: 40000"
        self.assertEqual(self.avto2.get_info(), expected_info)


if __name__ == '__main__':
    unittest.main()
