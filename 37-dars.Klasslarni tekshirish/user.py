"""
Created on Fri Jun 27 16:28:14 2025

37-dars. Klasslarni tekshirish 

@author: uktam
"""


class User:
    def __init__(self, username, email, password):
        if '@' not in email:
            raise ValueError("Email noto'g'ri formatda!")
        self.username = username
        self.email = email
        self._password = self._hash_password(password)
        self.confirmed = False

    def _hash_password(self, password):
        return password[::-1]

    def check_password(self, password):
        return self._password == self._hash_password(password)

    def update_email(self, new_email):
        if '@' not in new_email:
            raise ValueError("Email noto‘g‘ri formatda.")
        self.email = new_email
        self.confirmed = False

    def confirm_email(self):
        self.confirmed = True

    def delete_account(self):
        self.username = None
        self.email = None
        self._password = None
        self.confirmed = False
