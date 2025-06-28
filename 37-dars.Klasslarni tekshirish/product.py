"""
Created on Fri Jun 20:27:14 2025

37-dars. Klasslarni tekshirish 

@author: uktam
"""


class Product:
    def __init__(self, name, price, quantity=0):
        if price < 0:
            raise ValueError("Narh manfiy bolishi mumkin emas!")
        if quantity < 0:
            raise ValueError("Miqdor manfiy bo'lishi mumkin emas!")
        self.name = name
        self.price = price
        self.quantity = quantity

    def set_price(self, price):
        if price < 0:
            raise ValueError("Narh manfiy bolishi mumkin emas!")
        self.price = price

    def get_price(self):
        return self.price

    def update_price(self, diff):
        if self.price + diff < 0:
            raise ValueError("Yangi narh manfiy bo'lishi mumkin emas!")
        self.price += diff

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Miqdor manfiy bo'lishi mumkin emas!")
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def update_quantity(self, diff):
        if self.quantity + diff < 0:
            raise ValueError("Yangi miqdor manfiy bo'lishi mumkin emas!")
        self.quantity += diff

    def get_info(self):
        return f"{self.name} - {self.price} ({self.quantity} dona)"

    def applay_discount(self, percent):
        if not (0 <= percent <= 100):
            raise ValueError("Chagirma 0 va 100 foiz orasida bo'lishi kerak!")
        self.price *= (1 - percent / 100)

    def restock(self, amount):
        if amount <= 0:
            raise ValueError("Zaxira miqdaori musbat bo'lishi kerak!")
        self.quantity += amount

    def sell(self, amount):
        if amount <= 0:
            raise ValueError("Sotiladigan miqdor musbat bo'lishi kerak!")
        if amount > self.quantity:
            raise ValueError("Yatarli maxsulot yo'q!")
        self.quantity -= amount

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
