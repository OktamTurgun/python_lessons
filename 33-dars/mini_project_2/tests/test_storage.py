import unittest
from manager.product import Mahsulot
from manager.storage import save_mahsulotlar, load_mahsulotlar
import os

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.test_data = [Mahsulot("Test", 1234)]
        save_mahsulotlar(self.test_data)

    def tearDown(self):
        if os.path.exists("data/mahsulotlar.pkl"):
            os.remove("data/mahsulotlar.pkl")

    def test_load_save(self):
        result = load_mahsulotlar()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].nomi, "Test")
        self.assertEqual(result[0].narxi, 1234)

if __name__ == '__main__':
    unittest.main()