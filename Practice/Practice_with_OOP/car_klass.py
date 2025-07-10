"""
Mavzu: Practice with files.
Muallif: Uktam Turgunov
Sana: 2025-07-10

Vazifa 1: fayllar bilan ishlash
open, read, write, with:

Vazifa: sinflar yozishni boshlash.
Car klassi: model, yil, rang va metodlari.

User klassi: ism, email va metodlari (masalan, emailni tekshiruvchi).

BankAccount klassi: balans, depozit, yechib olish.
"""


class Car:
    def __init__(self, model, yil, rang):
        self.model = model
        self.yil = yil
        self.rang = rang

    def info(self):
        return f"{self.yil} yildagi {self.rang} {self.model}"

    def repaint(self, yangi_rang):
        old_rang = self.rang
        self.rang = yangi_rang
        print(f"🚗 {self.model} {old_rang} rangdan {yangi_rang} rangga bo‘yaldi!")

    def age(self, current_year):
        """Mashinaning yoshini hisoblaydi."""
        return current_year - self.yil

    def is_color(self, color):
        """Mashina rangini tekshiradi."""
        return self.rang.lower() == color.lower()


# 📋 Ishlatish:
car1 = Car("Toyota Camry", 2020, "oq")
print(car1.info())
car1.repaint("qora")
print(car1.info())
