"""
12-dars: Python re (regular expressions) kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda re kutubxonasi yordamida quyidagilarni o‘rganamiz:
 - matndan ma’lumot izlash (search, findall)
 - moslikni tekshirish (match)
 - matnni almashtirish (sub)
 - regex namunalar: telefon raqam, email, faqat raqam
"""

import re

# findall — barcha mos keladigan elementlarni topish
matn = "Bugun 2 ta olma, 3 ta banan va 1 ta shaftoli sotildi."
raqamlar = re.findall(r"\\d+", matn)
print("Topilgan raqamlar:", raqamlar)

# search — birinchi moslikni topish
email = "Kontakt: info@example.com"
mos = re.search(r"[\w.-]+@[\w.-]+\\.\w+", email)
if mos:
    print("Email topildi:", mos.group())

# match — faqat boshidan tekshiradi
s = "Python3"
if re.match(r"Python", s):
    print("Boshlanishda Python bor")

# sub — matnni almashtirish
s2 = "Salom, aziz foydalanuvchi!"
yangi = re.sub(r"foydalanuvchi", "Uktam", s2)
print(yangi)

# Amaliy mashq: faqat raqamdan iborat matnmi?


def raqammi(s):
    return bool(re.fullmatch(r"\\d+", s))


print("'12345' raqammi?", raqammi("12345"))
print("'12a45' raqammi?", raqammi("12a45"))

# Amaliy mashq: Telefon raqamini tekshirish (masalan, +998 90 123-45-67)


def telefonmi(s):
    return bool(re.fullmatch(r"\+998\s\d{2}\s\d{3}-\d{2}-\d{2}", s))


print("'+998 90 123-45-67' telefonmi?", telefonmi("+998 90 123-45-67"))
print("'998901234567' telefonmi?", telefonmi("998901234567"))

# Amaliy mashq: Email manzilini tekshirish


def emailmi(s):
    return bool(re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w+", s))


print("'test@gmail.com' emailmi?", emailmi("test@gmail.com"))
print("'test@@gmail.com' emailmi?", emailmi("test@@gmail.com"))

# Amaliy mashq: Matndan barcha so'zlarni ajratib olish
matn2 = "Salom, bu yerda bir nechta so'zlar bor!"
sozlar = re.findall(r"\w+", matn2)
print("Topilgan so'zlar:", sozlar)

# Amaliy mashq: Matndan barcha katta harflarni topish
matn3 = "Python va RE kutubxonasi Juda Qiziqarli!"
katta_harf = re.findall(r"[A-Z]", matn3)
print("Katta harflar:", katta_harf)
