import unittest
from bank import BankAccount


class TestbankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("John", 10000)

    def test_initial_balance(self):
        self.assertEqual(self.account1.get_balance(), 10000)

    def test_deposit(self):
        self.account1.deposit(5000)
        self.assertEqual(self.account1.get_balance(), 15000)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account1.deposit(-1000)

    def test_withdraw(self):
        self.account1.withdraw(2000)
        self.assertEqual(self.account1.get_balance(), 8000)

    def test_over_withdraw(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(15000)

    def test_get_balance(self):
        self.account1.deposit(5000)
        self.assertEqual(self.account1.get_balance(), 15000)

    def test_str_method(self):
        self.assertEqual(str(self.account1),
                         "Bank Hisobi: John, Balans: 10000 so'm")

    def test_withdraw_all(self):
        self.account1.withdraw(10000)
        self.assertEqual(self.account1.get_balance(), 0)


if __name__ == '__main__':
    unittest.main()
