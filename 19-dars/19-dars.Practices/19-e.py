"""
Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
"""
def daraja(x, y=2):
  print(f"{x} ning {y} darajasi: {x**y}")
  print(f"{x}^{y} = {x**y}")
  
daraja(3, 3)
daraja(3, 5)
daraja(15, 3)
daraja(6)