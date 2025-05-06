# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:39:18 2024

#09-dars: FOR LOOP

@author: uktam
"""

#mexmonlar =["Adham","Abduvali","Sohib","Ilhom","Zarif"]
#print("Salom", mexmonlar[0])
#for mexmon in mexmonlar:
#    print("Assalomu aleykum", mexmon)
#    print("Xush kelibsiz! ", mexmon)
    
#mexmonlar =["Adham","Abduvali","Sohib","Ilhom","Zarif"]
#for n in mexmonlar:
#    print("Assalomu aleykum", n)
    
#mexmonlar =["Adham","Abduvali","Sohib","Ilhom","Zarif"]
#for mexmon in mexmonlar:
#    print(f"Hurmatli {mexmon}, sizni 20 - Dekabr kuni nahorga oshga lutfan taklif etamiz. ")
#    print("Xurmat bilan Palonchiyevlar oilasi\n")
    
# Yuqoridagi kodda 2-qator bu tsikl boshi deyiladi. Aynan shu qator kodimiz 
# nech marta takrorlanishini aniqlaydi. Bizning holatimizda tsikl mehmonlar 
# ro'yxati ichidagi elementlar tugagunga qadar takrorlanadi. 
# Tsikl boshlanishi ikki nuqta (:) bilan tugaydi. Undan keyingi 3 va 4-qatorlar 
# bu tsiklning badani deyiladi.  

# Tsikl badani surilish (indentation) bilan ajratiladi, ya'ni tsiklning 
# takrorlanuvchi qismi asosiy koddan bir muncha o'ngroqqa surilgan bo'ladi. 
# Agar biz mana shu surilishni tark qilsak kodimiz xato beradi:


#mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
#for mehmon in mehmonlar:
#print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#print("Hurmat bilan, Palonchiyevlar oilasi\n")

# Natija: IndentationError: expected an indented block

# Ko'rib turganingizdek for dan keyingi qatorni o'ngga surmaganimiz uchun 
# indentation error (surishda xatolik) degan xabarni oldik.

# Shunigdek, ko'pchilik yo'l qo'yadigan yana bir xato, qo'shimcha qatorlarni 
# surish esdan chiqishi:
    
#mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#print("Hurmat bilan, Palonchiyevlar oilasi\n")  


#   Natija:

#Hurmatli Ali, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmatli Vali, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmatli Hasan, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmatli Husan, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmatli Olim, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#urmat bilan, Palonchiyevlar oilasi 🠄🠄🠄

# Yuqoridagi kodimizda 4-qatorni o'ngga surmaganimiz uchun, Python bu qatorni 
# tsikl tashqarisida deb qabul qildi va faqatgina 1 marta, tsikl tugaganidan so'ng bajardi. 

# Huddi shu kabi agar takrorlanishi kerak bo'magan kodni tsikldan so'ng o'ngga 
# surib qo'ysak Python bu qatorni tsiklning tarkibida deb hisoblab, qayta-qayta bajaradi:
    

#mexmonlar =["Adham","Abduvali","Sohib","Ilhom","Zarif"]
#for mexmon in mexmonlar:
#    print( mexmon)

#    print(mexmonlar)  # bu qator tsikl tashqarisida bo'lishi kerak edi

#sonlar = list(range(1,11))
#for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng")

#karra = list(range(2,10))
#for jadval in karra:
#    print(f"{jadval} ning kvadrati {jadval**2} ga teng")

#sonlar = list(range(11))# 1dan 10 gacha sonlar ro'yxatini yaratamiz
#sonlar_kvadrati = [] # Bo'sh ro'yxat yaratamiz
#for son in sonlar: # Sonlardagi xar bir son uchun
#    sonlar_kvadrati.append(son**2) # uning kvadratini xisoblab, sonlar_kvatratiga yuklaymiz

#print(sonlar)
#print(sonlar_kvadrati)

# for va input() birga

#dostlar = [] # Bo'sh ro'yxat
#print("5ta eng yaqin do'stingizni kim? \n")
#for n in range(5): # n bu yerda 0 dan 4 gacha bo'lgan qiymatlar oladi
#    dostlar.append(input(f"{n+1} - do'stingiz ismini kiriting: \n"))

#print(dostlar)    
#print(f"BU sizning d'stlaringiz ro'yxati: {dostlar.title()}") 
'''
Kodni tahlil qilamiz:

1-qatorda bo'sh dostlar ro'yxatini yaratdik

2-qatorda ekranga "5 ta eng yaqin do'stingiz kim?" degan xabarni chiqardik

3-qatorda tsiklni boshladik. range(5) funktsiyasi 0 dan 5 gacha sonlar 
ketma-ketligini yaratadi (0,1,2,3,4) tsikl esa n shularning har biriga teng bo'lib chiqquncha davom etadi. 

4-qatorda tsikl badani kelgan. Bu yerda biz foydalanuvchidan n+1 do'stingizni 
kiriting deb so'radik. Nima uchun n+1 (n emas)? Sababi n 0 dan 4 gacha qiymatlarni oladi, foydalanuvchiga tushunarli bo'lishi uchun esa biz "0-do'stingizni ismini kiriting:" deb emas, balki n+1 ya'ni 1-ismni kiriting deb murojat qilyapmiz.

5-qatorda shakllangan ro'yxatni konsolga chiqardik.  

for tsikli har qanday dasturlash tilining eng muhim qismlaridan hisoblanadi 
va biz bu operatoraga hali takror-takror qaytamiz. 
'''

"""
Practice
Multiplication table (from 1 to 10) in Python
"""
# num = 2

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
#for i in range(1, 10):
#   print(num, 'x', i, '=', num*i)

### M U S T A Q I L  ISH
#x = int(input("Enter the number for the multiplication table: ")) 
#y = int(input("Enter the number of rows for the multiplication table: ")) 
#for i in range(1, y + 1): 
#    result = x * i 
#    print(f"{x} * {i} = {result}") 
#else: 
#    if y > 20: print("The number of rows has been limited to 20. ")

# 1. Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir
#    ismga takrorlanuvchi xabar yozing
#ismlar = ['Sobir','Akmal','Oybek','Asad','Sardor','Komil']
#for ism in ismlar:
#    print("Salom do'stim", ism , " teatrga xush kelibsiz! ") # 1- variant
#    print(f"Salom do'stim {ism} teatrga xush kelibsiz! ") # 2- variant
    
# 2. Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi"
#    degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#for n in ismlar:
#    print("Salom", n)
#print(f"Kod {len(ismlar)} marta takrorlandi")

# 3. 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
#    Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#sonlar = list(range(11,100,2))
#for n in sonlar:
#    print(n**3)

# 4. Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, 
#    va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#kinolar = []
#print("5 ta eng sevimli kinoyiz? \n>>>")
#for kino in range(5):
#    kinolar.append(input(f"{kino+1}-sevgan kinoyiz ?\n>>>"))
#print(kinolar)

# 5. Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
#    va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. 
#    Ro'yxatni konsolga chiqaring.

#suxbatdoshlar = int(input("Bugun necha kishi bilan suxbat qildingiz? \n>>>"))
#ismlar = []
#for s in range(suxbatdoshlar):
#    ismlar.append(input(f"Bugun {s+1}- suxbat qilgan odamiz kim edi ?\n>>>" ))    
#print(ismlar)

#show = int(input("Bugun teatrda nechta spektakl bor?\n>>>"))
#shows = []
#for n in range(show):
#    shows.append(input(f"Bugungi o'ynagan {n+1}- spektakliz? "))
#print(shows)    


# mexmonlar = ["Ali", "Olim", "Shokir", "Bobur", "Mirzo", "Mustafo"]
# for mexmon in mexmonlar:
#     print("Salom", mexmon)
    
# friends = ["Alisher", "Kamron", "Bekzod", "Jasur", "qobil", "Jobir"]
# for friend in friends:
#     print(f"Xurmatli do'stim {friend}, sizni 22-dekabr kuni nahorga oshga taklif qilaman!")
#     print("Xurmat bilan, Sattorovlar oilasi\n")

# numbers = list(range(2,10))
# for num in numbers:
#     print(f"{num} ning kvadrati {num*2} ga teng\n")
    
# Karra jadvali

# numbers = list(range(2, 10))
# for num in numbers:
#     for i in range(2, 10):
#         print(f"{num} X {i} = {num * i}")
#     print()  # Har bir son uchun bo'sh qator qo'shamiz

  # Karra jadvali  variant 2
# for num in range(2, 10):
#     print(f"\n{num} karra jadvali:")
#     for i in range(2, 10):
#         print(f"{num} x {i} = {num * i}")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)

dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingiz ismini kiriting: ").title())
# print('\n' .join(dostlar))
print(*dostlar, sep=', ')