# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:41:10 2024

@author: uktam
"""

# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.



buxoriy = {
    'ism':'Abu Abdulloh Muhammad al Buxoriy',
    't_yil':810,
    'manzil':'buxoro',
    'v_yil':2016,
    'xaqida':'Hadis ilmining sultoni',
    'asarlari':["Al-jome' as-sahih", "Al-adab Al-mufrad", "At-tarix Al-kabir",
                "At-tarix as-sag'ir","Kitob al-favoid"]
    }

qodiriy = {
    'ism':'abdulla',
    't_yil':1894,
    'manzil':'toshkent',
    'v_yil':1938,
    'xaqida':"o'zbek adabiyotining ulkan namonyondasi",
    'asarlari':["o'tkan kunlar", "Mexrobdan chayon", "Jinlar bazmi",
                "Toshp'lat tajang nima deydi",""]
    }    

navoiy = {
    'ism':'nizomiddin mir alisher navoiy',
    't_yil':1441,
    'manzil':'hirot temuriylar imperiyasi',
    'v_yil':1501,
    'xaqida':"so'z mulkining sultoni",
    'asarlari':["Mahbub ul-qulub", "Lison ut-tayr", "Xamsa","Xazoin ul-maoniy",
                "Majolis un-Nafois"]
    }

termiziy = {
    'ism':'abu iso ',
    't_yil':824,
    'manzil':'termiz',
    'v_yil':892,
    'xaqida':"muhaddis, faqih va hofiz",
    'asarlari':["At-tarix", "Kitob az-zuhd", "Kitob ul-asmo", "Al-jomi'"]
    }
shaxshlar = [buxoriy,navoiy,termiziy,qodiriy]
for shaxs in shaxshlar:
    ism = shaxs['ism']
    asarlari = shaxs['asarlari']
    print(f"\n{ism.capitalize()}ning mashxur asarlari: ")
    for asar in asarlari:
        print(asar.title())











































