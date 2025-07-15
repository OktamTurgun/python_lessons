"""
Mavzu: Practice.
Muallif: Uktam Turgunov
Sana: 2025-07-07
"""
# Vazifa: 1 Username Generator
import random


def user_name():
    """Username generatsiya qiluvchi funksiya"""
    ism = input("Ismingizni kiriting: ")
    teskari_ism = ism[::-1]
    taxminiy_son = random.randint(0, 9)
    username = teskari_ism + str(taxminiy_son)
    print(f"Siz uchun generatsiya qilingan yangi ism: {username}")


user_name()

# Vazifa: 2 Vazifa 2: String to Integers.


def convert_add(royxat):
    """String ro'yxatini sonlarga aylantirib, yig'indini hisoblovchi funksiya"""
    sonlar = []
    for son in royxat:
        sonlar.append(int(son))
        jami = sum(sonlar)
    return jami


print(convert_add(['1', '2', '3']))
