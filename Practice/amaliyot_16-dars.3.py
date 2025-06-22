# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 06:28:06 2024

@author: uktam
"""

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.
# Natijani konsolga chiqaring.

kinolar = {
    'adham':['suyunchi','shum bola','sen yetim emassan'],
    'sardor':['vatan','otamdan qolgan dalalar',"kelinlar qo'zg'aloni"],
    'durbek':['gladiator','kavkaz asirasi','shurik']
    }

for ism,kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari: ")
    for kino in kinolar:
        print(kino.capitalize())

#natija

       #Adhamning sevimli kinolari: 
       #suyunchi
       #shum bola
       #sen yetim emassan

       #Sardorning sevimli kinolari: 
       #vatan
       #otamdan qolgan dalalar
       #kelinlar qo'zg'aloni

       #Durbekning sevimli kinolari: 
       #gladiator
       #avkaz asirasi
       #shurik




















