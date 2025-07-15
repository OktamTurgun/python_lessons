import unittest
from car_klass import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota Camry", 2020, "oq")

    def test_info(self):
        self.assertEqual(self.car.info(), "2020 yildagi oq Toyota Camry")

    def test_repaint(self):
        self.car.repaint("qora")
        self.assertEqual(self.car.rang, "qora")
        self.assertEqual(self.car.info(), "2020 yildagi qora Toyota Camry")

    def test_age(self):
        self.assertEqual(self.car.age(2024), 4)
        self.assertEqual(self.car.age(2020), 0)

    def test_is_color(self):
        self.assertTrue(self.car.is_color("oq"))
        self.assertTrue(self.car.is_color("OQ"))
        self.assertFalse(self.car.is_color("qora"))
        self.car.repaint("qora")
        self.assertTrue(self.car.is_color("qora"))


if __name__ == '__main__':
    unittest.main()
