# -*- coding: utf-8 -*-
"""
Created on Mon May 19 17:11:07 2025

@author: uktam
"""
# def salom_ber():
#     ''' salom beruvchi funksiya '''
#     print("Assalomu aleykum")

# salom_ber()

''''''
# Funksiyaga qiymat uzatish
def salom_ber(ism):
    """Foydalanuvchi ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalomu aleykum {ism.title()}!")
    
salom_ber("alex")

''''''
# Standart parametr qiymati
def salom_ber(ism='Mehmon'):
    """Foydalanuvchi ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalomu aleykum {ism.title()}!")
    
salom_ber() # Assalomu aleykum Mehmon!
salom_ber("alex") # Assalomu aleykum Alex!

''''''
# Qiymat qaytaruvchi funksiyalar (return)
def kvadrat_hisobla(son):
    """Sonni kvadratini xisoblovchi funksiya"""
    return son ** 2

result = kvadrat_hisobla(5)
print(result) # 25


''''''
# Funcsiyaga bir necha argument uzatish
def fullname(firstname, lastname):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"User name: {firstname.title()}\n"
          f"User last name: {lastname.title()}")

fullname('john', 'doe')

''''''
# Maxsulot narhini hisoblash
def narx_hisob(narx, *chegirmalar):
    """Bir nechta chegirmalardan keyingi narxni hisoblaydi"""
    for chegirma in chegirmalar:
        narx *= (100 - chegirma) / 100 # narx = narx * ((100 - chegirma) / 100)
    print(f"Yakuniy narx: {narx:.2f} so'm") # Natijani chiqarish 2 xonali aniqlikda

narx_hisob(100000, 10, 5, 2)

''''''
# Tanishtiruv funksiyasi
def tanishtir(name, age):
    """Foydalanuvchi ismi va yoshini qabul qilib, tanishtiruvchi funksiya"""
    print(f"Salom, mening ismim {name.title()}, va men {age}-yoshdaman.")
    
tanishtir('ali', 23)

''''''
# Xush kelibsiz funksiyasi
def xush_kelibsiz(ism, joy):
    """Mexmonni xush kutib olish funksiyasi"""
    print(f"Assalomu aleykum {ism.title()} {joy.title()}ga xush kelibsiz!")
    
xush_kelibsiz('halima', 'samarqand')

''''''
# Tug'ilgan yilini xisoblovchi funksiya
def tugilgan_yil(ism, familiya, yosh):
    """Foydalanuvchi tugilgan yilini xisoblaydi"""
    from datetime import datetime
    joriy_yil = datetime.now().year
    print(f"{ism.title()} {familiya.title()} siz {joriy_yil - yosh}-yilda tug'ilgansiz!")
    
tugilgan_yil("botir", "tolibov", 25)

''''''
# Yosh xisoblovchi funksiya
def yosh_hisobla(ism, t_yil, joriy_yil=2025):
    """Foydalanuvchi yoshini hisoblaydigan funksiya"""
    print(f"{ism.title()} {joriy_yil-t_yil} yoshda!")
    
yosh_hisobla("maxkam", 1995)
# yosh_hisobla(1995, "maxkam") # Xato 

# Kalit so'zli argumentlar
yosh_hisobla(t_yil=1995, ism='maxkam') # Shunday qilib yozish to'g'ri boladi
yosh_hisobla(ism='maxkam', t_yil=1995) # Natija bir xil bo'ladi va to'g'ri ishlaydi 

# Bu yerda parametr "joriy_yil"ni kiritmasak xam xatosiz ishlaydi,
# chunki parametr uchun default qiymat berib ketilgan
yosh_hisobla('olim', 1999) # joriy_yil=2025

''''''
# Telefon raqam funksiyasi
def telefon_raqam(kodi, raqam):
    """Telefon raqamni formatlab beradi"""
    print(f"Telefon raqamingiz: +{kodi} {raqam[:2]} {raqam[2:5]} {raqam[5:7]} {raqam[7:]}")

telefon_raqam("998", "901234567")

''''''
# Manzil funksiyasi
def manzil(shahar, tuman, kocha, uy):
    """Foydalanuvchi manzilini chiqaradi"""
    print(f"Manzil: {shahar.title()} shahar, {tuman.title()} tumani, {kocha.capitalize()} ko'chasi, {uy}-uy.")

manzil("andijon", "asaka", "bog'i shamol", 45)
