# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:15:56 2024

@author: uktam
"""

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni
# 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 

number = int(input("Istalgan butun son kiriting:\n>>>"))

for n in range(2,11):
    if not (number%n):
        print(f"{number} soni {n} ga qoldiqsiz bo'linadi")

#son = int(input("Istalgan butun son kiriting: "))

#for n in range(2,11):
#    if not (son%n):
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")