
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur

# Variant - 1
# son = int(input('Istalgan son kiriting: \n>>>'))
# print(f"{son} ning kvadrati {son**2} ga teng")
# print(f"{son} ning kubi {son**3} ga teng")

# Kodni bir qatorda yozish uchun
# print(f"{son} ning kvardrati {son**2} ga, kubi {son**3} ga teng")

# Variant - 2

try:
  number = int(input("Istalgan son kiriting: \n>>>"))
  print(f"{number} ning kvardrati {number**2} ga, kubi {number**3} ga teng")
except ValueError:
  print('Faqat butun son kiriting!')  