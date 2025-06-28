"""
Created on Fri Jun 27 23:59:14 2025

37-dars. Klasslarni tekshirish 

@author: uktam
"""
from product import Product


class Order:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Miqdor musbat bo‘lishi kerak.")
        if quantity > product.get_quantity():
            raise ValueError("Yetarli mahsulot mavjud emas.")
        product.sell(quantity)
        self.items.append((product, quantity))

    def total(self):
        return sum(product.get_price() * quantity for product, quantity in self.items)

    def summary(self):
        return [f"{product.name} x {quantity} = ${product.get_price() * quantity}" for product, quantity in self.items]
