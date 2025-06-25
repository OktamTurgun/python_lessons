"""
Fayl mavjudligini tekshiruvchi dastur yozing. Agar fayl mavjud bo'lmasa, yangi fayl yaratilsin.
"""
# Exercise: 1
import os
# filename = 'data.txt'

# try:
#     # Faylni o'qishga urinish
#     with open(filename, 'r') as file:
#         text = file.read()
#     print("Fayl mavjud. Fayl tarkibi:")
#     print(text)

# except FileNotFoundError:
#     print("Fayl mavjud emas. Yangi fayl yaratilmoqda...")

#     # Yangi fayl yaratish va unga boshlang'ich ma'lumot yozish
#     with open(filename, 'w') as file:
#         file.write("Bu yangi yaratilgan fayl\n")
#     print(f"'{filename}' fayli muvaffaqiyatli yaratildi!")

# Exercise: 2
filename = input("Fayl nomini kiriting (masalan: data.txt): ") or 'data.txt'

if os.path.exists(filename):
    print(f"\n'{filename}' fayli mavjud. Tarkibi:")
    with open(filename, 'r') as file:
        print(file.read())
else:
    print(f"\n'{filename}' fayli mavjud emas. Yangi fayl yaratilmoqda...")

    content = input("Faylga yozish uchun matn kiriting (ixtiyoriy): ")

    with open(filename, 'w') as file:
        file.write(content if content else "Fayl yaratildi: " + filename)

    print(f"'{filename}' fayli muvaffaqiyatli yaratildi!")
