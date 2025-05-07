"""
Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning
ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa,
"Musbat son kiriting" degan xabarni chiqaring. 
"""
num = int(input("Istalgan son kiriting: "))
if num > 0:
  print(f"{num} ning ildizi {int(num**(1/2))} ga teng")
else:
  print('Musbat son kiriting: ')

"""
Foydalanuvchi noto'g'ri ma'lumot kiritishi holatini hisobga olib,
while tsikli yordamida musbat son kiritilguncha qayta so'rash
"""
while True:
  num1 = input("Musbat son kiriting: ")
  if num1.replace('.', '', 1).isdigit() and float(num1) > 0:
    num1 = float(num1)
    print(f"{num1} nimg ildizi {num1**0.5:.2f} ga teng")
    break
  else:
    print("Iltimos, musbat son kiriting: ")
