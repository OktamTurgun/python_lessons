# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:47:32 2024
Lug'at elementlari bilan ishlash
@author: uktam
"""
'''
.items() metodi. elementlar deb tarjima qilinadi
Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.
'''
# talaba_0 = {
#    'familiya':'shamshiyev',
#   'yosh':'22',
#    'fakultet':'tarix',
#    'kurs':'4',
#    'manzil':'xorazm'
#    }
# print(talaba_0.items())

# Bu metodni to'g'ridan-to'g'ri emas, for tsikli yordamida chaqirish orqali lug'atdagi 
# barcha elementlarni tushunarliroq shaklda ko'rishimiz mumkin.

#for key, value in talaba_0.items():
#    print(f"Kalit: {key}")
#    print(f"Qiymat: {value.title()}\n")

phones = {
    'ali':'Iphone X',
    'vali':'samsung A 50',
    'olim':'huawei 250',
    'shokir':'Iphone 14 pro',
    'tohir':'xiomi redmi 10 pro'    
    }
# for key, value in phones.items():
#    print(f"{key.title()} ning telefoni {value.upper()}\n")

'''.keys()''' 
products = {
    'anor':14000,
    'uzum':20000,
    'non':30000,
    'tarvuz':12000,
    'shaftoli':25000,
    }
print(products.keys())
           
print('Do\'kondagi maxsulotlar:') # 1- variant
for product in products.keys():
   print(product.title())
           
print('Do\'kondagi maxsulotlar:') # 2- variant
for product in products:
   print(product.title())

bozorlik = ['anor','uzum','qovoq','tarvuz','non','baliq']
for product in products:
   if product in bozorlik:
       print(f"{product} {products[product]} so'm.")

for buyum in bozorlik:
   if buyum not in products:
       print(f"Iltimos do'koningizga {buyum} xam olib keling")

'''LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH'''

print("Do'konimizdagi maxsulotlar: ")
for maxsulot in sorted(products):
   print(maxsulot.title())
    
'''
.velues(). qiymatlar deb tarjima qilinadi    
Agar lug'atdagi qiymatlarni chiqarish talab qilinsa .values() metodidan foydalanishimiz mumkin.
'''   
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")    
# for tel in sorted(phones.values()):    
#    print(tel) 
    
'''
Yuqoridagi usul bilan qiymatlarni chiqrganimizda, lug'atdagi barcha qiymatlar 
chiqib keladi. Agar, biror qiymat ko'p marta qaytarilsa, konsolga ham ko'p
marta chiqib keladi.
'''
# Quyidagi misloni ko'raylik:
telefonlar = {
    'akmal':'Samsung galaxy s4',
    'shokir':'huawei E110',
    'Botir':'nokia 1200',
    'adham':'philips',
    'ilhom':'Iphone 14 pro max',
    'ziyoda':'Xiomi redmi 10 pro',
    'zarif':'LG 250',
    'Bobur':'Iphone 10 ultra',
    'dasha':'Samsung galaxy s4',
    'aziz':'Xiomi redmi 10 pro',
    'surayyo':'huawei E110',
    'yorqin':'Iphone 14 pro max',
    }
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for phone in telefonlar.values():
#    print(phone)

'''
Yuoqirdagi kodning natijasiga e'tibor bersanigz, bir nechta foydalanuvchilar Samsung galaxy s4, huawei E110 va Iphone 14 max pro  
telefonidan foydalanishar ekan, va bu modellar qayta-qayta konsolga chiqdi. 
Buning oldini olish uchun set() funktsiyasidan foydalanishimiz mumkin.
'''
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for phone in set(telefonlar.values()):
#    print(phone)

'''
  Pythonda set yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta 
elementlarni saqlashga mo'ljallangan. Lug'at va ro'yxatdan farqli ravishda, 
set ichidagi elementlar biror tartibda saqlanmaydi, va ularga indeks orqali murojat qilib
bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmaydi.
'''
# toys = {"ball","bear","car","teddy","lamp","ball","car"}
# print(toys)

# Practices
'''
1. Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida 
chiroyli qilib konsolga chiqaring.
''' 
python = {
    'string':'matn',
    'integer':'butun son',
    'float':'onlik son',
    'list':'royxat',
    'for':'takrorlash operatori',
    'else':'aks xolda',
    'tuple':'ozgarmas royxat',
    '.sort()':'tartiblash metodi',
    '.revers()':'boshini oxiriga aylantish metodi',
    'len()':'royxatni uzunligini aniqlash funksiyasi',
    'range()':'malum oraliqdagi sonlar ketma- ketligini yaratuvchi funksiya',
    'lower()':'xar bir xarfni kichik xarfga ozgartiradi',
    'title()':'matndagi xar bir soz birinchi xarfini katta bilan yozadi'
    }
print("Python izohli lug'ati: ")
for key, value in sorted(python.items()):
   print(f"{key.title()} - {value}\n")

'''
2. Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
   keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
'''
countries = {
    'avstria':'vena',
    'fransia':'parij',
    'italia':'rim',
    'uzbekistan':'toshkent',
    'eron':'texron',
    'mexico':'mexico',
    'rassia':'moscow',
    'xitoy':'pekin',
    'kolumbia':'bagota',
    'misr':'qohira',
    'iroq':'bagdad'
    }
print("Dunyo davlatlari:")
for davlat, poytaxt in sorted(countries.items()):
    print(f"Davlat: {davlat.title()} -  poytaxti {poytaxt.title()}")

'''
3. Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini
konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
"Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
'''
davlat = input('\nQaysi davlatning poytaxtini bilishni istaysiz? ').lower()
poytaxt = countries.get(davlat)
if poytaxt == None:
    print("Kechirasiz bizda bu xaqida ma'lumot yo'q!")
else:
   print(f"{davlat.upper()}ning - poytaxti {poytaxt.title()}")

''''''
country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = countries.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

'''
4. Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni 
menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda 
"bizda bunday taom yo'q" degan xabarni chiqaring.
'''
menu = {
        'osh':'25000',
        'lagman':'30000', 
        'bifshteks':'23000',
        'shashlik':'15000',
        'somsa':'8000', 
        'salat':'5000',
        'non':'5000',
        'shorva':'22000', 
        'tushonka':'40000',
        'baliq 100 gr':'17000',
        'mastava':'15000', 
        'qozon kabob':'30000',
        'tabaka 100 gr':'12000',
        'limon choy':'7000'
        }
print("3 ta taom buyurtma bering:")
zakaz = []

for n in range(3):
    zakaz.append(input(f"{n+1} - taom:").lower())

for buyurtma in zakaz:
    if buyurtma in menu:
        print(f" {buyurtma.title()} {menu[buyurtma]}")
    else:
        print(f"Kechirasiz bizda {buyurtma} yo'q.")

''' .items() '''

student_0 = {
    'name': "Ulug'bek",
    'lastName': 'Kamolov',
    'age': 23,
    'field': 'computer science',
    'degree': 4
    }
# print(student_0.items())

''''''
# for key, value in student_0.items():
#     print(f"Key: {key.title()} \n"
#           f"Value: {str(value).title()}\n") # Agar qiymat integer(son) bo'lsa string(matn) qilamiz

''''''
# for kalit, qiymat in student_0.items():
#     if isinstance(qiymat, str): # Agar qiymat faqat matn bo'lsa
#         print(f"Key: {kalit.title()}\n"
#               f"Value: {qiymat.title()}\n")
#     else: # Agar integer yoki boshqa type of date bo'lsa
#         print(f"Key: {kalit.title()}\n"
#               f"Value: {str(qiymat)}\n")

''''''
phones = {
    'john': 'Samsung Galaxy S25 Ultra',
    'alex': 'Apple iPhone 16 Pro Max',
    'mateo': 'Huawei Mate X6',
    'henry': 'Google Pixel 9 Pro',
    'william': 'Samsung Galaxy S25 Edge'
    }
# for name, phone in phones.items():
#     # print(f"User: {name.title()}\n"
#     #       f"Phone: {phone}\n")
#     print(f"{name.title()}'s phone {phone}\n")
    
''' .keys() '''

products = {
    'olma':13000,
    'anor':22000,
    'gilos':25000,
    'tuxum':50000,
    'sabzi':5000,
    'banan':22500,
    'shaftoli':19000,
    'non':5000,
    'baliq':30000,
    'sut':9000,
    'piyoz':4000
    }

# print(products.keys())

# print("\nProducts in the shop:")
# for product in products.keys():
#     print(product.title())

'''
Faqatgina ro'yxatdagi kalit so'zlarni olmoqchi bo'lsak,
 .keys() metodini yozish shart emas
'''
# print("\nProducts in the shop:")
# for product in products:
#     print(product.title())
    
''''''
bozorlik = [
    'non',
    'uzum',
    'baliq',
    'tuxum',
    'sut',
    'un',
    'piyoz'
    ]
# for maxsulot in products:
#     if maxsulot in bozorlik:
#         print(f"{maxsulot.title()} {products[maxsulot]} so'm")
        
''''''
# for maxsulot in bozorlik: # Bozorlik ro'yxatidagi har bir mahsulotni tekshiramiz
#     if maxsulot in products: # Agar mahsulot products lug'atida bo'lsa
#         print(f"{maxsulot.title()} {products[maxsulot]} so'm")
# #     else: # Aks holda
# #         print(f"{maxsulot.title()} bozorda yo'q")
# for buyum in bozorlik:
#     if buyum not in products:
#         print(f"Iltimos, do'koningizga {buyum} xam olib keling!")
        
'''Lug'at elementlarini tartib bian chiqarish'''

# print("Products in the store:")
# for product in sorted(products):
#     print(product.title())

''' .values() '''
# print(phones.values())

# print("The fallowing phones are used by users:")
# for phone in phones.values():
#     print(phone)
    
phones = {
    'john': 'Samsung Galaxy S25 Ultra',
    'alex': 'Apple iPhone 16 Pro Max',
    'mateo': 'Huawei Mate X6',
    'henry': 'Google Pixel 9 Pro',
    'william': 'Samsung Galaxy S25 Edge',
    'doctor': 'Huawei Mate X6',
    'sally': 'Samsung Galaxy S25 Edge',
    'micheal': 'Apple iPhone 16 Pro Max'
    }
# print("The fallowing phones are used by users:")
# for phone in phones.values():
#     print(phone)
    
''' set() '''
print("The fallowing phones are used by users:")
for phone in set(phones.values()):
    print(phone)
    
"""
Python'da set() Funksiyasi
 set Nima?
set — bu tartibsiz, indekssiz va takrorlanmas elementlar kolleksiyasi.

 Xususiyatlari:
Takrorlanmas: Har bir element faqat bir marta mavjud.

Tartibsiz: Elementlar tartibi saqlanmaydi.

O'zgartiriluvchi: Element qo'shish yoki o'chirish mumkin.

Faqat hashable turdagi elementlar: (son, satr, tuple).
"""
# Set Yaratish Usullari:

# Tartib kafolatlanmagan
toys = {"ball", "doll", "bear", "car", "train", "ball", "train"}
print(toys) # {'bear', 'train', 'doll', 'car', 'ball'}

# 1. Bo'sh to'plam
boshlangich = set()
print(boshlangich)  # set()

# 2. Elementlar bilan
sonlar = {1, 2, 3, 4}
print(sonlar)  # {1, 2, 3, 4}

# 3. Ro'yxat yoki tuple dan
yangi_set = set([1, 2, 3, 4])
print(yangi_set)  # {1, 2, 3, 4}

# 4. Satrdan (har bir belgi alohida element)
harflar = set("hello")
print(harflar)  # {'e', 'h', 'l', 'o'}

# Set Operatsiyalari:
a = {1, 2, 3}
b = {3, 4, 5}

# Birlashma
print(a | b)  # {1, 2, 3, 4, 5}

# Kesishma
print(a & b)  # {3}

# Farq
print(a - b)  # {1, 2}

# Simmetrik farq
print(a ^ b)  # {1, 2, 4, 5}

# Set Metodlari:
s = set()

# Element qo'shish
s.add(1)
s.add(2)
s.update([2, 3, 4])  # Bir nechta qo'shish

# Element o'chirish
s.remove(3)  # Agar yo'q bo'lsa, xatolik
s.discard(10)  # Agar yo'q bo'lsa, xatolik yo'q

# Tasodifiy elementni o'chirish
elem = s.pop()

# To'plamni tozalash
s.clear()

# Foydali Amaliyotlar:

# Takrorlangan elementlarni olib tashlash
lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print(unique)  # [1, 2, 3, 4, 5]

# Matnlardagi umumiy harflarni topish
common = set("hello") & set("world")
print(common)  # {'o', 'l'}

# Diqqat qilishingiz kerak bo'lgan joyi:
# Set faqat hashable (o'zgarmas) elementlarni qabul qiladi:

valid_set = {1, 'hello', (2, 3)}  # To'g'ri
# invalid_set = {[1, 2]}  # Xato: ro'yxat o'zgaruvchan

# Set tartiblanmagan, shuning uchun chiqish tartibi har 
# doim bir xil bo'lmasligi mumkin.





