# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur

# variant - 1
# age = int(input("Yoshingiz nechchida? \n>>>"))
# year = 2025 - age
# print(f"Siz {year} - da tug'ilgansiz!")

# Variant - 2
try:
  age1 = int(input("Yoshingiz nechchida? \n>>>"))
  current_year = 2025
  birth_year = current_year - age1
  print(f"Siz {birth_year}-da tug'ilgansiz!")
except ValueError:
  print("Iltimos, faqat raqam kiriting!")
