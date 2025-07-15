import unittest
from circle import getPerimeter, getArea


class TestCircle(unittest. TestCase):
    def test_getArea(self):
        # circle = getArea(5)
        # self.assertEqual(circle, 78.53975)
        # Shortcut for the above
        self.assertAlmostEqual(getArea(5), 78.53975)

    def test_getPerimeter(self):
        circle = getPerimeter(5)
        self.assertAlmostEqual(circle, 31.4159)


if __name__ == '__main__':
    unittest.main()
