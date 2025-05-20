"""
Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi 
funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
"""
# def greater_than(num1, num2):
#   if num1 > num2:
#     print(f"{num1} > {num2}")
#   elif num1 < num2:
#     print(f"{num1} < {num2}")
#   else:
#     print(f"{num1} = {num2} Sonlar teng!")

# greater_than(12, 25)
# greater_than(234, 543)
# greater_than(2*6, 2**2)

''''''
def compare(x:int, y:int) -> str:
  """Sonlarni solishtirish"""
  if x > y:
    return f"{x} > {y}"
  elif x < y:
    return f"{x} < {y}"
  else:
    return "Sonlar teng!"

x = int(input("Birinchi sonni kiriring: "))
y = int(input("Ikkinchi sonni kiriring: "))
print(compare(x, y))
    