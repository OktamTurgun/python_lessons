# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

# Variant - 1
# num1 = float(input("Birinchi sonni kiriting: \n>>>"))
# num2 = float(input("Ikkinchi sonni kiriting: \n>>>"))

# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")
# print(f"{num1} / {num2} = {num1 / num2}")

# Variant -2 Xatolarni boshqaring - try-except bloklaridan foydalaning
try:
  number1 = float(input("Bitinchi sonni kiriting: \n>>>"))
  number2 = float(input("Ikkinchi sonni kiriting: \n>>>"))

  print(f"{number1}+{number2} ={number1 + number2}")
  print(f"{number1}-{number2} ={number1 - number2}")
  print(f"{number1}*{number2} ={number1 * number2}")
  print(f"{number1}/{number2} ={number1 / number2}")
except ValueError:
  print("Iltimos, faqat raqam kiriting!")
except ZeroDivisionError:
  print("Nol(0)ga bo'lish mumkin emas!")