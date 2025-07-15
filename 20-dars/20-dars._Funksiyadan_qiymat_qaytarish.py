# -*- coding: utf-8 -*-
"""
Created on Thu May 22 08:01:28 2025

20-dars "Function Return Values" (Funksiyadan qiymat olish)

@author: uktam
"""
# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     print(toliq_ism)
    
# toliq_ism_yasa('olim', 'hakimov')

''''''
# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism
    
# student = toliq_ism_yasa('olim', 'hakimov')
# student1 = toliq_ism_yasa('abror', 'yusupov')
# print(f"Darsga kelmagan talabalar: {student} va {student1}")
# print(f"{student1} darsga kechikib keldi.")

''''''
# Ixtiyoriy argumentlar (Default Arguments)
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# student1 = toliq_ism_yasa('davron', 'qobulov')
# student2 = toliq_ism_yasa('davron', 'qobulov', 'shavkatovich')
# print(f"A'lochi o'quvchilar: {student1} va {student2}")

''''''
def avto_info(kompaniya, model, rang, korobka='avtomat', yil=None, narh=None):
    """Avtomobil haqida ma'lumot qaytaruvchi funksiya"""
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rang': rang,
        'korobka': korobka,
        'yil':yil,
        'narh': narh
    }
    return avto

# avto1 = avto_info('Toyota', 'Camry', 'oq')
# avto2 = avto_info('Hyundai', 'Sonata', 'qora', 'mexanika', 2020, '27000$')
# avto3 = avto_info('BYD', 'Seal', 'qizil', 'avtomat', 2024, '25000$')
# avtolar = [avto1, avto2, avto3]

# print("Online bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Nomalum"
#     print(f"{avto['rang'].title()} {avto['kompaniya']} {avto['model']} Narhi: {narh}")

''''''
# def hisobla(a, b, amal='+'):
#     """Ixtiyoriy amal bilan hisoblash"""
#     if amal == '+':
#         return a + b
#     elif amal == '-':
#         return a - b
#     elif amal == '*':
#         return a * b
#     elif amal == '/':
#         return a / b
#     else:
#         return "Noto'g'ri amal"

# print(hisobla(5, 3))  # 8
# print(hisobla(5, 3, '-'))  # 2

''''''
# def user_profile(ism, yosh, shahar='Toshkent', til='uz'):
#     """Foydalanuvchi profili yaratish"""
#     print(f"Ism: {ism}")
#     print(f"Yosh: {yosh}")
#     print(f"Shahar: {shahar}")
#     print(f"Til: {til}")

# user_profile('Ali', 25)
# user_profile('John', 30, 'New York', 'eng')

''''''
# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(0, 10))
# print(oraliq(10, 21))

''''''
def oraliq1(min, max, qadam):
    """A function that returns numbers in a given range."""
    nums = []
    while min<max:
        nums.append(min)
        min += qadam
    return nums
print(oraliq1(0,10,2))

''''''
print("saytimizdagi avtolar ro'yxatini shakllantiramiz.")
cars = []
while True:
    print("\nQuyidagi ma'lumotlartni kiriting:\n", end='')
    kompaniya=input("Ishlab chiqruvchi: ")
    model = input("Modeli: ")
    rang = input("Rangi: ")
    korobka = input("Korobka: ")
    yil = input("Yili: ")
    narh = input("Narhi: ")
    
    cars.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
    
    javob = input("Yana avtomabil qoshasizmi? (yes/no): ")
    if javob == 'no':
        break
print("\nSalonimizdagi avtolar:")
for avto in cars:
    if avto['narh']:
        price = avto['narh']
    else:
        price = 'Nomalum'
    print(f"{avto['kompaniya']} {avto['model']} {avto['yil']} Narhi: {price}")
