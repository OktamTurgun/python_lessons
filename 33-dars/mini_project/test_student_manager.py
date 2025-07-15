# test_student_manager.py
import unittest
import os
import pickle
from student_manager import Talaba, save_students, load_students

class TestStudentManager(unittest.TestCase):
    TEST_FILE = "test_students.pkl"

    def setUp(self):
        # Testlar oldidan vaqtinchalik ma'lumotlar tayyorlash
        self.t1 = Talaba("Ali", "Valiyev", 20)
        self.t2 = Talaba("Dilnoza", "Qodirova", 22)
        self.students = [self.t1, self.t2]
        with open(self.TEST_FILE, "wb") as f:
            pickle.dump(self.students, f)

    def tearDown(self):
        # Testlardan so‘ng faylni tozalash
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_student_save_and_load(self):
        save_students(self.students)
        result = load_students()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].ism, "Ali")
        self.assertEqual(result[1].familiya, "Qodirova")

    def test_repr_format(self):
        self.assertEqual(repr(self.t1), "Ali Valiyev, 20 yosh")

if __name__ == '__main__':
    unittest.main()
