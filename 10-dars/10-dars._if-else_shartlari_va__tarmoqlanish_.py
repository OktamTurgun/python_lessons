# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:48:28 2024

Dasturlash asoslari

#10-dars: TARMOQLANISH (if-else)

@author: uktam
"""  
cars = ['mercedes-benz', 'volvo', 'general motors', 'bmw', 'tesla', 'ferrari', 'audi',
    'toyota', 'honda', 'nissan', 'ford', 'volkswagen', 'hyundai', 'chevrolet',]

for car in cars: # avtolar ichidadi har bir avto uchun ...
    if car == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(car.upper()) # avto nomini hamma harflarini katta bilan yozadi.
    else: # aks holda ...
        print(car.title()) # avto nomini faqat birinchi harfini katta bilan yozadi.

''''''
kitchens = ['burger king','milliy taomlar','rayxon','bbq','safia','shashlik']

for brand in kitchens:
   if brand != 'bbq':
       print(brand.title())
   else:
       print(brand.upper())

'''
# Python matematikadan odatiy mantiqiy shartlarni qo'llab-quvvatlaydi:

# Teng: a == b, (tengmi? , teng bo'lsa)
# Teng emas: a != b
# Kichikroq: a < b
# Kichik yoki teng: a <= b
# Kattaroq: a > b
# dan katta yoki teng: a >= b
'''
# ism = 'Ali'

# ism.lower() == 'ali'

'''''' 
name = input("Ismingiz nima?\n>>> ").strip()
if name.lower() != "ali":
    print(f"Uzr {name.title()} biz Alini kutyapmiz")
else:
    print("Salom Ali") 
 
''''''
# ism = input("Ismingiz nima? \n>>> ")

# if ism.lower() != 'uktam':
#    print(f"Uzr {ism.title()} biz Uktamni kutyapmiz. ")
# else:
#    print("Salom,  Uktam ")

''''''
javob = int(input("12x6 nechiga teng?>>> "))
if javob != 72:
    print("Javob xato! To'g'ri javob 72")
else:
    print(f"Barakalla! Javob {javob} Juda to'gr'i")

''''''
yosh = int(input("Yoshingiz nechida?>>> "))
if yosh <= 18:
    print(f"Sizga kirish mumkin emas! Siz {yosh} yoshda ekansiz.")
else:
    print("Xush kelibsiz!")

''''''
# login = input("Yangi login tanlang: ")
# if len(login) <=5: # Login uzunligini tekshiramiz
#    print("Login 5 harfdan ko'proq bo'lishi shart! ")
# else:
#    print(f"Xush kelibsiz! {login.title()}")

''''''
# year = int(input("Tug'ulgan yilingizni kiriting: "))
# if 2025-year<18:
#     print(f"Yoshingiz {2025-year}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush keleibsiz") 
  
''''''    
# age = int(input("Yoshingiz nechida? "))
# if age>=65: print("Siz nafaqa yoshida ekansiz") 
    
''''''
# x, y = 25,50 # x=25 va y= 50
# print("x>y") if x>y else print("x<y")  # x<y 

''''''
# x, y = 50,25
# print("x>y") if x>y else print("x<y")  # x>y 
# 
''''''        
# name = 'Ali'
# name.lower() == 'Ali'
# print(name.lower() == 'ali')
    
# Practices    

# 1. Yangi cars degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini 
#    katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
 
# cars = ['tayota','mazda','hyundai','gm','kia','ferrari']   

# for avto in cars:
#    if avto == 'gm':
#        print(avto.upper())
#    else:
#       print(avto.title())
    
# 2. Yuqoridagi mashqni ( != ) operatori yordamida bajaring.

# for avto in cars:
#    if avto != 'gm':
#        print(avto.title())
#    else:
#        print(avto.upper()) 
    
# 3. Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
#    Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. 
#    Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.   
    
# login = input("login kiriting:\n>>>")    
# if login.lower() == "admin": 
#    print("Xush kelibsiz Admin foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#    print(f"xush kelibsiz {login.title()} ")    
    
# 4. Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
#   "Sonlar teng" ekan degan yozuvni konsolga chiqaring.   
    
# son1 = float(input("Birinchi sonni kiriting: >>>"))   
# son2 = float(input("Ikkinchi sonni kiriting:>>>"))    
# if son1 == son2:
#    print(f"Sonlar teng: {son1}={son2}")    
# else:
#    print("Sonlar teng emas!")    
    
# 5. Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa
#    konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.    
    
# son = float(input("istalgan son kiriting:\n>>>")) 
# print("Son manfiy") if son<0 else print("Son musbat") # Qisqa kodlar uchun shart va 
# uning badanini 1 qatorga jamlab yozishimiz ham mumkin:   
# if son >= 0:
#    print(f"{son} Musbat son")
# else:
#    print(f"{son} Manfiy son")
    
#son = float(input("istalgan son kiriting:\n>>>")) 
#print("Son manfiy") if son<0 else print("Son musbat")   
#if son < 0:
#    print(f"{son} Manfiy son")
#else:
#    print(f"{son} Musbat son")
        
# 6. Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning 
#    ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting"
#    degan xabarni chiqaring.     
    
#son = float(input("Istalgan son kiriting: "))   
#print(son**(1/2)) if son>0 else print("Musbat son kiriting:")    