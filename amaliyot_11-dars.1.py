# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:29:17 2024

@author: uktam
"""

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul

# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm

# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

yosh = int(input("Yoshingiz nechida?\n>>>"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh<18:
    narh = 10000
else:
    narh = 20000

print(f"Sizga kirish {narh} so'm")










