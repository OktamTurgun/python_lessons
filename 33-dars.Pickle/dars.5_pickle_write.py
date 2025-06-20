"""
Created on Thu Fri 20 11:20:14 2025

33-dars. Fayllar bilan ishlash. Pickle

@author: uktam
"""
import pickle
# Faylga yozish
talaba1 = {"ism": "Hasan", "familiya": "Olimov", "tyil": 2005, "kurs": 2}
talaba2 = {"ism": "Alijon", "familiya": "Valiyev", "tyil": 2004, "kurs": 3}
talaba3 = {"ism": "Rahima", "familiya": "Muminova", "tyil": 2006, "kurs": 1}
talabalar = [talaba1, talaba2, talaba3]

with open('info', 'wb') as file:
    pickle.dump(talaba1, file)
with open('info', 'ab') as file:
    pickle.dump(talaba2, file)
with open('info', 'ab') as file:
    pickle.dump(talaba3, file)
# Faylni o'qish
with open('info', 'rb') as file:
    while True:
        try:
            talaba = pickle.load(file)
            print(talaba)
        except EOFError:
            break  # Fayl oxiriga yetganda xatolik yuz bermasligi uchun
# Faylni o'qish
with open('info', 'rb') as file:
    talabalar = []
    while True:
        try:
            talaba = pickle.load(file)
            talabalar.append(talaba)
        except EOFError:
            break  # Fayl oxiriga yetganda xatolik yuz bermasligi uchun
          
print(talabalar)  # O'qilgan talabalar ro'yxatini chiqaramiz
# Har bir talabani alohida chiqarish
print("\nTalabalar ro'yxati:")
for talaba in talabalar:
    print(f"Ism: {talaba['ism']}, Familiya: {talaba['familiya']}, "
          f"Tug'ilgan yil: {talaba['tyil']}, Kurs: {talaba['kurs']}")
    
# Faylni o'qish va har bir talabani alohida chiqarish
with open('info', 'rb') as file:
    while True:
        try:
            talaba = pickle.load(file)
            print(f"Ism: {talaba['ism']}, Familiya: {talaba['familiya']}, "
                  f"Tug'ilgan yil: {talaba['tyil']}, Kurs: {talaba['kurs']}")
        except EOFError:
            break  # Fayl oxiriga yetganda xatolik yuz bermasligi uchun

