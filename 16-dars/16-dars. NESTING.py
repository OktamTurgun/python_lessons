# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:58:50 2024

Dasturlash asoslari

16-dars: NESTING

@author: uktam

"""
"""
NESTING
Lug'at ichida ro'yxat, ro'yxat ichida lug'at?

Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yoki boshqa lug'atni, 
yoki aksincha ro'yxat ichida lug'atni saqlash ham qo'l kelishi mumkin. 
Bu ingliz tilida Nesting deyiladi. Nesting Pythondagi foydali xususiyatlardan biri.

LUG'ATLAR RO'YXATI
Biz avvalgi darsimizda talabalarning ma'lumotlarini lug'at shaklida saqlashni ko'rgan edik.
Shunday talabalardan yuzlab bo'lganda, ularning har biriga alohida lug'at qilishimiz 
tabiiy, lekin bu lug'atlar bilan ishlash qiyinchilik tug'dirishi mumkin.
Shunday xolatda barcha lug'atlarni (talabalarni) bitta ro'yxatga joylab,
ular ustida turli amallar bajarish mumkin.

Kelin quyidagi misolni ko'ramiz, bazamizda bir nechta mashinalar bor. 
Har bir mashina alohida lug'at shaklida.
"""
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
        'rang':'qizil',
        'yil':'2022',
        'narh':'15000', 
        'km':'20000',
        'karobka':'mexanika'
        }

'''
Agar biz har bir lug'atga alohida murojat qiladigan bo'lsak, lug'atlarning
nomlarini yodlab qolishimiz talab qilinar edi:
'''
# car = car0
# print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']} $")

# car = car1
# print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']} $")

# car = car2
# print(f"{car['model'].title()},"
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']} $")

''' Keling, barcha avtolarni bitta ro'yxatga joylaymiz, va for tsikli yordamida ''' 
# birma-bir konsolga chiqaramiz
# cars = [car0, car1, car2]
# for car in cars:
#    print(f"{car['model'].title()},"
#          f"{car['rang']} rang,"
#          f"{car['yil']}-yil {car['narh']}$")
   
''' Yoki yana bir usul: Lug'atdan ma'lumotlarni dinamik olish '''
# cars = [car0, car1, car2]
# for car in cars:
#     print(", ".join(str(value.title()) for value in car.values()))

''' E'tibor bering, ishimiz bir muncha yengillashdi, kodimiz ham qisqardi. Natija esa bir hil. '''

'''
Endi biz ro'yxat  ichidagi istalgan lug'atga indeks bo'yicha murojat qilaveramiz
(lug'at nomini yodlab qolish shart emas). Lug'atdagi ma'lumotlarga alohida murojaat qilish
'''
# print(cars[0]['model'].title())

# print(f"{cars[2]['rang'].title()} "
#      f"{cars[2]['model']}")

''' for tsikli yordamida biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin: '''
malibus = []
for n in range(5):
    new_car = {
        'model':'malibu',
        'rang':None, # rang noaniq
        'yil':'2020',
        'narh':None, 
        'km':0,
        'karobka':'avto'}
    malibus.append(new_car)

# for malibu in malibus:
#    print(malibu)

'''
 Yuqoridagi misloda biz 5 ta Malibu mashinasidan iborat ro'yxat tuzdik. E'tibor qiling,
'rang' kalitiga qiymat bermadik va None deb qoldirdik. Endi ishlab chiqarish jarayonida
 mashinalarga turli ranglarni berishimiz mumkin.  Misol uchun birinchi 3 ta
 mashinaga qizil rang beramiz:
'''

# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'

# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
    
# for malibu in malibus[6:]:
#     malibu['rang'] = 'oq' 
#     malibu['karobka'] = 'mexanika'
    
#for malibu in malibus:    
#    print(malibu)

''' Keling endi, mashinalarning korobkasidan chiqqan holda narh belgilaymiz: '''
# for malibu in malibus:
#     if malibu['karobka'] == 'avtomat':
#         malibu['narh'] = 25000
#     else:
#         malibu['narh'] = 22000

#for malibu in malibus:    
#   print(malibu)

"""
LUG'AT ICHIDA RO'YXAT

Bir kalitga bir nechta qiymatlar berish talab qilinganda, qiymatlarni ro'yxat
ko'rinishida yozish o'rinlidir. Misol uchun, bir tashkilotda bir nechta dasturchilar 
ishlaydi va har bir dasturchi turli dasturlash tillarini biladi. Keling dasturchilar 
lug'atini tuzamiz va har bir dasturchi haqidagi ma'umotni konsolga chiqaramiz:
"""

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

"""
LIG'AT ICHIDA LUG'AT

Bunday qilish tavsiya etilmasada, istisno holatlarda lug'at ichidagi qiymatlarni lug'at 
ko'rinishida ham saqlash mumkin. Misol uchun, ish joyingizdagi hamkasblaringiz haqidagi 
ma'lumotlarni saqlashda, hamkasbingizning ismi kalit, u haqidagi ma'lumotlarni esa lug'at
ko'rinishida berilishi mumkin.
"""

# hamkasblar = {
#      'ali':{'familiya':'valiyev',
#             't_yil':1990,
#             'malumoti':'oliy',
#             'tillar':['python','c','c++']
#             },
#     'vali':{'familiya':'kenjayev',
#             't_yil':1995,
#             'malumoti':'orta-maxsus',
#             'tillar':['html','css','js']
#             },
#     'olim':{'familiya':'hasanov',
#             't_yil':1999,
#             'malumoti':'maxsus',
#             'tillar':['php','c++']
#             }
#    }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['t_yil']}-yilda tug'ilgan, "
#           f"Ma'lumoti: {info['malumoti']}. \n"
#           "Quyidagi dasturlsah tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper() )

# Lug'at ichidagi lug'atlar bir hil tuzilishga ega bo'lgani 
# ishingizni ancha yengillashtiradi, aks holda kodingiz murakkablashib ketishi mumkin.

tahoes = []
for n in range(5):
    new_car = {
        "model":"tahoe",
        "rang":None,
        "narh":57000,
        "km":0,
        "yil":2025,
        "karobka":"avto"
        }
    tahoes.append(new_car)
    
# for tahoe in tahoes:
#     print(tahoe)
    
# for tahoe in tahoes[:2]:
#     tahoe['rang'] = 'qizil'
# for tahoe in tahoes[2:4]:
#     tahoe['rang'] = 'qora'
# for tahoe in tahoes[4:]:
#     tahoe['rang'] = 'oq'
#     tahoe['karobka'] = 'mahanika'

    
# for tahoe in tahoes:
#     print(tahoe)
    
# List comprehension va dictionary update qilish
tahoes = [
    {
     "model":"tahoe",
     "rang":None,
     "narh":None,
     "km":0,
     "yil":2025,
     "karobka":"avto"
     }
    for _ in range(6)
]
# Ranglarni, narhlarni va karobkani o'zgartirish
karobka = ['mechanic', 'mechanic', 'avto', 'avto', 'avto', 'mechanic']
colors = ['qizil', 'qizil', 'oq', 'qora', 'oq', 'oq']
# prices = [45000, 50000, 53000, 50000, 47000, 59000]
for _, tahoe in enumerate(tahoes):
    tahoe['rang'] = colors[_]
    tahoe['karobka'] = karobka[_]
    # tahoe['narh'] = prices[_]
    
# for tahoe in tahoes:
#     print(', '.join(tahoe))
    
''' Kalit:qiymat ko'rinishida chiqarish: .join() yordamida '''
# for tahoe in tahoes:
#     print(', '.join(f"{key}: {value}" for key, value in tahoe.items()))
    
# Mashinalar uchun alohida qilib narh belgilaymiz
# for tahoe in tahoes:
#     if tahoe['karobka'] == 'avto':
#         tahoe['narh'] = 50000
#     else:
#         tahoe['narh'] = 45000
        
# for tahoe in tahoes:
#     print(', '.join(f"{key}: {value}" for key, value in tahoe.items()))
    
''' Lug'at ichida ro'yxat '''
programmers = {
    'john':['python', 'js', 'html'],
    'alex':['html', 'css', 'js'],
    'david':['rust', 'go'],
    'sally':['php', 'js', 'java'],
    'bill':['c#', 'c++', 'c', 'java']
    }
# for name, languages in programmers.items():
#     print(f"\n{name.title()} knows {languages}programming languages below:")
#     # print(f"{name.title():<5} knows: {', '.join(languages)}") # Bu formatda xam chiqarish mumkin
#     for language in languages:
#         print(language.upper())

# Foydalanuvchiga chiroyli formatda chiqarish:
# for name, languages in programmers.items():
#     print(f"{name.title()} knows these programming languages: {', '.join(languages).upper()}")

# for name, languages in programmers.items():
#     print(f"\n{name.title()} knows these programming languages below:")
#     for language in languages:
#         print(f"{language.upper()} ", end='')
        
''' Lug'at ichida lug'atlar '''
colleagues = {
    'martin':{
            'lastname':'doe',
            'age':32,
            'degree':'university degree',
            'languages':['java', 'python', 'js'],
            },
    'alex':{
            'lastname':'cook',
            'age':42,
            'degree':"master's degree",
            'languages':['c++', 'python', 'c#'],
            },
    'john':{
            'lastname':'kerry',
            'age':25,
            'degree':'higher education',
            'languages':['html', 'css', 'js', 'python'],
            }
    }
for name, info in colleagues.items():
    print(f"\n{name.title()} {info['lastname'].title()} "
          f"{info['age']} years old, "
          f"Education: {info['degree'].capitalize()}, \n"
          "Knows these languages:")
    print("_"*23)
    for language in info['languages']:
        print(language.upper())

# Yuqoridagi codni optimal qilib, o'qilishi oson, ihcham ko'rinishga olib kelish 
for name, info in colleagues.items():
    fullname = f"{name.title()} {info['lastname'].title()}"
    age = info['age']
    degree = info['degree'].capitalize()
    languages = ', '.join(info['languages'])
    
    print(f"\n{fullname}, {age} years old, Education: {degree}, Knows: {languages}.")
    
    
    
