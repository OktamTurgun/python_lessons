# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:58:50 2024

# Dasturlash asoslari

#16-dars: NESTING

@author: uktam

"""
# NESTING
# Lug'at ichida ro'yxat, ro'yxat ichida lug'at?

# Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yoki boshqa lug'atni, 
# yoki aksincha ro'yxat ichida lug'atni saqlash ham qo'l kelishi mumkin. 
# Bu ingliz tilida Nesting deyiladi. Nesting Pythondagi foydali xususiyatlardan biri.

# LUG'ATLAR RO'YXATI
# Biz avvalgi darsimizda talabalarning ma'lumotlarini lug'at shaklida saqlashni ko'rgan edik.
# Shunday talabalardan yuzlab bo'lganda, ularning har biriga alohida lug'at qilishimiz 
# tabiiy, lekin bu lug'atlar bilan ishlash qiyinchilik tug'dirishi mumkin.
# Shunday xolatda barcha lug'atlarni (talabalarni) bitta ro'yxatga joylab,
# ular ustida turli amallar bajarish mumkin.

# Kelin quyidagi misolni ko'ramiz, bazamizda bir nechta mashinalar bor. 
# Har bir mashina alohida lug'at shaklida.

car0 = {
        'model':'lasetti',
        'rang':'oq',
        'yil':'2021',
        'narh':'13500', 
        'km':'50000',
        'karobka':'avtomat' 
        }

car1 = {
        'model':'nexiya 3',
        'rang':'qora',
        'yil':'2020',
        'narh':'9500', 
        'km':'120000',
        'karobka':'avtomat'
        }

car2 = {
        'model':'gentra',
        'rang':'kulrang',
        'yil':'2022',
        'narh':'15000', 
        'km':'20000',
        'karobka':'mexanika'
        }

#  Agar biz har bir lug'atga alohida murojat qiladigan bo'lsak, lug'atlarning
#  nomlarini yodlab qolishimiz talab qilinar edi:


#car = car0
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']} $")

#car = car1
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']} $")

#car = car2
#print(f"{car['model'].title()},"
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']} $")

# Keling, barcha avtolarni bitta ro'yxatga joylaymiz, va for tsikli yordamida 
# birma-bir konsolga chiqaramiz

cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()},"
#          f"{car['rang']} rang,"
#          f"{car['yil']}-yil {['narh']}$ ")

# E'tibor bering, ishimiz bir muncha yengillashdi, kodimiz ham qisqardi. Natija esa bir hil.

#Endi biz ro'yxat  ichidagi istalgan lug'atga indeks bo'yicha murojat qilaveramiz
# (lug'at nomini yodlab qolish shart emas).

#print(f"{cars[2]['rang'].title()} "
#      f"{cars[2]['model']}")

# for tsikli yordamida biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin:

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None, # rang noaniq
        'yil':'2020',
        'narh':None, 
        'km':0,
        'karobka':'avtomat'}
    malibus.append(new_car)

#for malibu in malibus:
#    print(malibu)

#  Yuqoridagi misloda biz 10 ta Malibu mashinasidan iborat ro'yxat tuzdik. E'tibor qiling,
# 'rang' kalitiga qiymat bermadik va None deb qoldirdik. Endi ishlab chiqarish jarayonida
#  mashinalarga turli ranglarni berishimiz mumkin.  Misol uchun birinchi 3 ta
#  mashinaga qizil rang beramiz:

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'
    
for malibu in malibus[6:]:
    malibu['rang'] = 'oq' 
    malibu['karobka'] = 'mexanika'
    
#for malibu in malibus:    
#    print(malibu)

# Keling endi, mashinalarning korobkasidan chiqqan holda narh belgilaymiz:

for malibu in malibus:
    if malibu['karobka'] == 'avtomat':
        malibu['narh'] = 25000
    else:
        malibu['narh'] = 22000

#for malibu in malibus:    
#   print(malibu)

# LUG'AT ICHIDA RO'YXAT

# Bir kalitga bir nechta qiymatlar berish talab qilinganda, qiymatlarni ro'yxat
# ko'rinishida yozish o'rinlidir. Misol uchun, bir tashkilotda bir nechta dasturchilar 
# ishlaydi va har bir dasturchi turli dasturlash tillarini biladi. Keling dasturchilar 
# lug'atini tuzamiz va har bir dasturchi haqidagi ma'umotni konsolga chiqaramiz:

#programmers = {
#    'ali':['c#','java'],
#    'vali':['python','c','c++'],
#    'jasur':['c#','js'],
#    'olimjon':['go','php'],
#    'bekzod':['html','scc','js'],
#    'umid':['php','go','sql','js'],
#    }

#for ism, tillar in programmers.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi")
#    for til in tillar:
#        print(til.upper())

# Pythondagi print() funktsiyasi har bir matndan so'ng yangi qator tashlaydi. 
# Buning oldini olish uchun quyidagi usuldan foydalanish mumkin: print(string, end = '')

#for ism, tillar in programmers.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi")
#    for til in tillar:
#        print(f"{til.upper()} ", end = "")

# LIG'AT ICHIDA LUG'AT

# Bunday qilish tavsiya etilmasada, istisno holatlarda lug'at ichidagi qiymatlarni lug'at 
# ko'rinishida ham saqlash mumkin. Misol uchun, ish joyingizdagi hamkasblaringiz haqidagi 
# ma'lumotlarni saqlashda, hamkasbingizning ismi kalit, u haqidagi ma'lumotlarni esa lug'at
# ko'rinishida berilishi mumkin.

hamkasblar = {
     'ali':{'familiya':'valiyev',
            't_yil':1990,
            'malumoti':'oliy',
            'tillar':['python','c','c++']
            },
    'vali':{'familiya':'kenjayev',
            't_yil':1995,
            'malumoti':'orta-maxsus',
            'tillar':['html','css','js']
            },
    'olim':{'familiya':'hasanov',
            't_yil':1999,
            'malumoti':'maxsus',
            'tillar':['php','c++']
            }
   }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['t_yil']}-yilda tug'ilgan, "
          f"Ma'lumoti: {info['malumoti']}. \n"
          "Quyidagi dasturlsah tillarini biladi:")
    for til in info['tillar']:
        print(til.upper() )

# Lug'at ichidagi lug'atlar bir hil tuzilishga ega bo'lgani 
# ishingizni ancha yengillashtiradi, aks holda kodingiz murakkablashib ketishi mumkin.
