# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 08:38:48 2024

@author: uktam
"""

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
# foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda
# mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

davlatlar = {
    'uzbekistan':{'poytaxt':"toshkent",
                  'joylashuvi':'amudaryo va sirdaryo orasida joylashgan',
                  'maydoni':' 448.9',
                  'aholisi':' 36 799 800'},
             'turkiya':{'poytaxt':' istanbul',
               'joylashuvi':'sharqiy yarim sharda joylashgan',
               'maydoni':' 783 562',
               'aholisi':'86.099.039'},
             'indaneziya':{'poytaxt':' jakarta',
                  'joylashuvi':'janubiy sharqiy osiyodagi davlat',
                  'maydoni':' 1904.6',
                  'aholisi':' 265.000.000'},
             'ispaniya':{'poytaxt': 'madrid',
                'joylashuvi':"yevropaning janubi-g'arbida joylashgan",
                'maydoni':' 504.75',
                'aholisi':' 47.270.000'}
             }

davlat = input("Davlat nomini kiriting: \n").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()} "
      f"\nHududi: {info['joylashuvi'].title()} "
      f"\nMaydoni: {info['maydoni']}min kv. km "
      f"\nAholisi: {info['aholisi']} kishi ")
else:
    print("Bizda bu davlat xaqida ma'lumot mavjud emas. ")




















