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

# Trigonometrik funksiyalar
print("Sinus(PI/2):", math.sin(PI / 2))      # 1.0
print("Kosinus(0):", math.cos(0))            # 1.0
print("Tangens(PI/4):", math.tan(PI / 4))    # 1.0

# Radianlar va burchaklar orasida konvertatsiya
print("90 daraja radianlarda:", math.radians(90))      # 1.570796...
print("PI radian darajalarda:", math.degrees(math.pi/2))  # 90.0

# Logarifmlar
print("Logarifm 100 ning 10 asosida:", math.log(100, 10))  # 2.0
print("Natural logarifm 20:", math.log(20))                # 2.9957...
print("10 asosli logarifm 100:", math.log10(100))          # 2.0

# Sonlarni yaxlitlash
son = 3.14159
print(f"Yaxlitlangan son (2 xonali): {round(son, 2)}")     # 3.14
x = 4.1
y = 4.5
print(f"Yuqoriga yaxlitlangan {x}: {math.ceil(x)}")         # 5
print(f"Pastga yaxlitlangan {y}: {math.floor(y)}")          # 4
print(f"Yaqin butun son {x}: {round(x)}")                   # 4
print(f"Yaqin butun son {y}: {round(y)}")                   # 4

# Kvadrat ildiz va daraja
x = 81
y = math.sqrt(x)
print("81 ning kvadrat ildizi:", y)  # 81 ning kvadrat ildizi: 9.0

print("16 ning kvadrat ildizi:", math.sqrt(16))             # 4.0
print("2 ning 3-darajasi:", math.pow(2, 3))                 # 8.0

# Daraja oshirish
n = 5
print("n ning kubi:", math.pow(n, 3))                      # n ning kubi: 125.0
# n ning 5-darajasi: 3125.0
print("n ning 5-darajasi:", math.pow(n, 5))
# n dan kub ildiz: 1.7099759466766968
print("n dan kub ildiz:", math.pow(n, 1/3))
print("3 ning 4-darajasi:", math.pow(3, 4))                # 81.0
print("5 ning 2-darajasi:", math.pow(5, 2))                # 25.0
print("10 ning 0-darajasi:", math.pow(10, 0))              # 1.0
print("2 ning 10-darajasi:", math.pow(2, 10))              # 1024.0

# Modul va faktorial
print("-5 ning moduli:", math.fabs(-5))                     # 5.0
print("5 ning faktoriali:", math.factorial(5))              # 120

# Pi va E konstantalari
print("math.pi:", math.pi)                                  # 3.141592...
print("math.e:", math.e)                                    # 2.718281...

# Yaxlitlash funksiyalari
print("math.floor(3.7):", math.floor(3.7))                  # 3
print("math.ceil(3.1):", math.ceil(3.1))                    # 4

#  bu Python matematik modulidagi funksiya bo‘lib, berilgan sonning butun qismini
#  qaytaradi (ya’ni, kasr qismini olib tashlaydi). U sonni nolga tomon yaxlitlaydi.
print("math.trunc(3.9):", math.trunc(3.9))                  # 3

# Trigonometrik funksiyalar (radian)
print("math.sin(math.pi/2):", math.sin(math.pi/2))          # 1.0
print("math.cos(0):", math.cos(0))                         # 1.0
print("math.tan(math.pi/4):", math.tan(math.pi/4))          # 1.0

# Logarifmlar
print("math.log(8, 2):", math.log(8, 2))                   # 3.0
print("math.log10(100):", math.log10(100))                 # 2.0
print("math.exp(2):", math.exp(2))                         # e^2

# Faktorial hisoblash
print("math.factorial(0):", math.factorial(0))   # 1
print("math.factorial(1):", math.factorial(1))   # 1
print("math.factorial(3):", math.factorial(3))   # 6
print("math.factorial(6):", math.factorial(6))   # 720

# Amaliy mashq: radius 5 bo'lgan doira yuzasi


def doira_yuzasi(radius):
    return math.pi * math.pow(radius, 2)


print("Doira yuzasi (r=5):", doira_yuzasi(5))
