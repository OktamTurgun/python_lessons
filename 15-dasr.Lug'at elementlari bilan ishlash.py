# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:47:32 2024

@author: uktam
"""

# # .items() metodi. elementlar deb tarjima qilinadi

# Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin. 


#talaba_0 = {
#    'familiya':'shamshiyev',
#   'yosh':'22',
#    'fakultet':'tarix',
#    'kurs':'4',
#    'manzil':'xorazm'
#    }
#print(talaba_0.items())

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
#for key, value in phones.items():
#    print(f"{key.title()} ning telefoni {value.upper()}\n")
          ###
## .keys() 

products = {
    'anor':14000,
    'uzum':20000,
    'non':30000,
    'tarvuz':12000,
    'shaftoli':25000,
    }
#print(products.keys())
           ###
#print('Do\'kondagi maxsulotlar:')# 1- variant
#or product in products.keys():
#    print(product.title())
           ###
#print('Do\'kondagi maxsulotlar:')# 2- variant
#for product in products:
#    print(product.title())


#bozorlik = ['anor','uzum','qovoq','tarvuz','non','baliq']
#for product in products:
#    if product in bozorlik:
#        print(f"{product} {products[product]} so'm.")

#for buyum in bozorlik:
#    if buyum not in products:
#        print(f"Iltimos do'koningizga {buyum} xam olib keling")

## LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH

#print("Do'konimizdagi maxsulotlar: ")
#for maxsulot in sorted(products):
#    print(maxsulot.title())
    
# # .velues(). qiymatlar deb tarjima qilinadi    
# Agar lug'atdagi qiymatlarni chiqarish talab qilinsa .values() metodidan foydalanishimiz mumkin.
    
#print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")    
#for tel in sorted(phones.values()):    
#    print(tel) 
    
## Yuqoridagi usul bilan qiymatlarni chiqrganimizda, lug'atdagi barcha qiymatlar 
## chiqib keladi. Agar, biror qiymat ko'p marta qaytarilsa, konsolga ham ko'p
## marta chiqib keladi.

#  Quyidagi misloni ko'raylik:

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
#print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
#for phone in telefonlar.values():
#    print(phone)

# # Yuoqirdagi kodning natijasiga e'tibor bersanigz, bir nechta foydalanuvchilar Samsung galaxy s4, huawei E110 va Iphone 14 max pro  
# # telefonidan foydalanishar ekan, va bu modellar qayta-qayta konsolga chiqdi. 

## Buning oldini olish uchun set() funktsiyasidan foydalanishimiz mumkin.

#print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
#for phone in set(telefonlar.values()):
#    print(phone)

## Pythonda set yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta 
# elementlarni saqlashga mo'ljallangan. Lug'at va ro'yxatdan farqli ravishda, 
# set ichidagi elementlar biror tartibda saqlanmaydi, va ularga indeks orqali murojat qilib
# bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmaydi.

#toys = {"ball","bear","car","teddy","lamp","ball","car"}
#print(toys)

### AMALIYOT 

# 1. Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
#    Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida 
#    chiroyli qilib konsolga chiqaring. 

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
#print("Python izohli lug'ati: ")
#for key, value in sorted(python.items()):
#    print(f"{key.title()} - {value}\n")

# 2. Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
#    keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

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

# 3. Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini
#    konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
#    "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

davlat = input('\nQaysi davlatning poytaxtini bilishni istaysiz? ').lower()
poytaxt = countries.get(davlat)
if poytaxt == None:
    print("Kechirasiz bizda bu xaqida ma'lumot yo'q!")
else:
   print(f"{davlat.upper()}ning - poytaxti {poytaxt.title()}")

###

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = countries.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

# 4. Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni 
# menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda 
# "bizda bunday taom yo'q" degan xabarni chiqaring.

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







