"""
Mavzu: Practice with OOP.
Muallif: Uktam Turgunov
Sana: 2025-07-10

Vazifa: sinflar yozishni boshlash.
BankAccount klassi: balans, depozit, yechib olish.
"""


class BankAccount:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        self.balans = balans

    def balans_korish(self):
        print(f"💰 {self.egasi}ning balansida: {self.balans} so‘m")

    def depozit(self, summa):
        self.balans += summa
        print(f"✅ {summa} so‘m qo‘shildi.")

    def yechish(self, summa):
        if summa <= self.balans:
            self.balans -= summa
            print(f"💸 {summa} so‘m yechildi.")
        else:
            print("🚫 Mablag‘ yetarli emas!")

    def hisob_raqamini_ozgartirish(self, yangi_egasi):
        self.egasi = yangi_egasi
        print(f"Hisob egasi {yangi_egasi} ga o‘zgartirildi.")


# 📋 Ishlatish:
acc1 = BankAccount("Ali", 100000)
acc1.balans_korish()
acc1.depozit(50000)
acc1.yechish(120000)
acc1.balans_korish()
acc1.hisob_raqamini_ozgartirish("Valijon")
