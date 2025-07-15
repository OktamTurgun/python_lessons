"""
Created on Mon Jun 2 18:22:14 2025

24-dars. "Funksiyalar, so'ngi so'z" (filter())

@author: uktam
"""

import random as r


# filter() funksiyasi - bu Pythonning yuqori darajadagi funksiyalaridan biridir.
# U berilgan funksiyani iterable (ro'yxat, to'plam, tuple va h.k.) elementlariga qo'llaydi
# va natijalarni yangi iterable sifatida qaytaradi.
# filter() funksiyasining sintaksisi:
# filter(function, iterable)
# function - qo'llaniladigan funksiya
# iterable - elementlarga funksiya qo'llaniladigan iterable obyekt
# filter() funksiyasi iterable obyektning har bir elementiga funksiya qo'llaydi
# va natijalarni yangi iterable sifatida qaytaradi.
# filter() funksiyasini ishlatish uchun avval funksiya aniqlanadi,
# so'ngra filter() funksiyasi chaqiriladi.


def juftmi(x):
    return x % 2 == 0


# filter() funksiyasini ishlatish
sonlar = list(range(11))
juft_sonlar = list(filter(juftmi, sonlar))

# print("Sonlar:", sonlar)
# print("Juft sonlar:", juft_sonlar)


# filter() funksiyasi yordamida sonlarni 3 ga bo'lish
def uchga_bol(x):
    return x % 3 == 0


uchga_bolingan_sonlar = list(filter(uchga_bol, sonlar))
# print("Sonlar:", sonlar)
# print("3 ga bo'lingan sonlar:", uchga_bolingan_sonlar)


sonlar = r.sample(
    range(100), 10
)  # sample() funksiyasi tasodifiy sonlar ro'yxatini yaratadi
# print(sonlar)
print("Tasodifiy sonlar:", sonlar)


def juftmi2(x):
    return x % 2 == 0


juft_sonlar2 = list(filter(juftmi2, sonlar))

print("(function bilan)Juft sonlar:", juft_sonlar2)

juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
print("(lambda bilan) Juft sonlar:", juft_sonlar)

mevalar = [
    "olma",
    "anor",
    "uzum",
    "anjir",
    "shaftoli",
    "tarvuz",
    "qovun",
    "banan",
    "apelsin",
    "limon",
]


# filter() funksiyasi yordamida uzunligi 5 dan katta bo'lgan mevalarni ajratish
def uzunligi5danKatta(meva):
    return len(meva) > 5


uzun_mevalar = list(filter(uzunligi5danKatta, mevalar))
print("Uzunligi 5 dan katta bo'lgan mevalar:", uzun_mevalar)
uzun_mevalar_lambda = list(filter(lambda meva: len(meva) > 5, mevalar))
print("Uzunligi 5 dan katta bo'lgan mevalar (lambda bilan):", uzun_mevalar_lambda)


# filter() funksiyasi yordamida uzunligi 5 dan kichik bo'lgan mevalarni ajratish
def uzunligi5danKichik(meva):
    return len(meva) < 5


beshdan_kichik = list(filter(uzunligi5danKichik, mevalar))
print("Uzunligi 5 dan kichik bo'lgan mevalar:", beshdan_kichik)

uzun_mevalar_kichik_lambda = list(filter(lambda meva: len(meva) < 5, mevalar))
print(
    "Uzunligi 5 dan kichik bo'lgan mevalar (lambda bilan):", uzun_mevalar_kichik_lambda
)

harf_a_bilan_boshlanadigan_mevalar = list(
    filter(lambda meva: meva.startswith("a"), mevalar)
)
print("Harf 'a' bilan boshlanadigan mevalar:", harf_a_bilan_boshlanadigan_mevalar)
harf_a_bilan_boshlanadigan_mevalar2 = list(filter(lambda meva: meva[0] == "a", mevalar))

print(
    "Harf 'a' bilan boshlanadigan mevalar (indeks bilan):",
    harf_a_bilan_boshlanadigan_mevalar2,
)

harf_unli_harf = list(filter(lambda meva: meva[0] in "aeiou", mevalar))
print("Unli harf bilan boshlanadigan mevalar:", harf_unli_harf)

# Tarkibida 'a' harfi bo'lgan mevalarni ajratish
tarkibida_a_harfi_bor_mevalar = list(filter(lambda meva: "a" in meva, mevalar))
print("Tarkibida 'a' harfi bo'lgan mevalar:", tarkibida_a_harfi_bor_mevalar)

harf = "a"
mevalar_a = list(filter(lambda meva: meva.startswith(harf), mevalar))
print(f"Harf '{harf}' bilan boshlanadigan mevalar:", mevalar_a)

list(filter(lambda meva: (meva.startswith("a") and meva.endswith("r")), mevalar))
# Harf 'a' bilan boshlanib, 'r' bilan tugaydigan mevalarni ajratish
harf_a_meva = list(
    filter(lambda meva: (meva.startswith("a") and meva.endswith("r")), mevalar)
)
print(
    "Harf 'a' bilan boshlanib, 'r' bilan tugaydigan mevalar:",
    harf_a_meva,
)


# funksiya bilan ishlatish
def starts_with_a_and_ends_with_r(meva):
    return meva.startswith("a") and meva.endswith("r")


meva_a = list(filter(starts_with_a_and_ends_with_r, mevalar))
print(
    "Harf 'a' bilan boshlanib, 'r' bilan tugaydigan mevalar (funksiya bilan):",
    meva_a,
)
