"""
Created on Wed Jun 28 07:21:14 2025

37-dars. Klasslarni tekshirish 

@author: uktam
"""


class Cart:
    """ Savatcha klassi"""

    def __init__(self):
        self.items = {}

    def add(self, product, quantity):
        """Savatchaga maxsulot qo'shish"""
        if quantity <= 0:
            raise ValueError("Miqdor musbat bo'lishi kerak!")
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove(self, product):
        """savatchadan maxsulot olib tashlash"""
        if product in self.items:
            del self.items[product]
        else:
            raise ValueError("Maxsulot savatchada yo'q!")

    def update(self, product, quantity):
        """savatchadagi maxsulot miqdorini yangilash"""
        if quantity < 0:
            raise ValueError("Miqdor manfiy bo'lishi mumkin emas!")
        if product not in self.items:
            raise ValueError("Maxsulot savatchada yo'q!")
        if quantity == 0:
            self.remove(product)
        else:
            self.items[product] = quantity

    def total_items(self):
        """Savatchadagi jami maxsulotlar soni"""
        return sum(self.items.values())

    def clear(self):
        """Savatchani tozalash"""
        self.items.clear()
