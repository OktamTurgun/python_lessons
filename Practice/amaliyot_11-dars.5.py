# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:45:35 2024

@author: uktam
"""

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni
# foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

users = ["Uktam","Zarif","Bobur","Akmaljon","Oybek"]
login = input("Yangi login tanlang: ")

if login in users:
    print("Bu login band yangi login tanlang!")
else:
    print(f"Xush kelibsiz! {login.title()}!")