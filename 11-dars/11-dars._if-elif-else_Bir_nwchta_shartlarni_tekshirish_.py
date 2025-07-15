
"""
Created on Tue Jun 11 23:34:48 2024

Dasturlash asoslari

#11-dars: if-elif-else

@author: uktam
"""

#son = 50
#if son>50:
#    print("Manfiy son")
#else:
#    print("Musbat son") 

# Python avval if shartini tekshiradi, shart bajarilmasa elif ga o'tadi, 
# birinchi elif sharti bajarilmasa keyingi elif ga o'tadi va hokazo davom etaveradi.

#  Diqqat! if-elif-else ketma-ketlikda biror shart bajarilishi bilan, 
#  Python qolgan shartlarni tekshirmaydi.   
    
#yosh = int(input("Yoshingizni nechida?"))   
    
#if yosh<=7:
#   print("Sizga kirish bepul.")     
#elif yosh<=12:
#    print("Sizga kirish 10000 ming so'm.")
#elif yosh<=18:#
#    print("Sizga kirish 15000 ming so'm")    
#else:
#    print("Sizga kirish 25000 ming so'm.")       
#    
# yosh = int(input("Yoshingizni nechida?")) 

# Kod yozishda yaxshi amaliyotlardan biri, kodlarni qisqa yozish va buyruqlarni
# qayta-qayta takrorlamaslik. Bu kelajakda kodni o'zgartirishda ham juda qo'l keladi. 

# Avval aytganimizdek,  if-elif-else zanjirida bit nechta elif lar bo'lishi mumkin. 
# Misol uchun, hayvonot bog'i qariyalar uchun chegirma e'lon qilsa, 
# kodimizni quyidagicha o'zgartirishimiz mumkin:

#yosh = int(input("Yoshingizni nechida?"))   
     
#if yosh<=7: # yosh bolalarga bepul
#    narx = 0   
#elif yosh<=12: # 7 dan 12 yoshgacha 10000 ming so'm
#    narx = 10000
#elif yosh<=18: # 12 yoshdan 18 gacha 15000 so'm
#    narx = 15000
#elif yosh>=60: # Nafaqa yoshidagilarga kirish bepul 
#    narx = 0    
#else: # Qolganlarga  kirish 20000 so'm etib belgilandi
#     narx = 20000       
        
#print(f"Sizga kirish {narx} so'm")    
    
# AND, OR OPERATORLARI

# Yuqorida aytganimizdek, if-elif-else zanjirida shartlarning biri bajarilishi bilan,
# Python qolgan shartlarni tekshirmaydi va ularni bajarmaydi. Lekin ba'zida 
# biz 2 yoki undan ko'p shartlarni tekshirishni talab qilishimiz mumkin, buing uchun
#  AND va OR operatorlaridan foydalanamiz.    
    
# OR OPERATORI    
    
# OR ingliz tilidan "yoki" deb tarjima qilinadi, va ikki va undan ko'p shartlardan 
# biri bajarilishini tekshirishda ishlatiladi. Quyidagi misolni ko'raylik, 
# foydalanuvchidan hafta kunini so'raymiz va agar kun shanba yoki yakshanba bo'lsa, 
# bugun dam olish kuni degan xabarni chiqaramiz, aks holda bugun ish kuni degan xabarni chiqaramiz:    
    
#kun = input("Bugun nima kun?>>> ")    
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print("Bugun dam olish kuni")
#else:
#    print("Bugun ish kuni")  
    
# 2-qatrodagi or operatoriga e'tibor qiling, bu operator kun.lower()=='shanba' 
# yoki kun.lower()=='yakshanba' shartlaridan biri bajarilsa TRUE qiymatini qaytaradi    
    
# AND OPERATORI    
    
# AND ingliz tilidan "va" deb tarjima qilinadi, va ikki va undan ko'p shartlarning 
# barchasi bajarilishini tekshirishda ishlatiladi. AND operatori bilan yozilgan 
# shartlarning barchasi bajarilgandagina TRUE qiymati qaytadi, agar shartlardan 
# biri bajarilmay qolsa ham FALSE qiymati qaytadi.    
    
#kun = input("Bugun qaysi kun?>>>")    
#harorat = float(input("Havo harorati qanday?>>>"))    
    
#if kun.lower()== 'yakshanba' and harorat >= 30:
#    print("Cho'migani kettik!")  
#elif kun.lower()== 'yakshanba' and harorat <30:
#    print("Uyda dam olamiz ")    
#elif kun.lower()== 'juma' and harorat>=0:
#    print("Masjidga boramiz")    
#lse:
#    print("Uyda qolamiz")    
    
# 3-qatordagi and operatori kun.lower()=='yakshanba' va harorat>=30 shartlarining
# ikkisi ham bajarilgandagina TRUE qiymatini qaytaradi, aks holda qiymat FALSE bo'ladi.    

# BIR NECHTA SHARTLARNI KETMA-KET YOZISH
    
#kun = input("Bugun qaysi kun?>>>")    
#harorat = float(input("Havo harorati qanday?>>>"))    
    
#if (kun.lower()== 'yakshanba' or kun.lower()== 'shanba') and harorat >= 30:
#    print("Cho'migani kettik!")  
#elif (kun.lower()== 'yakshanba' or kun.lower()== 'shanba') and harorat <30:
#    print("Uyda dam olamiz ")      
     
# 3-qatorga e'tibor bersangiz biz avval kun shanba yoki yakshanba ekanligini so'ngra 
# haroratni tekshirdik. Bu shart bajarilishi uchun kun shanba yoki yakshanba va harorat
# 30 dan baland bo'lishi shart.   
    
# BOOLEAN MA'LUMOTLAR TURI

# Avvalgi darsimizda biz turli ifodalarni solishtirishda TRUE yoki FALSE qiymatlari 
# qaytishini ko'rdik. Bu qiymatlar boolean (mantiqiy) qiymatlar deb ataladi, va
# dasturlashda juda keng qo'llaniladi. Pythonda o'zgaruvchilarda boolean qiymatlarni
# ham saqlash mumkin. 

# Quyidagi dasturga e'tibor bering. Deylik, restoranimizga kelgan mijoz 15000 so'mlik
# taom oldi, biz mijoz qo'shimcha choy va salat ham olgan (olmaganiga) qarab,
# ularning narhini ham  yakuniy narhga qo'shishimiz kerak. Mijozning choy yoki 
# salat olgan (olmaganini) biz TRUE va FALSE qiymatlari bilan belgiladik.    
    
#narx = 15000 # mijoz 15000 so'mga taom oldi
#choy = True # Mijoz choy xam oldi 
#salad = True # Mijoz salad olmadi

#if choy and salad: #agar mijoz choy xam salad xam sotib olgan bo'lsa
#    narx = narx + 10000 # narxga 10000 so'm qo'shamiz 
#elif choy or salad: # agar mijoz choy yoki salad sotib olgan bo'lsa
#    narx = narx + 5000 # narxga 5000 so'm qo'shamiz   
    
#print(f"jami {narx} so'm ")    

# Natija: Jami 20000 so'm

# E'tibor bering, choy va salat boolean (mantiqiy) qiymatlar bo'gani uchun, 
# 134 va 136 -qatorlarda biz choy==True yoki salat==True deb yozib o'tirishimiz shart emas.

# Yuoqirdagi misolda choy = True (choy oldi) va salat = False (salat olmadi) bo'lgani uchun
# yakuniy narh narh+5000=20000 chiqdi.
    
#narh = 15000 # Mijoz 15000 so'mga ovqat oldi   
#choy = True    
#salad = False    
#non = True    
#ompot = True    
#assorti = False    
 # Quyidagi shartlar alohida tekshiriladi va bir - biriga bog'liq emas   
#if choy:
#    print("Mijoz choy oldi")    
#    narh = narh + 5000
#if salad:
#    print("Mijoz salad oldi")    
#   narh = narh + 5000
#if non:
#    print("Mijoz non oldi")    
#    narh = narh + 3000
#if kompot:
#    print("Mijoz kompot oldi")    
#    narh = narh + 3000
#if assorti:
#    print("Mijoz assorti oldi")    
#    narh = narh +15000
#print(f"Jami {narh} so'm")    

# Boolean o'zgaruvchilarni saqlashda TRUE va FALSE qiymatlari o'rniga 1 va 
# 0 sonlarini ham ishlatish mumkin.

# SHARTLARNI KETMA-KET TEKSHIRISH

# if-elif-else zanjirining kamchiligidan biri, shartlardan biri bajarilishi bilan, 
# qolgan shartlar tekshirilmaydi. Shung uchun ba'zida shartlarni ketma ket tekshirish uchun,
# har bir shartni alohida if bilan ajratish talab qilinishi mumkin.

# Yuqoridagi misolni kengaytiraylik:
    
#narh = 15000 # Mijoz 15000 so'mga ovqat oldi   
#choy = 1    
#salad = 1    
#on = 1    
#kompot = 1    
#assorti = 0    
  # Quyidagi shartlar alohida tekshiriladi va bir - biriga bog'liq emas   
#if choy:
#    print("Mijoz choy oldi")    
#    narh = narh + 5000
#if salad:
#    print("Mijoz salad oldi")    
#    narh = narh + 5000
#if non:
#    print("Mijoz non oldi")    
#    narh = narh + 3000
#if kompot:
#    print("Mijoz kompot oldi")    
#    narh = narh + 3000
#if assorti:
#    print("Mijoz assorti oldi")    
#    narh = narh +15000
#print(f"Jami {narh} so'm")    
# Yuqoridagi dasturda har bir if alohida tekshiriladi va avvalgi yoki keyingi if ga bog'liq emas.        
    
# RO'YXAT TARKIBINI TEKSHIRISH

# in OPERATORI 

# in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini 
# tekshirishimiz mumkin.   
    
#menu = ['osh','manti','lagman','shashlik','norun','somsa','qozonkabob']    
#'mastava' in menu # menuda manti bormi    
#ovqat = input("Nima ovqat yeysiz?>>> ")   
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi")    
#else:
#    print("Afsuski bizda bunday ovqat yo'q! ")    
    
# not in OPERATORI
 
# not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz mumkin.    
    
#menu = ['osh','manti','lagman','shashlik','norun','somsa','qozonkabob']     
#"ko'za sho'rva" not in menu  # menuda ko'za sho'rva yo'qmi?  
#ovqat = input("Nima ovqat yeysiz? \n>>>")   
#if ovqat not in menu:
#    print(f"Afsuski bizda {ovqat} yo'q! Kechirasiz! ")
#    print("Xurmatli mijoz qanaqa ovqat zakaz qilasiz?")    
#else:
#    print("Buyurtmangiz qabul qilindi!")    
    
# not operatorini boshqa shartlarning oldidan ham qo'yishimiz mumkin. 
# Misol uchun: if not a==5 ifodasi if a!=5 ifodasi bilan bir hil natija qaytaradi. 

# IKKI RO'YXATNI SOLISHTIRISH

# Ikki ro'yxatning tarkibi quyidagicha tekshiriladi:   
    
#menu = ['osh','manti','lagman','shashlik','norun','somsa','qozonkabob']     
#buyurtmalar = ['osh','somsa','salat','shashlik','non']
    
#for taom in buyurtmalar:
#   if taom in menu:
#       print(f"Menuda {taom} bor.")    
#    else:
#        print(f"Kechirasiz menuda {taom} yo'q.")
   
    
# RO'YXAT BO'SH EMASLIGINI TEKSHIRISH    
    
# Yuqoridagi dasturimizda biz foydalanuvchi buyurtma berdi deb tasavvur qilyapmiz. 
# Lekin foydalanuvchidan bo'sh ro'yxat kelsachi? Demak for tsiklini bajarishdan avval
# ro'yxat bo'sh emasligiga amin bo'lishimiz kerak. Buning uchun avvalgi kodimizni quyidagicha o'zgartiramiz:    
    
#menu = ['osh','manti','lagman','shashlik','norun','somsa','qozonkabob']     
#buyurtmalar = ['osh','somsa','salat','shashlik','non']
#if buyurtmalar:    
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor.")    
#        else:
#            print(f"Kechirasiz menuda {taom} yo'q.")
#else:
#    print("Savatchangiz bo'sh!")    
        
# Demak if royxat_nomi: ifodasi agar ro'yxatda bir dona element bo'lsa ham
# TRUE qiymat qaytaradi, aks holda FALSE qiymatini qaytaradi. 

"""Added new exercises"""
# num = -2
# if num<0:
#     print("Manfiy son")
# elif num == 0:
#     print("Nol")
# else:
#     print("musbat son")

# print("Step into the wild – Welcome to the Zoo!")
# age = int(input("How old are you?>>> ").strip())
# if age<=7:
#     price = 0
# elif age <=16: # Aks holda, agar
#     price = 10000
# elif age >=60:
#     price = 0
# else: # Aks holda
#     price = 25000
# print(f"Sizga kirish: {price} so'm")

'''OR operatori'''
# day = input("What day is it today? ").strip().lower()
# if day == "saturday" or day == "sunday":
#     print("It's a rest day today.")
# else:
#     print("It's a workday today.")

'''AND operatori'''
# day = input("What day is it today? ").lower().strip()
# temp = float(input("What's the temperature outside? "))
# if day == 'saturday' and temp >= 30:
#     print("Let's go swimming!")
# elif day == 'saturday' and temp < 30:
#     print("We rest at home!")
# else:
#     print("Don’t forget, it’s time to get to work.")

''''''    
# age = int(input("How old are you? "))
# is_student = input("Are you student? ").lower().strip()

# if age >= 18 or is_student == 'yes':
#     print("Chegirma mavjud!")
# elif age >= 18 and is_student == 'yes':
#     print("Oddiy narx!")
# else:
#     print("Kirish taqiqlanadi!")

''''''    
# weather = "sunny"
# time = "afternoon"

# if weather == "sunny" and time == "afternoon": 
#     print("Parkga boramiz!") # Parkga boramiz! chiqadi Chunki 2 shart xam True
# elif weather == "rainy" and time == "evening":
#     print("Uyda kino ko'ramiz!")
# else:
#     print("Reja yo'q!")
    
''''''
# weather = "rainy"
# time = "evening"

# if weather == "sunny" or time == "evening":
#     print("Kino ko'ramiz!")  # Chiqadimi?
# elif weather == "rainy" and time == "evening":
#     print("Uyda qolamiz!")   # Chiqadimi?

''''''
# day = input('What day is it today? ').lower().strip()
# temp = float(input("What's the temperature outside? "))
# if (day == "saturday" or day == "sunday") and temp >= 30:
#     message = "Cho'milgani kettik!"
# elif (day == "saturday" or day == 'sunday') and temp < 30:
#     message = "Uyda dam olmiz!"
# else:
#     message = "Don't forget, it's time to get to work."
# print(message)

''''''
# narh = 30000
# choy = True
# salat = False

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
    
# print(f"Jami: {narh} so'm")

''''''
# narh = 25000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1

# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 5000
# if salat:
#     print('Mijoz salat oldi.')
#     narh = narh + 7000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 5000
# if kompot:
#     print("Mijoz kompot oldi")
#     narh = narh + 8000
# if assorti:
#     print("Mijoz assorti oldi")
#     narh = narh + 15000
# print(f"Jami: {narh} so'm")

'''in operatori'''
# menu = ['osh', 'qozonkabob', 'norin', 'somsa', 'kabob', "lag'mon"]
# ovqat = input("Nima ovqat yeysiz? ").lower().strip()
# if ovqat in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Afsuski bizda bu taom qolmadi")
    
'''not in operatori'''
# menu = ['osh', 'qozonkabob', 'norin', 'somsa', 'kabob', "lag'mon"]
# ovqat = input("Nima ovqat yeysiz? ").lower()
# if ovqat not in menu:
#     print("Afsuski bizda bunday ovqat qolmadi")
# else:
#     print("Buyrtma qabul qilindi")
    
''''''
menu = ['osh', 'qozonkabob', 'norin', 'somsa', 'kabob', "lag'mon", 'non']
orders = ['osh', 'somsa', 'shashlik', 'non']

if orders: # Ro'yxatda biror element bo'lsa bu ifoda True qaytaradi
    for taom in orders:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz menuda {taom} qolmadi.")
else: # Aks holda ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh")