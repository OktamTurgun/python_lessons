"""
11-dars: Python getpass kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda getpass kutubxonasi yordamida:
 - Foydalanuvchidan yashirin parol kiritishni
 - Oddiy input() bilan farqini
 - Login tizimi kabi real amaliyotda qo‘llashni o‘rganamiz.
"""

import getpass

# Oddiy input bilan farq
foydalanuvchi = input("Foydalanuvchi nomi: ")
parol = getpass.getpass("Parol: ")

# Parolni tekshirish
if parol == "123456":
    print(f"Xush kelibsiz, {foydalanuvchi}!")
else:
    print("⚠️ Noto‘g‘ri parol!")

# Diqqat: getpass faqat terminal/konsolda ishlaydi!
# Jupyter Notebook yoki GUI muhitda xatolik beradi
