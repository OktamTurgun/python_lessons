# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:59:34 2024

@author: Uktam Turgunov
"""

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni
# lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi
# ma'lumotni konsolga chiqaring.

muhammad_ali = {
    'ism':'cassius marcellus clay',
    't_yil':1942,
    'manzil':'amerika',
    'v_yil':2016,
    'xaqida':'boks boyicha jahon chempioni'
    }

buxoriy = {
    'ism':'Abu Abdulloh Muhammad al Buxoriy',
    't_yil':810,
    'manzil':'buxoro',
    'v_yil':2016,
    'xaqida':'Hadis ilmining sultoni'
    }

qodiriy = {
    'ism':'abdulla',
    't_yil':1894,
    'manzil':'toshkent',
    'v_yil':1938,
    'xaqida':"o'zbek adabiyotining ulkan namonyondasi"
    }    

navoiy = {
    'ism':'nizomiddin mir alisher navoiy',
    't_yil':1441,
    'manzil':'hirot temuriylar imperiyasi',
    'v_yil':1501,
    'xaqida':"so'z mulkining sultoni"
    }

persons = [muhammad_ali,buxoriy,qodiriy,navoiy]
for person in persons:
    ism = person['ism']
    t_yil = person['t_yil']
    manzil = person['manzil']
    v_yil = person['v_yil']
    xaqida = person['xaqida'] 
    print(f"\n{ism.title()} {t_yil}-da {manzil.title()}da tug'ilgan, "
          f"{xaqida.title()} {v_yil}-da olamdan o'tgan, "
          f"{t_yil}-{v_yil}larda yashab o'tgan tarixiy shaxs.")






























