"""Xatolar yuz berganda, ularni ushlash va dastur to'xtashining oldini olishni ko'rdik. Ya'ni, try-except ketma-ketligi xatolarning oldini olishga yordam bera olmaydi. Xatolarning oldini olish uchun if-else va while tsikllaridan foydalanganimiz afzal.
"""
# try-except xatolarni ushlab qoladi, ya'ni xato bo'lsa ham dastur to'xtab qolmaydi.

# Lekin u xatoning oldini olmaydi — xato baribir bo'ladi,
# faqat uni ushlab, qandaydir chora ko‘rishga imkon beradi.

# Agar siz xatoning umuman yuz bermasligini xohlasangiz, unda if-else yoki while
# yordamida xatoga olib keladigan vaziyatlarni tekshirishingiz kerak.

# Exercise: 1 Faqat Try-Except bilan
try:
    age = int(input("Yoshingizni kiriting: "))
except ValueError:
    print("Xato: Yosh raqam bolishi kerak!")

'''
Tushuntirish:
Agar foydalanuvchi "salom" deb yozsa → xato bo'ladi (ValueError)
Lekin try-except bu xatoni ushlab qoladi va dasturni to'xtatmaydi.
Ammo xato baribir yuz berdi.
'''

# Exercise: 2 If-Else bilan. Avval tekshir, keyin ishlat (xatoni oldini olish)
age = input("Yoshinghizni kiriting: ")

if age.isdigit():
    age = int(age)
    print(f"Siz {age} yoshdasiz!")
else:
    print("Faqat butun son kiriting")

'''
Tushuntirish:
Bu yerda biz oldindan tekshirdik, ya'ni foydalanuvchi son kiritdimi?
Shuning uchun xato umuman bo'lmadi.
Bu xatoni oldini olish degani.
'''

# Exercise: 3 while bilan foydalanuvchidan to‘g‘ri ma’lumot kiritguncha so'rash
while True:
    age = input("Yoshingizni kiriting: ")
    if age.isdigit():
        age = int(age)
        print(f"Siz {age} yoshdasiz.")
        break
    else:
        print("Xato! Faqat butun son kiriting.")

print(f"Siz {2025 - age}-yilda tug'ilgansiz.")

'''
Tushuntirish:
Bu holatda foydalanuvchi xato kiritsa ham, to'g'ri kiritmaguncha so'rayveradi.
Ya'ni xato yuz bermaydi, chunki biz xato holatga yo'l qo'ymayapmiz.
'''
