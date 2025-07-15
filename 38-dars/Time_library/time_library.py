"""
14-dars: Python time kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda time kutubxonasi yordamida:
 - Vaqtni olish (time.time, time.ctime)
 - Kutish (time.sleep)
 - Kichik taymer va vaqt o‘lchov dasturi
 - Qo‘shimcha amaliy mashqlar
"""

import time

# Joriy vaqt (sekundlarda 1970 yildan boshlab)
print("time.time():", time.time())

# O‘qiladigan holatdagi vaqt
print("time.ctime():", time.ctime())

# Kutish funksiyasi
print("3 soniya kuting...")
time.sleep(3)
print("Davom etamiz!")

# Amaliyot: operatsiya vaqtini o‘lchash
t0 = time.time()
for i in range(1_000_000):
    i ** 2
print("Ish vaqti:", round(time.time() - t0, 4), "sekund")

# Amaliyot: oddiy taymer


def taymer(sekund):
    while sekund:
        print(f"Qolgan vaqt: {sekund} s", end="\r")
        time.sleep(1)
        sekund -= 1
    print("\n⏰ Vaqt tugadi!")


taymer(5)

# Qo‘shimcha amaliy mashq 1: Rejalashtirilgan xabar
print("5 soniyadan so‘ng xabar chiqadi...")
time.sleep(5)
print("📢 Endi xabar chiqarildi!")

# Qo‘shimcha amaliy mashq 2: 10 soniyalik progress indikator


def progress_bar(sekund):
    for i in range(sekund):
        print(f"[{i+1}/{sekund}] Kuting...", end="\r")
        time.sleep(1)
    print("\n✅ Tayyor!")


progress_bar(10)

# Qo‘shimcha amaliy mashq 3: Har 2 sekundda salom chiqarish (5 marta)
for i in range(5):
    print(f"{i+1}. Salom!")
    time.sleep(2)
