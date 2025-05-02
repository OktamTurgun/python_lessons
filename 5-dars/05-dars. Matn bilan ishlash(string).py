
"""
05-dars.Python darslari| Matn bilan ishlash

Created on Thu May 30 08:54:19 2024

@author: uktam
"""

#ism = "Uktam"

#shahar = "ҚЎқўон"
#viloyat = "Фаргона"

#matn = "Men yangi 📱 oldim"
#print(matn)
#xabar = "Hello, hov are you? 😂"
#print(xabar)

#  STRING USTIDA AMALLAR

# Matnlarni qo'shish uchun + operatoridan foydalanmiz:
#ism = "Mustafo"
#print("Mening ismim " + ism )

#ism = "O'ktam"
#familiya = "Turg'unov"
#print(ism + familiya)

#ism = "O'ktam"
#familiya = "Turg'unov"
#print(ism +' ' + familiya)# orada bo'shliq bo'ishi uchun ' ' belgidan foydalanamiz

#  f-strung

 #Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun 
 #f-string usulidan  f"{matn1} {matn2}" ham foydalansak bo'ladi:
#ism = "Ahad"
#familiya = "Qayum"
#ism_sharif = f"{ism} {familiya}"
#print(ism_sharif)

# Bu usul yordamida uzun matnlarni xam yasash mumkin:

#ism = "James"
#familiya = "Bond"
#print(f"Salom, mening ismin, {familiya}. {ism} {familiya}!")

# MAXSUS BELGILAR
# Matnga bo'shliq qo'shish uchun \t belgisidan,
# yangi qatordan boshlash uchun \n belgisidan foydalanamiz:

#print('Hello World!')
#print('Hello \tWorld!')
#print('Hello \nWorld!')

# STRING METODLAR

#ism = 'james'
#familiya = 'bond'
#ism_sharif = f"{ism} {familiya}"
#ism_sharif = ism_sharif.upper()
#print(ism_sharif.upper())
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())

#meva ="        olma         "
#print("Men " + meva.lstrip() + " yaxshi ko'raman ")
#print("Men " + meva.rstrip() + " yaxshi ko'raman ")
#rint("Men " + meva.strip() + " yaxshi ko'raman ")
#print("Men " + meva + " yaxshi ko'raman ")
#print(meva)

 # INPUT - Foydalanuvchi bilan muloqot
# Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichida berayotgan edik.
# Keling endi qiymatni o'zimiz emas, balki dastur foydalanuvchilariga kiritish imkonini beramiz. 
# Buning uchun input() funktsyasidan foydalanamiz. 

#ism = input("Ismingiz nima ?\n")
#print("Assalomu aleykum,\n " + ism.title())

# AMALIYOT

#kocha = "Bog'bon"
#mahalla = "Sog'bon"
#tuman = "Bodomzor"
#viloyat = "Toshkent"
#print(kocha + " ko'chasi, " , mahalla + " mahallasi,\n" ,
#     tuman + " tumani," , viloyat + " viloyati." )

#print("Iltimos quyidagi malumotlarni kiriting: ")
#kocha = input("Ko'changiz? \n")
#mahalla = input("Mahallangiz? \n")
#tuman = input("Tumaningiz? \n")
#viloyat = input("Viloyatingiz? \n")
#print(kocha + " ko'chasi,\n " + mahalla + " mahallasi,\n " \
#      + tuman + " tumani, \n" + viloyat + " viloyati")

#kocha = "Bog'bon"
#mahalla = "Sog'bon"
#tuman = "Bodomzor"
#viloyat = "Toshkent"
#manzil = f" {kocha} {mahalla} {tuman} {viloyat}"
#print(manzil.upper())
#print(manzil.lower())
#print(manzil.title())
#print(manzil.capitalize())



