# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:48:28 2024

Dasturlash asoslari

#10-dars: TARMOQLANISH

@author: uktam
"""

#avtolar = ['audi','bmw','volvo','ferrari','kia','hyundai']

#for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#    else: # aks holda ... 
#       print(avto.title())  # avto nomini faqat birinchi harfini katta bilann yoz.

#kitchens = ['burger king','milliy taomlar','rayxon','kfc','safia','shashlik']

#for kitchen in kitchens:
#    if kitchen == 'kfc':
#        print(kitchen.upper())
#    else:
#        print(kitchen.title())

# Python matematikadan odatiy mantiqiy shartlarni qo'llab-quvvatlaydi:

# Teng: a == b, (tengmi? , teng bo'lsa)
# Teng emas: a != b
# Kichikroq: a < b
# Kichik yoki teng: a <= b
# Kattaroq: a > b
# dan katta yoki teng: a >= b

#ism = 'Ali'

#ism.lower() == 'ali'

#ism = input('ismingiz nima?\n>>> ')
#if ism.lower() != 'ali':
#    print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
#else:
#    print("Salom, Ali ")    

#ism = input("Ismingiz nima? \n>>> ")

#if ism.lower() != 'uktam':
#    print(f"Uzr {ism.title()} biz Uktamni kutyapmiz. ")
#else:
#    print("Salom,  Uktam ")

#javob = float(input("12*6 nechiga teng? \n>>> " ))
#if javob != 72:
#    print("Javob xato!")
#else:
#    print("Javob to'g'ri!")

#yosh = int(input("Yoshingiz nechida?\n>>> "))

#if yosh >= 18:
#    print("Xush kelibsiz!")
#else:
#    print("Kirish mukin emas!")

#login = input("Yangi login tanlang: ")
#if len(login) <=5: # Login uzunligini tekshiramiz
#    print("Login 5 harfdan ko'proq bo'lishi shart! ")
#else:
#    print(f"Xush kelibsiz! {login.title()}")

#yil = int(input("Tug'ilgan yilingizni kiriting:\n "))
#if 2024-yil<18:
#    print(f"Yoshingiz {2024-yil} da ekan.")
#   print("Kirish mumkin emas!")
#else:
#    print("Xush kelibsiz!")    
    
#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>65: print("Siz  COVID-2019 risk guruxida ekansiz")  
    
#x, y = 25,50 # x=25 va y= 50
#print("x>y") if x>y else print("x<y")    
    
#x, y = 50,25 # x=25 va y= 50
#print("x>y") if x>y else print("x<y")    
    
# A M A L I Y O T    

# 1. Yangi cars degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini 
#    katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
 
#cars = ['tayota','mazda','hyundai','gm','kia','ferrari']   

#for avto in cars:
#    if avto == 'gm':
#        print(avto.upper())
#    else:
#       print(avto.title())
    
# 2. Yuqoridagi mashqni ( != ) operatori yordamida bajaring.

#for avto in cars:
#    if avto != 'gm':
#        print(avto.title())
#    else:
#        print(avto.upper()) 
    
# 3. Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
#    Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. 
#    Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.   
    
#login = input("login kiriting:\n>>>")    
#if login.lower() == "admin": 
#    print("Xush kelibsiz Admin foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
#    print(f"xush kelibsiz {login.title()} ")    
    
# 4. Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
#   "Sonlar teng" ekan degan yozuvni konsolga chiqaring.   
    
#son1 = float(input("Birinchi sonni kiriting: >>>"))   
#son2 = float(input("Ikkinchi sonni kiriting:>>>"))    
#if son1 == son2:
#    print(f"Sonlar teng: {son1}={son2}")    
#else:
#    print("Sonlar teng emas!")    
    
# 5. Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa
#    konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.    
    
#son = float(input("istalgan son kiriting:\n>>>")) 
#print("Son manfiy") if son<0 else print("Son musbat") # Qisqa kodlar uchun shart va 
# uning badanini 1 qatorga jamlab yozishimiz ham mumkin:   
#if son >= 0:
#    print(f"{son} Musbat son")
#else:
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