"""
Created on Thu Jun 19 12:29:14 2025

33-dars. Fayllar bilan ishlash. Pickle

@author: uktam
"""
# Fayllar bilan ishlash: Pi sonini o'qish va floatga o'tkazish
# 1. Asosiy usul (oddiy variant)

with open('pi.txt') as file:
    pi = file.read()  # Fayldan ma'lumotni o'qib olamiz
    
print(pi)  # O'qilgan ma'lumotni ko'rsatamiz

pi = pi.rstrip()  # O'qilgan matnning oxiridagi bo'shliq va \n belgisini olib tashlaymiz
pi = pi.replace('\n','')  # Matn ichidagi barcha yangi qator belgilarini olib tashlaymiz
pi = float(pi)  # Matnni float (o'nlik son) ga o'tkazamiz
print(pi)  # Float ko'rinishdagi pi sonini chiqaramiz
'''
Izoh:
Bu eng oddiy usul bo'lib, faqat faylda to'g'ri formatdagi son borligiga ishonch hosil qilinganda ishlatiladi.
Agar faylda son bo'lmasa yoki noto'g'ri belgilar bo'lsa, dastur xato berib to'xtab qoladi.
.rstrip() faqat oxiridagi bo'shliqlarni olib tashlaydi, .strip() esa bosh va oxiridagi bo'shliqlarni olib tashlaydi.
'''

# 2. Xatolarni boshqarish bilan ishlash (tavsiya etilgan usul)

with open('pi.txt') as file:
    pi = file.read()  # Fayldan ma'lumotni o'qib olamiz
    
print(pi)  # O'qilgan ma'lumotni ko'rsatamiz

pi = pi.strip()  # Matnning boshidagi va oxiridagi barcha bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','')  # Matn ichidagi barcha yangi qator belgilarini olib tashlaymiz
pi = pi.replace(' ','')   # Matn ichidagi barcha bo'shliqlarni ham olib tashlaymiz

try:
    pi_float = float(pi)  # Matnni floatga o'tkazishga urinamiz
    print(pi_float)  # Agar muvaffaqiyatli bo'lsa, natijani chiqaramiz
except ValueError:
    # Agar floatga o'tkazish mumkin bo'lmasa, xato xabarini chiqaramiz
    print("Faylda noto'g'ri formatdagi ma'lumot bor. Faqat sonlarni o'qiydigan qiling.")
'''
Izoh:
Bu eng yaxshi amaliyot hisoblanadi, chunki u xatolarni boshqarishni o'z ichiga oladi.
.strip() metodi .rstrip() dan ko'ra yaxshiroq, chunki u bosh va oxiridagi bo'shliqlarni olib tashlaydi.
try-except bloki dasturni xatolardan himoya qiladi.
Agar faylda son bo'lmasa, dastur to'xtamaydi, balki foydalanuvchiga xato haqida ma'lumot beradi.
'''

# 3. Qisqartirilgan va optimallashtirilgan usul

with open('pi.txt') as file:
    # Bir qatorda faylni o'qish va matnni tozalash
    pi = file.read().strip().replace('\n', '')

try:
    pi_float = float(pi)  # Floatga o'tkazishga urinamiz
    print("Float qiymati:", pi_float)  # Muvaffaqiyatli natijani chiqaramiz
except ValueError:
    # Xato yuz berganda xabar chiqaramiz
    print("Xato: Faylda son emas, boshqa belgilar bor!")
'''
Izoh:
Bu eng ixcham va Python uslubiga mos keladigan yechim.
Barcha operatsiyalar bir nechta qatorda bajariladi.
try-except bloki hali ham xatolarni ushlab turadi.
Chiqarish biroz ko'proq ma'lumot beradi, bu foydalanuvchiga yaxshiroq 
tushunish imkonini beradi.
'''