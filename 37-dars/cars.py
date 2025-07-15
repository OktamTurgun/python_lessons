"""
Created on Wed Jun 26 10:00:14 2025

37-dars. Klasslarni tekshirish 

@author: uktam
"""


class Car:
    def __init__(self, make, model, year, km=0, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.__km = km
        self.price = price

    def set_price(self, other_price):
        self.price = other_price

    def add_km(self, new_km):
        if new_km >= 0:
            self.__km += new_km
            print(f"{new_km} km qo'shildi. Jami km: {self.__km}")
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas!")

    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}, "
        info += f"{self.year}-yil, {self.__km} km yurgan. "
        if self.price:
            info += f"Narh: {self.price}"
        return info

    def get_km(self):
        return self.__km


# avto1 = Car('gm', 'malibu', 2024)
# print(avto1.get_info())       # GM Malibu, 2024-yil, 0 km yurgan.
# print(avto1.get_km())         # 0 km
# print(avto1.add_km(5000))     # 5000 km qo'shildi. Jami km: 5000
# print(avto1.get_info())       # GM Malibu, 2024-yil, 5000 km yurgan.
# print(avto1.add_km(-1000))    # ValueError: km manfiy bo'lishi mumkin emas!
