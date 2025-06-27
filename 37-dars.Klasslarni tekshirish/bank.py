"""
Created on Fri Jun 27 15:07:14 2025

37-dars. Klasslarni tekshirish 

@author: uktam
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit miqdori musbat bo'lishi kerak.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Hisobda yetarli mablag' yo'q.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
