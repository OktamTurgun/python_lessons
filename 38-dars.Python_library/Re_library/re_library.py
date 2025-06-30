"""
12-dars: Python re (regular expressions) kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-29

Ushbu darsda re kutubxonasi yordamida quyidagilarni o‘rganamiz:
 - matndan ma’lumot izlash (search, findall)
 - moslikni tekshirish (match)
 - matnni almashtirish (sub)
 - regex namunalar: telefon raqam, email, faqat raqam
"""

import re
from uzwords import words

# findall — barcha mos keladigan raqamlarni topish
matn = "Bugun 2 ta olma, 3 ta banan va 1 ta shaftoli sotildi."
raqamlar = re.findall(r"\d+", matn)
print("Topilgan raqamlar:", raqamlar)

# search — birinchi moslikni topish (email)
email = "Kontakt: info@example.com"
mos = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email)
if mos:
    print("Email topildi:", mos.group())

matn = "Assalomu alaykum! Bugun havo juda yaxshi, quyosh porlayapti. Doʻstlarim bilan bogʻliq yangiliklar almashdim. Kechagi konsert ajoyib boʻldi! Endi loyiham ustida ishlashim kerak. Elektron manzilim: user123@example.com. Yangi kitob oʻqiyapman, juda qiziqarli. Ertaga futbol oʻyiniga boramiz. Hayot goʻzal!"

andoza1 = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
email = re.findall(andoza1, matn)
print("Email topildi:", email)

# match — faqat boshidan tekshiradi,
s = "Python3"
if re.match(r"Python", s):
    print("Boshlanishda Python bor")

word1 = "temir"
word2 = "tomir"
word3 = "tulpor"

andoza = "^t...r$"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

matches = []
for word in words:
    if re.match(andoza, word):
        matches.append(word)

print(matches)

# Kuchli parolni tekshirish
andoza2 = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
msg = "Yangi parol kiriting"
msg += "(kamida 8 ta belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, "
msg += "1 ta son va 1 ta maxsus belgi bo'lishi kerak): "

while True:
    password = input(msg)
    if re.match(andoza2, password):
        print("Maxfiy so'z qabul qilindi!")
        break
    else:
        print("Maxfiy so'z talabga javob berpaydi!")

# # sub — matnni almashtirish
# s2 = "Salom, aziz foydalanuvchi!"
# yangi = re.sub(r"foydalanuvchi", "Bobir", s2)
# print(yangi)

# # Amaliy mashq: faqat raqamdan iborat matnmi?


# def raqammi(s):
#     return bool(re.fullmatch(r"\d+", s))


# print("'12345' raqammi?", raqammi("12345"))
# print("'12a45' raqammi?", raqammi("12a45"))

# # Amaliy mashq: Telefon raqamini tekshirish (masalan, +998 90 123-45-67)


# def telefonmi(s):
#     return bool(re.fullmatch(r"\+998\s\d{2}\s\d{3}-\d{2}-\d{2}", s))


# print("'+998 90 123-45-67' telefonmi?", telefonmi("+998 90 123-45-67"))
# print("'998901234567' telefonmi?", telefonmi("998901234567"))

# # Amaliy mashq: Email manzilini tekshirish


# def emailmi(s):
#     return bool(re.fullmatch(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", s))


# print("'test@gmail.com' emailmi?", emailmi("test@gmail.com"))
# print("'test@@gmail.com' emailmi?", emailmi("test@@gmail.com"))

# # Amaliy mashq: Matndan barcha so'zlarni ajratib olish
# matn2 = "Salom, bu yerda bir nechta so'zlar bor!"
# sozlar = re.findall(r"\w+", matn2)
# print("Topilgan so'zlar:", sozlar)

# # Amaliy mashq: Matndan barcha katta harflarni topish
# matn3 = "Python va RE kutubxonasi Juda Qiziqarli!"
# katta_harf = re.findall(r"[A-Z]", matn3)
# print("Katta harflar:", katta_harf)
