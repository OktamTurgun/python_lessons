"""
Created on Mon Jun 23 19:23:14 2025

35-dars. Xatolar bilan ishlash. Exception handling 

@author: uktam
"""
# Xatolar bilan ishlash (Exception handling) - Pythonda xatolarni qanday aniqlash va ularga qanday javob berish haqida
# Xatolarni aniqlash va ularga javob berish uchun try-except bloklaridan foydalanamiz
# try - bu yerda xatoga olib kelishi mumkin bo'lgan kod yoziladi
# except - bu yerda xatoga javob berish kodi yoziladi
# finally - bu yerda har doim bajarilishi kerak bo'lgan kod yoziladi (xato bo'lsa ham, bo'lmasa ham)
# else - bu yerda xato bo'lmasa bajarilishi kerak bo'lgan kod yoziladi

# Exercise: 1
age = input("Yoshingizni kiriting: ")
try:
    # Bu yerda xato bo'lishi mumkin, agar foydalanuvchi raqam kiritmasa
    age = int(age)
except ValueError:
    print("Xato! Iltimos faqat butun son kiriting!")
else:
    print(f"Siz {2025-age}-yilda tug'igansiz.")

# Ushbu kodda foydalanuvchi kiritgan yoshni tekshirish va xatolarni boshqarish ko'rsatilgan
# try:
#     age = input("Yoshingizni kiriting: ")
#     age = int(age)  # Avval int-ga o'tkazish

#     # Qo'shimcha tekshirishlar
#     if age < 0:
#         raise ValueError("Yosh manfiy bo'lishi mumkin emas!")
#     if age > 120:
#         raise ValueError("Yosh 120 dan katta bo'lishi mumkin emas!")

#     print(f"Siz {2025 - age}-yilda tug'ilgansiz.")

# except ValueError as e:
#     if "invalid literal for int()" in str(e):
#         print("Xato: Iltimos, faqat butun son kiriting!")
#     else:
#         print(f"Xato: {e}")
#     print(f"Xatolik tafsilotlari: {type(e).__name__}: {e}")

# else:
#     print("Yoshingiz muvaffaqiyatli qabul qilindi!")

# finally:
#     print("Dastur tugadi. Yana urinib ko'ring!")
