import unittest
from user import User


class TestUser(unittest.TestCase):
    def test_create_valid_user(self):
        """Foydalanuvchini to'g'ri yaratish"""
        user1 = User("johndoe", "john@example.com", "123456")
        self.assertEqual(user1.username, "johndoe")
        self.assertEqual(user1.email, "john@example.com")
        self.assertTrue(user1.check_password("123456"))
        self.assertFalse(user1.confirmed)

    def test_invalid_email(self):
        """Noto'g'ri email formatini tekshirish"""
        with self.assertRaises(ValueError):
            User("janedoe", "janegmail.com", "pass")

    def test_password_is_hidden(self):
        """Parolni tekshirish"""
        user2 = User("ali", "ali@mail.com", "secret")
        self.assertFalse(hasattr(user2, 'password'))
        self.assertTrue(user2.check_password("secret"))

    def test_email_update_and_confirm(self):
        """Foydalanuvchi emailini yangilash va tasdiqlash"""
        user3 = User("mary", "mary@mail.com", "qwerty")
        user3.update_email("new@mail.com")
        self.assertEqual(user3.email, "new@mail.com")
        self.assertFalse(user3.confirmed)
        user3.confirm_email()
        self.assertTrue(user3.confirmed)

    def test_delete_account(self):
        """Foydalanuvchi hisobini o'chirish"""
        user4 = User("bob", "bob@mail.com", "abc123")
        user4.delete_account()
        self.assertIsNone(user4.username)
        self.assertIsNone(user4.email)
        self.assertIsNone(user4._password)
        self.assertFalse(user4.confirmed)

    def test_update_email_with_invalid(self):
        user = User("test", "test@mail.com", "pass")
        with self.assertRaises(ValueError):
            user.update_email("notanemail")

    def test_wrong_password_check(self):
        user = User("alice", "alice@mail.com", "mypassword")
        self.assertFalse(user.check_password("wrongpass"))

    def test_str_method(self):
        """User klassining __str__ methodini tekshirish"""
        user5 = User("Anvar", "anvar@gmail.com", "anvar1995")
        user5.confirm_email()
        self.assertEqual(
            str(user5), "User: Anvar, Email: anvar@gmail.com, Confirmed: True")
        user5.delete_account()
        self.assertEqual(
            str(user5), "User: None, Email: None, Confirmed: False")


if __name__ == "__main__":
    unittest.main()
