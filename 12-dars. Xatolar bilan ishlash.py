# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:53:07 2024

@author: uktam
"""

# SyntaxError - SINTEKS XATOLAR

#print"Hello, World!"

# EOL va EOF xatolik

# EOL (End of Line - qator yakuni) xatoligi sintaks xatolikning bir turi bo'lib, 
# odatda qator oxirida qo'shtirnoq (birtirnoq) ni yopish esdan chiqqanda yuzaga keladi.
#print("Hello, World!
      
# EOF (End of function - funktsiya yakuni) xatoligi esa funktsiya oxirida qavsni yopish esdan chiqqanda yuzaga keladi.       
#print("Assalomu aleykum"

# IndetationError - SURISHDAGI XATOLAR

# print("Hello, World!")# IndentationError: unexpected indent- kutilmagan bo'sh joy

#print("O'ngacha sanaymiz")
#for n in range(10):
#print(n+1) #IndentationError: expected an indented block after 'for' statement on line 26
           # for siklida joytashlanmagan, bir xil joy tashlash kerak

# RUN TIME ERROR - DASTURNI BAJARISHDA XATOLAR

# Run time error — dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini 
# to'xtatadi. Sintaks xatolikdan farqli ravishda Python bunday xatolarni dasturni 
# bajarishdan avval aniqlay olmaydi. Run time error ning bir necha turi bor.
# Keling, ulardan ba'zilari bilan tanishamiz.

# TypeError

# Biror amalni (funktsiya, metod) noto'g'ri ma'lumot turi ustida bajarish.

#son = input("Istalgan son kiriting: ") # yoki son = int(son) deb yana bir qator qo'shishimiz kerak           
#print(f"{son} ning kvadrati {son**2} ga teng") 
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# foydalanuvchidan qabul qilgan sonimizni int ga o'tqazib olish esimizdan chiqdi

#son = int(input("Istalgan son kiriting: ")) # bu xolatda yozsa xam bo'ladi            
#print(f"{son} ning kvadrati {son**2} ga teng") 

# NameError - ma'lum bir o'zgaruvchi yoki funksiyani nomini xato yozib qo'yganda
# yuz beradigan xatolar turidan biri

#1
#prit("Hello, World!") # bu yerda print() funksiyasi xato yozildi

#2
#
#mevalar = ['olma','anor','shaftoli','anjir']
#for meva in mvalar: #NameError: name 'mvalar' is not defined
#    print(meva)

# ValueError
# Noto'g'ri qiymat berib qo'yganimizda valueError kelib chiqadi

#son = int(input("Istalgan son kiriting: "))
#if son>=0:
#    print("Musbat son")
#else:
#    print("Manfiy son")
    
# Natija:Istalgan son kiriting: 23.5
# ValueError: invalid literal for int() with base 10: '23.5'    
# istalgan (butun) son kiriting deb o'zgartirishimiz kerak yoki quyidagi xolatda
#son = float(input("Istalgan son kiriting: "))# int ni float ga ya'ni butun sonni o'nlik songa
#if son>=0:                                   # o'zgartirishimiz kerak
#    print("Musbat son")
#else:
#    print("Manfiy son")    
    
# IndexError
# Ya'ni ro'yxat elementlariga murojat qilishda indeksni noto'g'ri kiritish.    

#mevalar = ['anor','uzum','bexi','anjir','olma']    
#print(mevalar[5]) # IndexError: list index out of range. Noto'gri index berildi  
# Dasturlashda index 0 dan boshlanadi    
    
# ZeroDivisionError - 0 ga bo'lish xalolari    

#x, y = 50, 50    
#z = 250/(x-y) # ZeroDivisionError: division by zero 0 ga bo'ldingiz , 0 ga bo'lib bo'lmaydi  

#x, y = 60, 50 # shu xolatda to'g'ri bo'ladi  
#z = 250/(x-y)    
   
# MANTIQIY XATOLAR
# Mantiqiy xatolar - dasturchi tomonidan yo'l qo'yilgan va kutilgan natijani berishda 
# to'sqinlik qiluvchi xatolar. Bunday xatolar eng ko'p uchraydigan va aniqlash eng qiyin
# bo'lgan xatolar hisoblanadi. Aksar holatlarda Python mantiqiy xatolarni aniqlamaydi
# va dastur bajarilaveradi (lekin kutilgan natija chiqmaydi).
 
# Mantiqiy xatolar turli ko'rinishda bo'lishi mumkin, masalan sonlar bilan ishlashda:

#radius = 5
#pi = 4.14 # pi = 3.14159 bo'adi
#aylana_yuzi = pi*radius**2
#print(aylana_yuzi)

#son = float(input("Istalgan son kiriting: "))
#ildiz = son**1/2    
#print(f"{son} ning ildizi {ildiz} ga teng")    
#  2-qatorda ildizni hisoblashda foydalanuvchi kiritgan son avval 1-darajaga oshirildi 
# va undan keyin 2 ga bo'lindi. Kodni to'g'rilaymiz:
    
#son = float(input("Istalgan son kiriting: "))
#ildiz = son**(1/2) # yoki ildiz = son**0.5 deb yozamiz   
#print(f"{son} ning ildizi {ildiz} ga teng") 

# Noo'rin bo'sh joy qoldirish (yoki qoldirmaslik) ham mantiqiy xatoga olib kelishi mumkin:    

mevalar = ['anjir','olma','shaftoli','gilos','nok','xurmo']
for meva in mevalar:
    print(meva)    
    print("Dastur tugadi")# bu yerda dastur tugadi niqator boshidan yozishimiz kerak edi
                          # surib qo'yigan qatorni qator boshiga surib qo'yamiz,
    
# AMALIYOT        
# 1.
#son = float(input("Juft son kiriting: "))
#if son%2!=0:
#    print("Bu son juft emas.")
#lse:
#    print("Rahmat!")


# 2.
#yosh = float(input("Yoshingiz nechida?"))

#if yosh<=4 or yosh>=60:
#     narh = 0
#elif yosh < 18:
#    narh = 10000
#else:
#   narh = 20000
#print(f"Chipta {narh} so'm")

# 3.
#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")
    
# 4.    
#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#avat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#if savat:
#    for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            print(f"Do'konimizda {mahsulot} bor")
#        else:
#           print(f"Do'konimizda {mahsulot} yo'q")
#lse: 
#    print("Savatingiz bo'sh")        
    
# 5.    
    
#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:"))

#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)

#if mavjud_emas:
#  print("Do'konimizda quyidagi mahsulotlar yo'q:")
#  for mahsulot in mavjud_emas:
#      print(mahsulot)
#else:
#  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# 6.
#users = ['alisher1983','aziza','yasina' 'umar']

#login = input("Yangi login tanlang:")

#if login in users:
#    print('Login band, yangi login tanalng!')
#else:
#    print("Xush kelibsiz!")

# 7.

#son = int(input("Istalgan butun son kiriting: "))

#for n in range(2,11):
#    if not (son%n):
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")