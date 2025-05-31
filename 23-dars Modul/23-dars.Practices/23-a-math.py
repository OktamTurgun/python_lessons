'''
MATH moduli fazifalari:

1 Doira yuzasini hisoblash, aylana uzunligini hisoblash

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

'''
2 Kvadrat tenglama yechimini topish

a, b, c koeffitsiyentlarni foydalanuvchidan so'rab, 
ax² + bx + c = 0 tenglamaning ildizlarini toping.
Diskriminant manfiy bo'lsa, haqiqiy ildizlar yo'qligini bildiring.
'''
def kvadrat_tenglama(a, b, c):
  """kvadrat tenglama yechimini touvchi funksiya"""
  if a == 0:
    raise ValueError("a nolga teng bolishi mumkin emas!")
  
  diskriminant = b**2 - 4*a*c
  
  if diskriminant < 0:
    return "Haqiqiy ildizlar mavjud emas"
  elif diskriminant == 0:
    x = -b / (2 * a)
    return f"Bir xil ildiz: x = {x}"
  else: 
    x1 = (-b + diskriminant**0.5) / (2 * a)
    x2 = (-b - diskriminant**0.5) / (2 * a)
    return f"Ildizlar: x1 = {x1}, x2 = {x2}"

def main():
    print("ax² + bx + c = 0 kvadrat tenglamaning ildizlarini topish")
    try:
        a = float(input("a koeffitsiyentini kiriting: "))
        b = float(input("b koeffitsiyentini kiriting: "))
        c = float(input("c koeffitsiyentini kiriting: "))
        
        result = kvadrat_tenglama(a, b, c)
        print("\nYechim:", result)
        
    except ValueError as e:
        print(f"\nXato: {e}")
    except Exception as e:
        print(f"\nKutilmagan xato: {e}")

if __name__ == "__main__":
    main() 