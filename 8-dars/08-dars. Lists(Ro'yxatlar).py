# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 12:02:46 2024

08-dars. LISTS (RO'YXATALAR bilan tanishish) 

@author: uktam
"""

# Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida 
# tartiblash talab qilinishi mumkin. Buning uchun list uchun maxsus 
# .sort() metodidan foydalanamiz.

#cars = ['bmw','mercedes-benz','volvo','general motors','tesla','ferrari','audi']
#cars.sort()
#print(cars)

# #  KATTA va KICHIK HARF

# Diqqat! Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling. 
# Agar matndagi so'zlarning bosh harfi katta-kichik aralash yozilgan bo'lsa, 
# ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi. 

#cars = ['Bmw','mercedes-benz','volvo','general motors','tesla','ferrari','audi']
#cars.sort()
#print(cars)

# # TESKARI TARTIB

#  Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida
#  reverse=True  argumentini ham kiritamiz. 

#cars = ['bmw','mercedes-benz','volvo','general motors','tesla','ferrari','audi']
#cars.sort(reverse=True)
#print(cars)

# # SORTED()

# .sort() metodi ro'yxatni tartiblaydi. Ba'zida asl ro'yxat ichidagi elementlarning 
# ketma-ketligini buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun 
# sorted() funktsiyasidan foydalanamiz: 
    
#mexmonlar = ['Akmal','Azamat','Sobir','Oybek','Farrux','Ziyodillo','Ravshan']
#print("sorted() qaytargan ro'yxat : ", sorted(mexmonlar))
#print("Asl ro'yxat o'zgarmas qoldi: ", mexmonlar)
#print(sorted(mexmonlar, reverse = True))

# sorted() funktsiyasi yordamida teskari tartiblash uchun ham 
# reverse=True argumentini beramiz:
# asl ro'yxatdagi qiymatlar o'zgarmaydi

# # SONLI RO'YXATLAR

# Yuoqridagi ikki usul bilan sonli ro'yxatlarni ham tartiblashimiz mumkin: 

#ages = [15,5,19,23,17,7,33,83,46,70,18,]
#ages.sort()
#ages.sort(reverse=True)
#print(ages)
#print(sorted(ages))
#print(sorted(ages, reverse = True))

# # RO'YXATNI ORTIDAN BOSHLAB CHIQARISH

# Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin.
# Buning uchun .reverse() metodidan foydalanamiz.

#fruits = ['pear','banana','avocado','Mango','Cherry','lemon','Watermelon']
#fruits.reverse()
#print(fruits)

# # RO'YXAT UZUNLIGI

# Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun 
# len() funktsiyasidan foydalanamiz:
    
#fruits = ['pear','banana','avocado','Mango','Cherry','lemon','Watermelon']
#print("Elementlar soni: " , len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

# # range() FUNKTSIYASI

# Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. 
# list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:

#sonlar = list(range(0,10))
#print(sonlar)

# Yuqoridagi misolda range(0,10) funktsiyasi 0 dan 9 gacha sonlar ketma-ketligini 
# shakllantirdi, list(range(0,9)) esa bu ketma-ketlikni ro'yxatga aylantirdi.

# Diqqat! E'tibor qiling range()
# funktsiyasi ikkinchi indeksdan bitta avval to'xtaydi.

# # RANGE VA QADAM

# range() yordamida qadamni ham berishimiz mumkin:

#juft_sonlar = list(range(0,20,2))
#toq_sonlar = list(range(1,20,2))
#print("Juft sonlar; " , juft_sonlar)
#print("Toq sonlar; " , toq_sonlar)

# Agar sonlar ketma-ketligi 0 dan boshlansa, range() funktsiyasida yakuniy indeksni 
# ko'rsatish kifoya. Misol uchun range(0,10) emas range(10) deb yozsak ham bo'laveradi.

# #  SONLI RO'YXAT USTIDA SODDA AMALLAR

# Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. 
# Misol uchun ro'yxatdagi eng kichik sonni topish uchun 
#min()
# funktsiyasidan, eng katta sonni topish uchun esa 
#max()
# funktsiyasidan, sonlarning yig'indisini topish uchun esa 
#sum()
# funktsyasidan foydalansak bo'ladi:

# min(), max(), sum()

#narxlar = [22000,34000,1500,12000,5500,2700,9999,56400,123500,7500]
#arzon = min(narxlar)
#qimmat = max(narxlar)
#jami = sum(narxlar)
#print("Eng arzon narx: ", arzon, "\nEng qimmat narx: ", qimmat, "\nJami summa: ", jami)
#print("Narxlar soni:", len(narxlar), "ta")

# # RO'YXATNI KESISH

# Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin,
# deylik biz quyidagi cars degan ro'yxatdan birinchi 3 ta elementni ajratib olmoqchimiz,
# buning uchun biz boshlang'ich va oxirgi indekslarni beramiz:

#cars = ['bmw','mercedes-benz','volvo','general motors','tesla','ferrari','audi']
#my_cars = cars[1:4]# 1-indeksdan boshlab 3ta element ajratib olamiz. 4- indeks kirmaydi
#print(my_cars)
#my_cars = cars
#my_cars.remove('volvo')
#print(my_cars)
#my_cars.append('volvo')
#print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
#print(cars[:3]) # Ro'yxat boshidan 3-gacha kesadi (0,1,2,)
#print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# # RO'YXATDAN NUSXA OLISH

# Dastur davomida biror ro'yxatdan nusxa olish talab qilinishi mumkin. 
# Buning uchun biz tenglik(=) belgisidan foydalansak bo'ladimi? 
# Quyidagi misolga e'tibor bering:
    
#sonlar = [1,2,3,4,5,6,7,8,9,10,11,12]    
#sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
#sonlar2.append(13) #  sonlar2 ga 13 sonini qo'shamiz
#sonlar2.append(14) # sonlar2 ga 14 sonini qo'shamiz
#print("Bu sonlar ro'yxati: ",sonlar)
#print("Bu esa sonlar2 ro'yxat: ", sonlar2)

# Natija biz kutgandek chiqdimi? Yo'q. Biz 6 va 7 sonlarini sonlar2 degan ro'yxatga
# qo'shgan edik, lekin bu ikki son sonlar degan asl ro'yxatga ham qo'shilib qoldi. 

# Demak yuqorida biz sonlar2=sonlar deb yozgan komandamiz yangi ro'yxat yaratish o'rniga, 
# ikkala o'zgaruvchini ham bitta ro'yxatga bog'lab (yo'naltirib) qo'ydi. 
# Biz sonlar yoki sonlar2 ustida bajargan amallarimiz aslida bitta ro'yxat ustida
# bajarilyapti.

#cars = ['bmw','mercedes-benz','volvo','general motors','tesla','ferrari','audi']
#my_cars = cars
#print(my_cars)
#print(my_cars)
#my_cars.append('Jeep')
#print(my_cars)
#my_cars[0] = 'Hyunadi'
#my_cars[2] = 'bmw'
#print(my_cars)

# Unda, qanday qilib ro'yxatdan nusxa olamiz? Buning uchun yuoqirdagi ka'bi ro'yxatni
# kesish usulidan foydalanamiz. Faqatgina, kvadrat qavs ichida ikkala indeksni
# ham ko'rsatmasdan, bo'sh qoldiramiz:

# cars = ['bmw','mercedes-benz','volvo','general motors','tesla','ferrari','audi']
# my_cars = cars[:]
# my_cars.remove('bmw')

# # TUPLES - O'ZGARMAS RO'YXAT

# Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin.
# Pythonda bunday ro'yxatlar tuples deb yuritiladi. Tuple ichidagi qiymatlarni bir marta, 
# dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. List dan farqli ravishda,
# Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:

# # TUPLES - O'ZGARMAS RO'YXAT

#tomonlar = (5,12,20,35,55,2)
#print(tomonlar)

# Tuple ichidagi elementlarga huddi ro'yxat elementlariga murojat qilingani 
# kabi murojat qilinaveradi:

#toys = ('bus','car','bear','dino','snake','lizard')
#print(toys[0])
#print(toys[-1])
#print(toys[2:5])
#print(toys[3:])
#toys = ('bus','car','bear','dino','snake','lizard')

# TypeError: 'tuple' object does not support item assignment
#toys[3] = 'dragon'
#toys.append('teddy')# AttributeError: 'tuple' object has no attribute 'append'
#toys.remove('bear')# AttributeError: 'tuple' object has no attribute 'remove'
#print(toys)

# Demak yuqorida ko'rib turganingiz kabi, bu operatsiya xatolikka olib keldi. 
# Shu kabi ro'yxatdan biror elementni o'chirish yoki yangi element qo'shish ham mumkin emas.

## Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni 
## list() funktsiyasi yordamida List (oddiy ro'yxat) ko'rinishiga keltirib olish, 
## o'zgarishlarni bajarsih va qaytarib tuple() funktsiyasi yordamida 
## o'zgarmas ro'yxatga o'tkazish mumkin:

#toys = ('bus','car','bear','dino','snake','lizard')# o'zgarmas ro'yxat
#toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz:
    
#toys.append('dragon')
#toys.append('teddy') 
#toys.remove('bus')   
#toys[1]  = 'mcqueen'   
#toys = tuple(toys) 

#print(toys)

###   A M A L I Y I Y O T  ###

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#davlatlar = ["Turkiya", "Malayziya", "Yaponiya", "Ispaniya", "Angliya", "Misr", "Falastin"]

# Ro'yxatning uzunligini konsolga chiqaring
#print(len(davlatlar))

#print("Davlatlar soni " , len(davlatlar), "ta")

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#print(sorted(davlatlar))
#print(sorted(davlatlar, reverse = True))

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#print(davlatlar)
#davlatlar.reverse()# Ro'yxatni teskarisiga (oxiridan boshiga qarab) chiqaradi
#print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
#harflar = ['Z','C','K','O','A','L','D','M','G','T','F','W']
#harflar.sort()
#print(harflar)
#harflar.sort(reverse=True)# Ro'yxatni teskari tartibda chiqaradi
#print(harflar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#sonlar = [120,1200,2]
#sonlar = list(range(120,1200,2))
#print(list(range(120,1200,10)))

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
#jami = sum(sonlar)
#print(jami)
#katta_son = max(sonlar)
#kichik_son = min(sonlar)

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
#print(max(sonlar) - min(sonlar))

# Ro'yxatdagi elementlar sonini hisoblang
#print(len(sonlar))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

#print(sonlar[:20])
#print(sonlar[-20:])
#print(sonlar[530:550])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

#taomlar = ['osh','manti','tok oshi','kabob','xonim']

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
#nonushta = taomlar[:]
#nonushta.remove('osh')
#nonushta.remove('xonim')
#nonushta.remove('kabob')
# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
#nonushta.append('non va qaymoq')
#nonushta.append('salad')
#nonushta.append('tuxum vs sasiska')

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
#print(taomlar)
#print(nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va 
# nonushta[0] = "non" deb qiymat berib ko'ring.

#nonushta = tuple(nonushta)
#nonushta['non']

# Ynagi mashqlar bilan boyotildi

# .sort() methodi ro'yxatni alifbo tartibida tartiblaydi, ro'yxatni joyida o'zgartiradi (in-place)

cars = ['Bmw', 'mercedes-benz', 'volvo', 'General motors', 'tesla', 'ferrari', 'audi',
    'toyota', 'honda', 'nissan', 'ford', 'chevrolet', 'volkswagen', 'hyundai',]

# cars.sort(key=str.lower) # Barchasini kichik harflarda solishtiradi
# print(cars)
# cars.sort(reverse=True) # Ro'yxatni teskari tartibda tartiblaydi, original ro'yxat o'zgaradi
# print(cars)

# sorted() funktsiyasi yangi tartiblangan ro'yxat qaytaradi, original ro'yxat o'zgarmaydi

# print(sorted(cars))
# sorted_cars = sorted(cars, key=str.lower) # Original ro'yxat o'zgarmaydi
# print(cars)

fruits = ['olma', 'anor', 'banan', 'uzum', 'nok', 'shaftoli', 'mandarin',
    'limon', 'gilos', 'qulupnay', 'behi', 'xurmo', 'anjir']
# sorted_fruits = sorted(fruits)
# print("Tartiblangan: ", fruits)

# reversed_fruits = sorted(fruits, reverse=True) # Original list o'zgarmagan

# print("Tartiblangan, original list o'zgarmagan: ", sorted_fruits)

sonlar = [19, 54, 98, 23, 71.5, 8.0, 123, 16, -12.5, -0.5, 2]
# sonlar.sort(reverse=True) # Teskari tartiblaydi, original list o'zgaradi
# reversed_sonlar = sorted(sonlar, reverse=True) # teskari tartiblaydi original list o'zgarmaydi
# print(sonlar[::-1]) # Sonlarni faqat terskari tartibda chiqarish kerak bo'lsa, tartiblanmagan xolda

# reverse() funksiyasi ro'yxatni ortidan boshlab chiqarish uchun ishlatiladi
# cars.reverse()
# print(cars)

# len() funksiyasi ro'yxat uzunligini qaytaradi
# print(f"Length of cars list: {len(cars)}")
# print("Sonlar ro'yxati: ", len(sonlar), "ta")
# length = len(sonlar)

# range() funksiyasi ma'lum bir oraliqdagi sonlar ro'yxatini qaytaradi

# numbers = list(range(0, 10))
# print(numbers)
# numbers.reverse()
# print(numbers)

# odd_numbers = list(range(1,20,2))
# print(odd_numbers)

# even_numbers = list(range(2,20,2))

# max_value = max(even_numbers)

# narhlar = [1000, 3500, 7000, 19500, 1127000, 120000, 5500]

# min_price = min(narhlar)
# max_price = max(narhlar)
# sum_prices = sum(narhlar)
# print(f"Eng arzon narh: {min_price}. \nEng qimmat narh: {max_price} \nJami: {sum_prices}")

# Ro'yxatni keshish

# my_cars = cars[0:3]
# print(f"Garajdagi moshinalar: {my_cars}")
# print("Garjdagi moshinalar: ", my_cars)

# join() metodi yordamida ro'yxatni stringga aylantirib, katta-kichik harf muammosidan qutulishimiz mumkin

# red_cars = cars[:5]
# print(f"Garajdagi moshinalar: {', '.join(red_cars)}")
# print("Garjdagi moshinalar: " + ", " .join(red_cars))

"""
  String Kesmalari (Slicing)
 [start:stop:step] sintaksisi yordamida stringning bir qismini ajratib olish mumkin.

  Asosiy kesma qoidalari:
1. s[start:stop] - start indeksidan stop indeksigacha (stop kirmaydi)

2. s[start:] - startdan oxirigacha

3. s[:stop] - boshidan stopgacha

4. s[:] - butun string

5. s[::step] - qadam bilan olish
"""

# print(cars[3:7]) # (3 dan 6 gacha )
# print(cars[10:]) # (10 dan oxirgacha) 
# print(cars[:5]) # (boshidan 5 gacha) 
# print(cars[:])  # (butun list)
# print(cars[::3]) # (boshidan xar 3 - element) 
# print(cars[-5:]) # (oxiridan 5 ta element)
# print(cars[:-7]) # (oxiridan 7 tasini olmaydi ro'yxatga) 
# print(cars[::1]) # (Ro'yxatni teskari qaytaradi) 
# print(cars[10:4:-1]) # (10 dan 4 gacha teskari) 
# print(cars[1:9:2]) # (1 dan 9 gacha 2 qadam bilan)

# Ro'yxatdan Nusxa olish

# my_cars = cars
# my_cars.remove("audi")
# my_cars[0] = "tesla 3"
# print(my_cars)
# print(cars)

"""
Ro'yxatdan nusxa olish uchun yuoqirdagi ka'bi ro'yxatni KESISH usulidan [:] foydalanamiz. 
Faqatgina, kvadrat qavs ichida [:] ikkala indeksni ham ko'rsatmasdan, bo'sh qoldiramiz:
"""
# my_cars = cars[:]
# my_cars = my_cars[:-5]

# cars.remove("audi")
# cars.remove('volvo')

# print("These are my cars: ", my_cars)
# print(cars)

"""
  Tuples - bu Python dasturlash tilidagi o'zgarmas (immutable) ma'lumotlar strukturasi. 
  List (ro'yxat)larga o'xshash, lekin ularni yaratilgandan keyin o'zgartirib bo'lmaydi.

Asosiy Xususiyatlari:
1. O'zgarmaslik - Yaratilgandan keyin elementlarni o'zgartirib bo'lmaydi

2. Qavs bilan yoziladi - Odatiy holda () ichida yoziladi, lekin qavssiz ham yaratish mumkin

3. Har xil turdagi ma'lumotlarni saqlashi mumkin - Bir tuple ichida turli turdagi 
   ma'lumotlar bo'lishi mumkin
"""
# Oddiy tuple
toys = ('bus', 'mcqueen', 'dino', 'snake', 'lizard', 'car', 'train')
# print(toys[0]) # bus
# print(toys[-1]) # train
# print(toys[1:4]) # ('mcqueen', 'dino', 'snake')
# print(f"Toys in the warehouse: {', '.join(toys)}")

# Qavssiz tuple 
my_toys = 'bus', 'mcqueen', 'train', 'car'
# print("My toys: "+", " .join(my_toys).title()) # My toys: Bus, Mcqueen, Train, Car

# Faqat 1 lementli tuple (vergul bilan)
outdated_toys = ('dino',)
# print('Outdated toys: '+', ' .join(outdated_toys).upper()) # Outdated toys: DINO

# Bu xato beradi chinki bu o'zgarmas 
#toys[0] = "doll" # TypeError: 'tuple' object does not support item assignment
# toys.append("ball") # AttributeError: 'tuple' object has no attribute 'append'

"""
To'g'ridan to'g'ri tupleni orzgartirib yoki element qo'shib bo'lmaydi, lekin muqobil yo'l mavjud:
"""
original = (1, 2, 3)
new_element = 4

# + opratori yordamida
new_tuple = original + (new_element,)
print(new_tuple) # (1, 2, 3, 4)

# yoki 
new_tuple = (*original, new_element)
print(new_tuple) # (1, 2, 3, 4)

# Listga o'tkazib, o'zgartirib, qayta tuple qilish:
toys = list(toys)
toys.append("duck")
toys = tuple(toys)
print(toys) # ('bus', 'mcqueen', 'dino', 'snake', 'lizard', 'car', 'train', 'duck')

# Bir necha element qo'shish

colors = ('green', 'red', 'white')
new_colors = colors + ('blue', 'black')
print(new_colors) # ('green', 'red', 'white', 'blue', 'black')


