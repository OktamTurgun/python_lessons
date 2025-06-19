"""
Created on Thu Jun 19 12:29:14 2025

33-dars. Fayllar bilan ishlash. Pickle

@author: uktam
"""
#!!! Tavsiya qilingan oddiy usul
# with open('pi.txt') as file:
#     pi = file.read()
    
# print(pi)

# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)

# Exercise: 2 Xatolarni boshqarish bilan ishlash (tavsiya etilgan usul)
with open('pi.txt') as file:
    pi = file.read()
    
print(pi)

pi = pi.strip()  # bosh va oxiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','')  # yangi qator belgilarini olib tashlaymiz
pi = pi.replace(' ','')   # bo'shliqlarni ham olib tashlash kerak bo'lishi mumkin

try:
    pi_float = float(pi)  # float ga o'girishga harakat qilamiz
    print("Float qiymati:", pi_float)
except ValueError:
    print("Faylda noto'g'ri formatdagi ma'lumot bor. Faqat sonlarni o'qiydigan qiling.")

# Exercise: 3 Qisqartirilgan va optimallashtirilgan usul
# with open('pi.txt') as file:
#     pi = file.read().strip().replace('\n', '')

# try:
#     pi_float = float(pi)
#     print("Float qiymati:", pi_float)
# except ValueError:
#     print("Xato: Faylda son emas, boshqa belgilar bor!")