"""
Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring
 va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
"""
num1 = float(input("1-sonni kiriting: "))
num2 = float(input("2-sonni kiriting: "))
if num1 == num2:
  print(f"{num1}={num2}")
elif num1 > num2:
  print(f"{num1}>{num2}")
else:
  print(f"{num1}<{num2}")

"""Ternary operator yordamida xa codni yanaqa qisqaroq yozish mumkin"""

num1, num2 = float(input("1-sonni kiriting: ")), float(input("2-sonni kiriting: "))
print(f"{num1}={num2}" if num1 == num2 else f"{num1}>{num2}" if num1 > num2 else f"{num1}<{num2}")
