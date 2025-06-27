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


if __name__ == '__main__':
    unittest.main()
