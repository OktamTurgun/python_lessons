"""
Faylga O'zimiz Belgilangan Ma'lumotlarni Yozish
Agar foydalanuvchidan input soramasdan, to'g'ridan-to'g'ri o'zingiz 
belgilangan ma'lumotlarni (ro'yxat, lug'at, tuple yoki to'plam) 
faylga yozmoqchi bo'lsangiz, quyidagi usullardan foydalanishingiz mumkin:
"""

# 1. Ro'yxat (List) ni faylga yozish
import os
import json

filename = input("Fayl nomini kiriting (masalan: data.txt): ") or 'data.txt'

if os.path.exists(filename):
    print(f"\n'{filename}' fayli mavjud. Tarkibi:")
    with open(filename, 'r') as file:
        print(file.read())
else:
    print(f"\n'{filename}' fayli mavjud emas. Yangi fayl yaratilmoqda...")

    # Ro'yxat yaratamiz
    my_list = ["Python", "Java", "C++", "JavaScript"]

    with open(filename, 'w') as file:
        # Variant 1: Oddiy yozish
        file.write("\n".join(my_list))

        # Variant 2: JSON formatida
        # json.dump(my_list, file)

    print(f"'{filename}' fayli muvaffaqiyatli yaratildi!")

# 2. Lug'at (Dict) ni faylga yozish
# else:
    print(f"\n'{filename}' fayli mavjud emas. Yangi fayl yaratilmoqda...")

    # Lug'at yaratamiz
    my_dict = {"name": "John", "age": 30, "city": "New York"}

    with open(filename, 'w') as file:
        # Variant 1: Oddiy yozish
        for key, value in my_dict.items():
            file.write(f"{key}: {value}\n")

        # Variant 2: JSON formatida
        # json.dump(my_dict, file, indent=4)

# 3. Tuple yoki Set ni faylga yozish
# else:
    print(f"\n'{filename}' fayli mavjud emas. Yangi fayl yaratilmoqda...")

    # Tuple yaratamiz
    my_tuple = ("apple", "banana", "cherry")
    # Yoki Set
    my_set = {"red", "green", "blue"}

    with open(filename, 'w') as file:
        # Tuple uchun
        file.write("\n".join(my_tuple))

        # Set uchun
        # file.write("\n".join(my_set))
# 4. Har xil ma'lumot turlarini aralash yozish
# else:
    print(f"\n'{filename}' fayli mavjud emas. Yangi fayl yaratilmoqda...")

    # Turli ma'lumotlar
    data = {
        "name": "Alice",
        "skills": ["Python", "SQL", "Django"],
        "age": 25,
        "is_active": True,
        "projects": {"project1": "E-commerce", "project2": "Blog"}
    }

    with open(filename, 'w') as file:
        # JSON formatida saqlash eng qulay
        json.dump(data, file, indent=4)

# Muhim maslahatlar:
# JSON formatida saqlash - Agar murakkab ma'lumotlarni saqlamoqchi bo'lsangiz, json modulidan foydalaning.

# Matn formatida saqlash - Agar oddiy matn sifatida ko'rish kerak bo'lsa, .join() metodidan foydalaning.

# Fayl formati - Ma'lumot turiga qarab .txt yoki .json kengaytmalaridan foydalaning.

# Indentatsiya - JSON fayllarida indent=4 parametri chiroyli formatlash uchun ishlatiladi.
