"""
Mavzu: Practice with files.
Muallif: Uktam Turgunov
Sana: 2025-07-08

Vazifa 1: fayllar bilan ishlash
open, read, write, with:

Vazifa:
Foydalanuvchidan ism va sharf so‘rab, feedback.txt faylga qo‘shib yozish.
"""

ism = input("Ismingizni kiriting:  ")
familiya = input("Familiyangizni kiriting: ")

with open("feedback.txt", 'w') as file:
    file.write(", ".join([ism, familiya]))

# Yaxshi amaliyot uchun xar safar 'w' bilan faylni qaytadan yozmasdan 'a' bilan
# Bu har bir foydalanuvchining ism-sharifini yangi qatordan qo‘shib boradi.
# with open("feedback.txt", 'w', encoding="utf-8") as file:
#     file.write(f"{ism} {familiya}")

# print("✅ Feedback saqlandi!")

with open("feedback.txt", 'r') as file:
    ism_sharif = file.read()
print(f"foydalanuvchi ism sharfi: {ism_sharif}")

# Exercise: 2


def feedback_qoshish():
    ism = input("Ismingizni kiriting:  ")
    familiya = input("Familiyangizni kiriting: ")

    with open("feedback.txt", 'a', encoding="utf-8") as file:
        file.write(f"{ism} {familiya}\n")

    print("✅ Feedback saqlandi!")


def feedback_oqish():
    with open("feedback.txt", 'r', encoding="utf-8") as file:
        print("📋 Barcha feedbacklar:")
        print(file.read())


feedback_qoshish()
feedback_oqish()
