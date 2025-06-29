"""
10-dars: Python json kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda json kutubxonasi yordamida quyidagilarni o‘rganamiz:
 - Python obyektlarini JSON formatiga o‘girish
 - JSON formatidagi matnni Python obyektiga aylantirish
 - JSON faylga yozish va fayldan o‘qish
"""

import json

# Python dict -> JSON matn (dump)
mahsulot = {
    "nom": "Olma",
    "narx": 12000,
    "mavjud": True,
    "miqdor": 50
}

json_matn = json.dumps(mahsulot, indent=4, ensure_ascii=False)
print("JSON matn:\n", json_matn)

# JSON matn -> Python dict (load)
python_dict = json.loads(json_matn)
print("Python dict:", python_dict)

# JSON faylga yozish
with open("mahsulot.json", "w", encoding="utf-8") as f:
    json.dump(mahsulot, f, indent=4, ensure_ascii=False)

# JSON fayldan o‘qish
with open("mahsulot.json", "r", encoding="utf-8") as f:
    malumot = json.load(f)
    print("Fayldan o‘qilgan ma’lumot:", malumot)

# Amaliy mashq: Talaba ro‘yxatini JSON faylga saqlash va qayta o‘qish
talabalar = [
    {"ism": "Ali", "yosh": 20},
    {"ism": "Laylo", "yosh": 21}
]

with open("talabalar.json", "w", encoding="utf-8") as f:
    json.dump(talabalar, f, indent=2, ensure_ascii=False)

with open("talabalar.json", "r", encoding="utf-8") as f:
    talabalar_oqildi = json.load(f)
    print("Talabalar ro‘yxati:", talabalar_oqildi)

# Amaliy mashq: Lug'atlar ro'yxatini JSON faylga yozish va o'qish
lugatlar = [
    {"so'z": "kitob", "tarjima": "book"},
    {"so'z": "daraxt", "tarjima": "tree"}
]

with open("lugatlar.json", "w", encoding="utf-8") as f:
    json.dump(lugatlar, f, indent=2, ensure_ascii=False)

with open("lugatlar.json", "r", encoding="utf-8") as f:
    lugatlar_oqildi = json.load(f)
    print("Lug'atlar ro'yxati:", lugatlar_oqildi)

# Amaliy mashq: Foydalanuvchi ma'lumotlarini JSON faylga saqlash va o'qish
foydalanuvchi = {
    "ism": "Jasur",
    "email": "jasur@mail.com",
    "yosh": 25,
    "faol": True
}

with open("foydalanuvchi.json", "w", encoding="utf-8") as f:
    json.dump(foydalanuvchi, f, indent=4, ensure_ascii=False)

with open("foydalanuvchi.json", "r", encoding="utf-8") as f:
    foydalanuvchi_oqildi = json.load(f)
    print("Foydalanuvchi ma'lumoti:", foydalanuvchi_oqildi)
