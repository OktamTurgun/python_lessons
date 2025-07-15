import json

"""
Mavzu: Practice with files.
Muallif: Uktam Turgunov
Sana: 2025-07-08

Vazifa 1: fayllar bilan ishlash
open, read, write, with:

Matnli faylga 10 ta ism yozish va uni o‘qib chiqarish.
"""

dostlar_ism = ["Alisher", "Gulbahor", "E'zoza", "Odina",
               "Anvar", "Jamol", "Sanjar", "Jamshid", "Lobar", "Kamola"]

with open("dostlar_ism.txt", 'w') as file:
    for ism in dostlar_ism:
        file.write(ism + '\n')
print("Mening dostlarim:")
with open("dostlar_ism.txt", 'r') as file:
    for row in file:
        print(row.strip())
    print("="*20)

# 10 ta ismni ro'yxatga olamiz
ismlar = ["Ali", "Vali", "Hasan", "Husan", "Aziz",
          "Dilshod", "Gulbahor", "Malika", "Sardor", "Diyor"]

# Faylga yozamiz
with open("ismlar.txt", "w", encoding="utf-8") as fayl:
    for ism in ismlar:
        fayl.write(ism + "\n")

# Fayldan o'qib ekranga chiqaramiz
with open("ismlar.txt", "r", encoding="utf-8") as fayl:
    for qator in fayl:
        print(qator.strip())
# Yangi usul: faylga barcha ismlarni bir qatorda yozish va o'qish
with open("ismlar_bir_qator.txt", "w", encoding="utf-8") as fayl:
    fayl.write(", ".join(ismlar))

with open("ismlar_bir_qator.txt", "r", encoding="utf-8") as fayl:
    qator = fayl.read()
    print("Bir qatorda ismlar:", qator)

# Yana bir usul: faylga ro'yxatni json formatida saqlash va o'qish

with open("ismlar.json", "w", encoding="utf-8") as fayl:
    json.dump(ismlar, fayl, ensure_ascii=False)

with open("ismlar.json", "r", encoding="utf-8") as fayl:
    ismlar_json = json.load(fayl)
    print("JSONdan o'qilgan ismlar:", ismlar_json)

# Yangi misol: Fayldan ma'lumotlarni teskari tartibda o'qish
with open("ismlar.txt", "r", encoding="utf-8") as fayl:
    qatorlar = fayl.readlines()
    print("Teskari tartibda ismlar:")
    for ism in reversed(qatorlar):
        print(ism.strip())

# Yangi misol: Fayldagi ismlarni bosh harfi bilan filtrlash (masalan, 'A' harfi)
print("A harfi bilan boshlanadigan ismlar:")
with open("ismlar.txt", "r", encoding="utf-8") as fayl:
    for ism in fayl:
        if ism.strip().startswith("A"):
            print(ism.strip())

# Yangi misol: Faylga yangi ism qo'shish (append)
yangi_ism = "Zafar"
with open("ismlar.txt", "a", encoding="utf-8") as fayl:
    fayl.write(yangi_ism + "\n")
print(f"{yangi_ism} ismi faylga qo'shildi.")
