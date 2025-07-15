"""
Created on Mon June 02 16:50:21 2025

24-dars. "Funksiyalar, so'ngi so'z" (map())

@author: uktam
"""

# map() funksiyasi - bu Pythonning yuqori darajadagi funksiyalaridan biridir.
# U berilgan funksiyani iterable (ro'yxat, to'plam, tuple va h.k.) elementlariga qo'llaydi
# va natijalarni yangi iterable sifatida qaytaradi.
# map() funksiyasining sintaksisi:
# map(function, iterable, ...)
# function - qo'llaniladigan funksiya
# iterable - elementlarga funksiya qo'llaniladigan iterable obyekt
# ... - qo'shimcha iterable obyektlar (agar funksiya bir nechta argument oladigan bo'lsa)
# map() funksiyasi iterable obyektning har bir elementiga funksiya qo'llaydi
# va natijalarni yangi iterable sifatida qaytaradi.
# map() funksiyasini ishlatish uchun avval funksiya aniqlanadi,
# so'ngra map() funksiyasi chaqiriladi.

from math import sqrt  # Kvadrat ildiz olish uchun sqrt funksiyasini import qilamiz

# Funksiya aniqlash
sonlar = list(range(11))
ildizlar = list(map(sqrt, sonlar))

# map() funksiyasini ishlatish
# print("Sonlar:", sonlar)
# print("Kvadrat ildizlar:", ildizlar)

# map() funksiyasi yordamida sonlarni kvadratga oshirish
sonlar_kvadrat = list(map(lambda x: x**2, sonlar))
# print("Sonlar kvadrat:", sonlar_kvadrat)

# map() funksiyasi yordamida sonlarni 3 ga ko'paytirish
sonlar_uchga_kopaytirilgan = list(map(lambda x: x * 3, sonlar))
# print("Sonlar 3 ga ko'paytirilgan:", sonlar_uchga_kopaytirilgan)

# map() funksiyasi yordamida sonlarni 2 ga bo'lish
sonlar_ikki_bolingan = list(map(lambda x: x / 2, sonlar))
# print("Sonlar 2 ga bo'lingan:", sonlar_ikki_bolingan)


def daraja2(x):
    return x * x


kvadrat_sonlar = list(map(daraja2, sonlar))
# print(kvadrat_sonlar)

kvadratlar = list(map(lambda x: x**2, sonlar))
# print("Sonlar kvadrati:", kvadratlar)

kvadratlar = []
for son in sonlar:
    kvadratlar.append(son * son)
# print("Sonlar kvadrati:", kvadratlar)

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x, y: x + y, a, b))
print("A va B ro'yxatlari yig'indisi:", a_plus_b)
print(a_plus_b)
print("A va B ro'yxatlari yig'indisi:", list(map(lambda x, y: x + y, a, b)))
