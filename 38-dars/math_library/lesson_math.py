"""
Created on Sat Jun 28 11:35:45 2025. Sana: 2025-06-28

38-dars. PYTHON KUTUBXONASI (01-dars: Python math kutubxonasi)

Muallif: Uktam Turgunov

Ushbu darsda biz math kutubxonasining eng muhim funksiyalarini o'rganamiz:
 - Pi va E konstantalari
 - Ildiz, daraja, modul
 - Trigonometrik funksiyalar
 - Yaxlitlash funksiyalari
 - Logarifmlar
"""

import math

PI = math.pi
# print(f"PI ning qiymati: {PI}")

E = math.e
# print(f"E ning qiymati: {E}")

# # Trigonometric funksiyalar
sinus = math.sin(PI / 2)
# print(f"Sinus(PI/2): {sinus}")

kosinus = math.cos(0)
# print(f"Kosinus(0): {kosinus}")

tangens = math.tan(PI / 4)
# print(f"Tangens(PI/4): {tangens}")

# # Radianlar va burchaklar orasida konvertatsiya
radian = math.radians(90)
# print(f"90 daraja radianlarda: {radian}")
daraja = math.degrees(math.pi/2)
# print(f"PI radian darajalarda: {daraja}")

# # Logarifmlar
logarifm = math.log(100, 10)
# print(f"Logaririfm 100 ning 10 asosida logarifmi: {logarifm}")

# # Natural logarifm
math.log(5)  # Chiqish: 1.6094379124341003
# 10 asosli lagorifm
lagorifm_10 = math.log10(100)  # Chiqish: 2.0

nat_logarifm = math.log(20)  # Chiqish: 2.995732173547877
# print(f"Natural logarifm 20 ning logarifmi: {nat_logarifm}")

# # Sonlarni yaxlitlash
son = 3.14159
yaxlitlangan = round(son, 2)  # chiqish: 3.14
print(f"Yaxlitlangan son: {yaxlitlangan}")

x = 4.1
y = 4.5
yaxlitlangan_x = math.ceil(x)  # ceil() funksiyasi sonni yuqoriga yaxlitlaydi
yaxlitlangan_y = math.floor(y)  # floor() funksiyasi sonni pastga yaxlitlaydi

# round() funksiyasi sonni yaqin butun sonlarga yaxlitlaydi
yaxlitla_x = round(x)
yaxlitla_y = round(y)

# print(f"Yuqoriga yaxlitlangan {x}: {yaxlitlangan_x}")
# print(f"Pastga yaxlitlangan {y}: {yaxlitlangan_y}")
print(f"Yuqoriga yaxlitlangan {x}: {yaxlitla_x}")
print(f"Pastga yaxlitlangan {y}: {yaxlitla_y}")

# kvadrat ildiz olish
kvadrat_ildiz = math.sqrt(16)  # Chiqish: 4
# print(f"16 ning kvadrat ildizi: {kvadrat_ildiz}")

# # Daraja olish
daraja_olish = math.pow(2, 3)  # Chiqish: 8
# print(f"2 ning 3-darajasi: {daraja_olish}")

# # Modul olish
modul = math.fabs(-5)  # Chiqish: 5.0
# print(f"-5 ning modul: {modul}")

# # Faktorial hisoblash
factorial = math.factorial(5)  # Chiqish: 120
# print(f"5 ning faktoriali: {factorial}")# # Trigonometric funksiyalar

# Pi va E
print("math.pi:", math.pi)          # 3.141592...
print("math.e:", math.e)            # 2.718281...

# Ildiz va daraja
print("math.sqrt(16):", math.sqrt(16))      # 4.0
print("math.pow(2, 3):", math.pow(2, 3))    # 8.0

# Modul va faktorial
print("math.fabs(-5):", math.fabs(-5))      # 5.0
print("math.factorial(5):", math.factorial(5))  # 120

# Yaxlitlash
print("math.floor(3.7):", math.floor(3.7))   # 3
print("math.ceil(3.1):", math.ceil(3.1))     # 4
print("math.trunc(3.9):", math.trunc(3.9))   # 3

# Trigonometrik funksiyalar (radian)
print("math.sin(math.pi/2):", math.sin(math.pi/2))  # 1.0
print("math.cos(0):", math.cos(0))                # 1.0
print("math.tan(math.pi/4):", math.tan(math.pi/4))  # 1.0

# Logarifmlar
print("math.log(8, 2):", math.log(8, 2))    # 3.0
print("math.log10(100):", math.log10(100))  # 2.0
print("math.exp(2):", math.exp(2))         # e^2

# Amaliy mashq: radius 5 bo'lgan doira yuzasi


def doira_yuzasi(radius):
    return math.pi * math.pow(radius, 2)


print("Doira yuzasi (r=5):", doira_yuzasi(5))
