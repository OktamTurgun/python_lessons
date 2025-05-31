'''
MATH moduli fazifalari:

radius ni foydalanuvchidan so'rab, quyidagilarni hisoblang:
1. Doira yuzasi (πr²)
2. Aylana uzunligi (2πr)
Natijalarni yaxlitlab, 2 xona aniqlikda chiqaring
'''
import math
def doira_yuzasi(radius):
    """Doira yuzasini hisoblaydi"""
    if radius < 0:
        raise ValueError("Radius manfiy bo'lishi mumkin emas")
    return round(math.pi * (radius ** 2), 2)

def aylana_uzunligi(radius):
    """Aylana uzunligini hisoblaydi"""
    if radius < 0:
        raise ValueError("Radius manfiy bo'lishi mumkin emas")
    return round(2 * math.pi * radius, 2)
  
radius = float(input("Aylana radiusini kiriting: "))
print(f"{radius} radiusli doira yuzasi: {doira_yuzasi(radius)}")
print(f"{radius} radiusga teng aylana uzunligi: {aylana_uzunligi(radius)}")

# Example 2
def doira_yuzasi(radius):
    return round(math.pi * (radius ** 2), 2)

def aylana_uzunligi(radius):
    return round(2 * math.pi * radius, 2)

try:
    radius = float(input("Aylana radiusini kiriting: "))
    if radius < 0:
        print("Diqqat! Radius manfiy bo'lishi mumkin emas")
    else:
        print(f"{radius} radiusli doira yuzasi: {doira_yuzasi(radius)}")
        print(f"{radius} radiusga teng aylana uzunligi: {aylana_uzunligi(radius)}")
except ValueError:
    print("Xato: Iltimos, faqat raqam kiriting (masalan: 5 yoki 7.25)")
