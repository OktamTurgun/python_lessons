# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:45:25 2024

@author: uktam
"""

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning 
# teng yoki katta/kichikligi haqida xabarni chiqaring

x = float(input("Birinchi sonni kiriting:\n>>> "))
y = float(input("Ikkinchi sonni kiriting:\n>>>"))
if x==y:
    print(f"{x}={y}")
elif x>y:
    print(f"{x}>{y}")
else:
    print(f"{x}<{y}")    

