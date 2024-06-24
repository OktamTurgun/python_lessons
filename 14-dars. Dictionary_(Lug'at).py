# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:34:02 2024

@author: uktam
"""
# Sodda lug'at yaratamiz car_0 nomli

car_0 = {'model':'ferrari','color':'red'}
#print(car_0['model'])
#print(car_0['color'])

# LUG'AT BILAN ISHLASH
# Demak, Pytonda lug'at kalit so'z-qiymat juftliklarining yi'ginidisi ekan. 
# Lug'atdagi biror qiymatni ko'rish uchun unga kalit so'z orqali murojat qilamiz:

eng_uz = {'apple':'olma','peach':'shaftoli','grapes':'uzum','watermwlon':'tarvuz','pear':'nok'}
#print(eng_uz['grapes'])
#print(eng_uz['apple'])

mevalar = {'olma':'15000','uzum':'35000','tarvuz':'25000','nok':'17000','banan':'21700','qovun':'9000'}
#print(f"Olma narhi {mevalar['olma']} so'm")
#print(f"Banan narhi {mevalar['banan']} so'm")

# Lug'atdagi qiymatlar son (int, float), matn (string), ro'yxat (list, tuple) va 
# hatto boshqa lug'at ham bo'lishi mumkin.

talaba_0 = {'ism':'bobur','t_yil':'2001','yosh':'23'}
#print(f"{talaba_0['ism'].title()},\
#{talaba_0['t_yil']}- yilda tug'ilgan,\
#talaba_0['yosh']} yoshda ")

# YANGI JUFTLIK QO'SHISH
# Lug'aga yangi kalit so'z va qiymatlar qo'shishimiz ham mumkin. Keling, yuqoridagi talaba_0
# nomli lu'gatga yana 2 ta yangi, kurs va fakultet nomli, kalit so'zlar va qiymatlar qo'shamiz:

talaba_0['kurs'] = 3
talaba_0['fakultet'] = 'informatika'

## BO'SH LUG'AT

# Ba'zida dastur boshida bo'sh lug'at yaratib, dastur davomida lug'atga yangi ma'lumotlar 
# kiritib borish talab qilinishi mumkin. Bunday holatda bo'sh lug'at quyidagicha yaratiladi:
    
talaba_1 = {}
    
talaba_1['ism'] = 'Ilhom'    
talaba_1['t_yil'] = 1997   
talaba_1['yosh'] = 27    
talaba_1['kurs'] = 4
talaba_1['fakultet'] = 'xalqaro biznes'    
talaba_1['manzil'] = 'Toshkent shahar ,yashnabod tumani'
   
#print(f"Ismi {talaba_1['ism'].title()},\
#{talaba_1['t_yil']}-yilda tug'ilgan,\
#{talaba_1['yosh'] } yoshda,\
#{talaba_1['kurs']}- kursda o'qimoqda,\
#{talaba_1['fakultet']} fakultet talabasi,\
#{talaba_1['manzil']}da yashaydi")       
        
## QIYMATNI O'ZGARTIRISH
# Biror kalit so'zga tegishli qiymatni o'zgartirish esa quyidgachia amalga oshiriladi:   
    
talaba_1['kurs'] = 3
talaba_1['ism'] = 'Oybek'    
talaba_1['t_yil'] = 2002   
    
# KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH

# Lu'gatdagi biror juftlik kerak emas bo'lsa uni del operatori yordamida lug'atdan olib
# tashlashimiz mumkin:
    
#talaba_0 = {'ism':'bobur','t_yil':'2001','yosh':'23'}   
#print(talaba_0)
#el talaba_0['yosh']    
#print(talaba_0)    
    
### Natija: {'ism': 'bobur', 't_yil': '2001', 'yosh': '23'}
###         {'ism': 'bobur', 't_yil': '2001'}    
    
# LUG'ATNI QATORLARGA BO'LIB YOZISH

# Uzung lug'atlarni bir necha qatorga bo'lib yozishimiz ham mumkin.
# Keling quyidagi misolni ko'ramiz, siz do'stlaringizdan ular qanday telefon ishlatishini
# so'radingiz va javoblarni bitta lug'atga joylamoqchisiz:    
    
telefonlar = {
    'Akmal':'Iphone 14 pro max',
    'Xurshid':'Samsung 12',
    'Sanjarbek':'Xiomi Redmi 11',
    'Sardor':'Huavei',
    'Hosilboy':'Samsung galaxy',
    "O'tkirbek":'Iphone 15 pro'
    }    

## get() METODI

# Biz shu vaqtgacha lug'atdagi qiymatlarni ko'rish uchun to'g'ridan-to'g'ri kalit so'z
# orqali murojat qilayotgan edik. Bu usulning kamchiligi shundaki, agar lug'atda siz 
# so'ragan kalit topilmasa, dastur KeyError xatoligi bilan to'xtab qoladi. 

#phone = telefonlar['Hasan']
#print(f"Hasanning telefoni {'Hasan'}")   


# Natija: KeyError: 'hasan'

# Lug'atda 'hasan' kalit so'zi bo'lmagani uchun, yuqoridagi kod KeyError degan xatoni 
# qaytardi. KeyError ham Run time error qatoriga kiradi.

# Hozir get() metodi yordamida lug'atga murojat qilish va mavjud bolmagan 
# kalitning o'rniga biror xabar qaytarishni ko'raylik.

#phone = telefonlar.get('hasan','Bunday ism mavjud emas')

# Yuqorida, lug'at nomidan so'ng .get() metodini yozdik, va argumentlar sifatida kalit so'z
# ('hasan') va kalit mavjud bo'lmaganda chiqadigan xabarni yozdik ('Bunday ism mavjud emas').

#print(phone) # Natija: Bunday ism mavjud emas

#meva = eng_uz.get('strawberry', 'Bunday meva mavjud emas')
#print(meva)

#phone = telefonlar.get('Hasan')
#print(phone)

# AMALIYOT

# 1. otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida
# kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :

#otam = {'ism':"mo'minjon",'t_yil':'1956','manzil':'namangan viloyat, chortoq shahar'}
#onam = {'ism':"etiborxon",'t_yil':'1957','manzil':'namangan viloyat, chortoq shahar'}

#parent1 = otam.get('kasbi', 'Xozir nafaqda')
#parent2 = onam.get('kasbi', 'Xozir nafaqada')

#print(f"Otam {parent1},onam xam {parent2} dam olishmoqda")

#print(f"Otamning ismi: {otam['ism'].upper()}, \
#tug'ilgan yili: {otam['t_yil']}- yilda tug'ilgan, \
#Yashash joyi: {otam['manzil'].title()}.")

#print(f"Otamning ismi {otam['ism'].title()}, Onamning ismi {onam['ism'].title()}")

# 2. Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta 
# ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: 

taom = {
    "otam":"sho'rva",
    "onam":"manti",
    "akam":"qozon kabob",
    "ukam":"lag'mon",
    "singlim":"shashlik"
    }
#print(f"Otamning sevimli taomi {taom['otam']}\n,\
#      Onamning sevimli taomi {taom['onam']}\n,\
#         Akammning sevimli taomi esa {taom['akam']}\n,\
#             Singlimni sevimli taomi bu xar xil {taom['singlim']}lar")

# 3. Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani)
# kiriting (masalan integer, float, string, if, else va hokazo) 
# va har birining qisqacha tarjimasini yozing.

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

#alit = input("Kalit so'z kiriting: ").lower()
#print(python.get(kalit,'Bunday atama mavjud emas'))

kalit = input("Kalit so'z kiriting: ").lower()
tarjima = python.get(kalit)
print(python.get(kalit))
if tarjima==None:
    print(f"Bunday so'z {tarjima} mavjud emas!")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")    






    
    
    
    