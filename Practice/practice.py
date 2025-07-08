"""
Mavzu: Practice.
Muallif: Uktam Turgunov
Sana: 2025-07-05

Vazifa 1: Username Generator
Username generatsiya qiluvchi user_name nomli funksiyani yozing.
Funksiya foydalanuvchidan ismini so’rashi kerak.
Keyin funksiya kiritilgan ismni teskari o’girib, uning oxiriga 0 dan 9 gacha bo’lgan ixtiyoriy sonni qo’shsin.
Oxirida funksiya foydalanuvchiga usernameni qaytarsin.

Misol:
Ismingizni kiriting: Toshmat
Sizning uchun generatsiya qilingan username: tamhsot2.

Vazifa 2: String to Integers.
Convert_add degan funksiya yasang, u orqali kiritilgan stringlar 
listini ([‘1’, ‘3’, ‘5’])  integerga o’tkazib ([1, 3, 5]), summasi hisoblansin (9).

Bir qatorda ishlashga harakat qiling.

"""
# Vazifa: 1
import random


def generate_username():
    """
    Foydalanuvchiga o'z ismini kiritishni taklif qiladi, kiritilgan nomni teskari o'zgartirish orqali foydalanuvchi nomini yaratadi
    va tasodifiy raqamni (0-9) qo'shib, keyin yaratilgan foydalanuvchi nomini chop etadi.
    """

    name = input("Ismingizni kiriting: ")
    reversed_name = name[::-1]
    random_num = random.randint(0, 9)
    username = reversed_name + str(random_num)
    print(f"Siz uchun ganeratsiya qilingan username: {username}")


# Vazifa: 2
def convert_add(str_list):
    """
    Stringlardan iborat ro'yxatni butun songa o'zgartirib, ularning yig'indisini qaytaradi.

    Argumentlar:
      list (str ro'yxati): Raqamli stringlardan iborat ro'yxat.

    Natija:
      int: O'zgartirilgan sonlarning yig'indisi.

    Xatoliklar:
      ValueError: Agar ro'yxatdagi biror element butun songa o'zgartirib bo'lmasa.
    """
    return sum(map(int, str_list))


if __name__ == "__main__":
    generate_username()

    list = ['1', '2', '3', '4']
    print(convert_add(list))
