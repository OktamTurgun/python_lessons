"""
Mavzu: Practice. (Username Generator)
Muallif: Uktam Turgunov
Sana: 2025-07-05
Vazifa:
Username generatsiya qiluvchi user_name nomli funksiyani yozing.

Funksiya foydalanuvchidan ismini so’rashi kerak.

Keyin funksiya kiritilgan ismni teskari o’girib, uning oxiriga 0 dan 9 gacha bo’lgan ixtiyoriy sonni qo’shsin.

Oxirida funksiya foydalanuvchiga usernameni qaytarsin.

Misol:
Ismingizni kiriting: Toshmat
Sizning uchun generatsiya qilingan username: tamhsot2
"""
import random


def gernerate_username():
    """
    Foydalanuvchiga o'z ismini kiritishni taklif qiladi, kiritilgan nomni teskari o'zgartirish orqali foydalanuvchi nomini yaratadi
    va tasodifiy raqamni (0-9) qo'shib, keyin yaratilgan foydalanuvchi nomini chop etadi..
    Returns:
        None
    """

    name = input("Ismingizni kiriting: ")
    reversed_name = name[::-1]
    random_num = random.randint(0, 9)
    username = reversed_name + str(random_num)
    print(f"Siz uchun ganeratsiya qilingan username: {username}")


if __name__ == "__main__":
    gernerate_username()
