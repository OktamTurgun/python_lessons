"""
Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib
qolmoqda. Xatolarni to'g'rilay olasizmi?
"""
# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting: "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat.lower() == 'exit':
#       print("Dastur tugatildi!")
#       break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
'''try-except yordamida tekshiramiz'''
# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting: "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#       print("Dastur tugatildi!")
#       break
#     try:
#       qiymat = float(qiymat)
#       if qiymat < 0:
#         print("Musbat son kiriting!")
#         continue
#       ildiz = qiymat ** 0.5
#       print(f"{qiymat} ning ildizi {ildiz} ga teng")
#     except ValueError:
#       print("Iltomos, musbat son kiriting yoki 'exit' deb yozing!")  
      
"""
Parol tekshiruvchi dastur tuzing. 3 ta urunish berilsin.
"""
login = "python123"
attempts = 3

while attempts > 0:
  qiymat = input("Parol kiriting: ")
  if qiymat == login:
    print("Xush kelibsiz!")
    break
  attempts -= 1
  print(f"Noto'g'ri login! {attempts} ta urunish qoldi")
else:
  print("Hisobingiz bolklandi")
  
''' 1dan n gacha bo'lgan toq sonlarni chiqaring. '''
n = int(input("N sonini kiriting: "))
i = 1
while i <= n:
  if i % 2 != 0:
    print(i, end=" ")
  i += 1 
  
''' faktorial hisoblash '''
n = int(input("Son kiriting: "))
factorial = 1
i = 1
while i <= n:
  factorial *= i
  i += 1
print(f"{n}! = {factorial}")

''' Sonni teskari chiqarish '''
num = int(input("Son kiriting: "))
teskari = 0
while num > 0:
  teskari = teskari * 10 + num % 10
  num = num // 10
print(f"Teskari son: {teskari}")

''' Tub sonini tekshirish '''
n = int(input("Son kiriting: "))
i = 2
tub_son = True
while i < n:
  if n % i == 0:
    tub_son = False
    break
  i += 1
print(f"{n} tub son." if tub_son else f"{n} tub son emas")