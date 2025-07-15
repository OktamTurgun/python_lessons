# -*- coding: utf-8 -*-
"""
Created on Fri May 16 22:59:06 2025

17-dars: INPUT va WHILE

@author: uktam

"""

# INPUT()

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechchida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# height = float(height)

# WHILE

# son = 1
# while son<=5:
#    print(son, end = ' ') # sonni konsolga chiqaramiz
#    son+=1 # songa 1 ni qo'shamiz (son+=1 = son=son+1 bu shaklda xam yozsa bo'ladi A+=B = A=A+B
# print("Dastur tugadi.")

''''''
# while and input
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur. ")
# savol = "Istalgan son kiriting: "
# savol += " (Dasturni to'xtatish uchun 'exit' deb yozing. )"
# qiymat = ' '
# while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)

''''''
# # Ishora (flag)
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur. ")
# savol = "Istalgan son kiriting: "
# savol += " (Dasturni to'xtatish uchun 'exit' deb yozing. )"
# ishora = True
# while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#        print(float(qiymat)**2)
# print("Dastur to'xtadi ")

''''''
# # break while
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur. ")
# savol = "Istalgan son kiriting: "
# savol += " (Dasturni to'xtatish uchun 'exit' deb yozing. )"
# while True: #Abadiy tsikl
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break # Tsiklni to'xtatish
#    else:
#        print(float(qiymat)**2)
# print("Dastur to'xtadi ")

''''''
# # break for 
# sonlar = list(range(1,11))
# for son in sonlar:
#    if son == 7:
#        break
#    print(f"{son} ning kvadrati {son**2} ga teng")

''''''
# # continue while
# sonlar = list(range(1,11))
# for son in sonlar:
#    if son == 5:
#        continue
#    print(f"{son} ning kvadrati {son**2} ga teng")

''''''
# # continue while 1
# son = 0
# while son<10:
#    son+=1
#    if son%2!= 0: # juft sonlarni chiqaradi
#        continue
#    else:
#        print(son)

''''''
# # continue while 2
# son = 0
# while son<10:
#    son+=1
#    if son%2== 0: # toq sonlarni chiqaradi
#        continue
#    else:
#        print(son)

''''''
# name = input("What is your name? ").strip().title()
# if name == '':
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")

''''''   
# name = input("What is your name? ").strip().title()
# while name == '':
#     print("You did not enter your name")
#     name = input("What is your name? ").strip().title()
# else:
#     print(f"Hello {name}")
    
''''''
# name = input("What is your name? ").strip().title()
# prompt = f"Hello, {name.title()}. How old are you? "
# age = input(prompt)
# age = int(age)
# height = input("How tall are you? ")
# height = float(height)
# print(f"{name.title()} is {age} years old and {height:.2f} meters tall.") # :.2f degani "folating point" sonni 2ta raqamgacha ko'rsatish

''' while() - toki deb tarjima qilsak bo'ladi '''
# num = 1
# while num<=5:
#     print(num, end=' ') # (end=' ') sonlarni yonma-yon chiqaradi
#     num +=1
# print("\nThe program has ended")

''' while & input '''
# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(f"{qiymat} ning kvadrati: {float(qiymat)**2} ga teng.")
#     else:
#         print("Dastur tugadi!")

''' ishora o'zgaruvchi (flag) '''
# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(f"{qiymat} ning kvadrati: {float(qiymat)**2} ga teng.")
# print("Dastur to'xtadi!")

''' Bir nechta shartlar bilan flag '''
# aralash_sonlar = [1, 3.5, -2, 4, 'hello', 7, 'python', 10.1] # [1, 3.5, -2, 4, 11, 7, -00.5, 10.1]
# faqat_sonlar = []
# ishora = True

# for element in aralash_sonlar:
#     if not isinstance(element, (int, float)):
#         ishora = False
#         print(f"{element} son emas, tsikl to'xtatildi")
#         break
#     faqat_sonlar.append(element)

# if ishora:
#     print("Barcha elementlar sonlardan iborat")      
#     print(f"Yig'ilgan sonlar: {faqat_sonlar}")  

''' bir nechta flaglar bilan ishlash '''
# parol = input("Parol kiriting: ")
# uzunlik_ok = False
# katta_harf_bor = False
# son_bor = False

# if len(parol) >= 8:
#     uzunlik_ok = True

# for harf in parol:
#     if harf.isupper():
#         katta_harf_bor = True
#     if harf.isdigit():
#         son_bor = True

# if uzunlik_ok and katta_harf_bor and son_bor:
#     print("Parol qabul qilindi!")
# else:
#     print("Parol yetarlicha mustahkam emas")

''' Yuqoridagi kodni while loop bilan '''
# while True:
#     parol = input("Parol kiriting: ")
    
#     uzunlik_ok = len(parol) >= 8
#     katta_harf_bor = False
#     son_bor = False
#     belgi_bor = False
    
#     for harf in parol:
#         if harf.isupper():
#             katta_harf_bor = True
#         elif harf.isdigit():
#             son_bor = True
#         elif not harf.isalnum():
#             belgi_bor = True
    
#     if uzunlik_ok and katta_harf_bor and son_bor and belgi_bor:
#         print("Parol qabul qilindi!")
#         break
#     else:
#         print("Parol yetarlicha mustahkam emas. Qayta urinib ko'ring!")
    
#         if not uzunlik_ok:
#             print("- Parol kamida 8 belgidan iborat bo'lishi kerak")
#         elif not katta_harf_bor:
#             print("- Kamida 1 ta katta harf bo'lishi kerak")
#         elif not son_bor:
#             print("- Kamida 1 ta raqam bo'lishi kerak")
#         elif not belgi_bor:
#             print("- Kamida 1 ta maxsus belgi (./>&#*\%) bo'lishi kerak")

''' break & while '''
# print("Kritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalga son kiriting: "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing) "

# while True: # Infinite loop - cheksiz sikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # loop to'xtatildi
#     else:
#         print(float(qiymat)**2)
# print("Dastur to'xtatildi!")

''' break & for '''
# nums = list(range(2,10))
# for num in nums:
#     if num == 5:
#         break
#     print(f"{num} ning kvadrati: {num**2} ga teng")
    
''' continue '''
# nums = list(range(2,10))
# for num in nums:
#     if num == 5:
#         continue
#     print(f"{num} ning kvadrati: {num**2} ga teng")

''' continue while '''
# num = 0             # 1) num o'zgaruvchisini 0 ga tenglaymiz
# while num<=10:      # 2) num 10 dan kichik yoki teng bo'lgunga tsiklni davom ettiramiz
#     num += 1        # 3) Har tsikl bosqichida num ni 1 ga oshiramiz
#     if num%2!=0:    # 4) Agar num toq bo'lsa (2 ga bo'lganda qoldiq 0 bo'lmasa)
#         continue    # 5) Keyingi tsikl bosqichiga o'tamiz (print qilmaymiz)
#     else:           # 6) Aks holda (juft bo'lsa)
#         print(num)  # 7) num ning qiymatini chiqaramiz
        
''' infinite loop '''
# num = 0
# while num<10:
#     # Shu qatorda num += 1 unuttik
#     if num%2!=0:
#         continue
#     else:
#         print(num)
        
''''''     
# num = 0
# while num<10:
#     # 3 - qator
#     if num%2!=0:
#         continue
#     else:
#         print(num)                                                       
#     num +=1 # Mana bu codni ushbu dasturning 3- qatorida yozish kerak
        
'''''' 
# num = 0
# while num>10: # Mana bu qatorda shartni noto'g'ri yozilgan. num<10: yozish kerak.
#     num += 1
#     if num%2!=0:
#         continue
#     else:
#         print(num)
