
"""
Created on Sat Jun  1 10:34:55 2024

07-dars LIST Ro'yxat'

@author: uktam
"""

#mevalar = ['anor' , 'olma' , 'anjir' , 'shaftoli' , 'bexi' , 'uzum']
#narxlar = [1500, 2200, 3400, 5500, 12000, 17000, 20000,70000, 100000]
#sonlar = ['bir' , 'ikki' , 'uch' , 4 , 5, 6, 7]
#ismlar = []

#print('Birinchi meva:' , mevalar[0])
#print(mevalar[-2])
#print(mevalar[::-1])

# Agar list ichidagi elementlar matn ko'rinishid bo'lsa, 
# ularga string metodlarni qo'llashimiz mumkin:
    
#print(mevalar[0].upper())
#print(mevalar[3].title())

# List elementlari ustida arifmetik amallar bajarish:
    
#print(narxlar[0]+narxlar[3])
#print(narxlar[4]+1000-500)
#print(mevalar)
#mevalar[0]='banan'

# Ro'yxatga yangi elementlar qo'shish

# .append() metodi bo'sh ro'yxatni to'ldrisihda juda qulay usul. 
# Odatda dastur boshida bo'sh ro'yxat yaratilib, dastur davomida ro'yxat 
# foydalanuvchi tomonidan to'ldirib borilishi odatiy hol.

#mevalar.append('tarvuz')
#mevalar.append("o'rik")
#print(mevalar)

# Ro'yxatning istalgan joyiga yangi element qo'shish uchun 
# .insert() metodidan foydalanamiz. .insert() metodi ichida yangi elementning indeksi 
# va qiymati beriladi:
    
#mevalar.insert(0, 'qovun')
#mevalar.insert(4, 'ananas')
#mevalar.insert(0, 'avocado')

# ELEMENTNI O'CHIRISH

# Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini
# bilishimiz lozim. Inedks yordamida olib tashlash uchun del operatoridan foydalanamiz:

#cars = []
#cars.append('nexiya')
#cars.append('tico')
#cars.append('damas')
#cars.append('volga')
#print(cars)
#del cars[3]
#print(cars)
#cars.insert(0,'volvo')
#cars.insert(2, 'matiz')
#print(cars)

#cars.remove('matiz')
#print(cars)

#hayvonlar = []
#ayvonlar.append('it')
#hayvonlar.append('mushuk')
#hayvonlar.append('ot')
#hayvonlar.append('echki')

# Elementni o'chirish

# Element qiymati bo'yichi o'chirish uchun esa 
# .remove(qiymat) metodidan foydalanamiz. Buning uchun qavs ichida o'chirib
# tashlash kerak bo'lgan qiymatni yozamiz

#hayvonlar = ['it','ot','sigir','mushuk']
#hayvonlar.remove('it')
#print(hayvonlar)

# Elementni sug'urib olish

# Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni 
# ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin. 
# Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.

#bozorlik = ["go'sht","kartoshka","piyoz","yog'","sabzi","un"]

#maxsulot = bozorlik.pop(0)
#print("Men " + maxsulot + " sotib oldim")
#print("Olinmagan maxsulotlar: " , bozorlik)

# Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.

# A M A L I Y O T

#ismlar = []
#ismlar.append("Adham")
#ismlar.append("O'tkir")
#ismlar.append("Xurshid")
#ismlar.append("Oybek")
#ismlar.append("Sarvar")
#print(ismlar)

#sms = ismlar.pop(0)
#print("Salom do'stim " + sms + " qachon ko'rishamiz? ")
#sms = ismlar.pop(1)
#print(sms + " Aka qachon uyga qaytasiz? ")
#sms = ismlar.pop(2)
#print("Assalomu aleykum " + sms + " bugun oshga kelasanmi? ") 

#sonlar = [-12, 5.5, 19, 27, 30, 36.6, 77, -320]
#print(sonlar[1] + sonlar[2])
#print(sonlar[1]+ 36.6)
#sonlar[0] = -11
#sonlar[3] + 25
#sonlar[-1] = -220
#print(sonlar)

#t_shaxslar = ["Muhammad Sollalloho Alayhi Avssallam","Amir Temur","Alisher Navoiy"\
 #             ,"Imom Buhoriy","G'azzoliy","Sulton Sulaymon","Jaloliddn"]
#z_shaxslar = ["Ilon Mask","Putin","Habib","Ronaldo","Uboba","Maxmud Usmon"]

#print(f"Men {t_shaxslar.pop(0)} ni yaxshi ko'raman,\n zamonaviy shaxslardan esa\
# {z_shaxslar.pop(-1)}ni xurmat qilaman" )

#friends = []
#friends.append("Sobir")
#friends.append("Sohibjon")
#friends.append("Abduvali")
#friends.append("Elyor")
#friends.append("Adhamjon")
#print(friends)

#friends.remove("Sohibjon")

#friends.insert(0, "O'tkir")
#friends.insert(-1,"Botir")

#yangi_mexmonlar = []
#yangi_mexmonlar.append(friends.pop(-1)) 
#yangi_mexmonlar.append(friends.pop(1)) 
#yangi_mexmonlar.append(friends.pop(-2))
#print(f"Mexmonga kelgan do'stlar {friends.pop(2)} ,{friends.pop(0)}")
#print('\nKelgan mexmonlar:', yangi_mexmonlar )
