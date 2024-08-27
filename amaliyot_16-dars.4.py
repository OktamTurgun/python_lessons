# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 06:46:20 2024

@author: uktam
"""

# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni 
# lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    'uzbekistan':{'poytaxt':"toshkent",
                  'joylashuvi':'amudaryo va sirdaryo orasida joylashgan',
                  'maydoni':' 448.9 ming kv km',
                  'aholisi':' 36 799 800 kishi'},
    'turkiya':{'poytaxt':' istanbul',
               'joylashuvi':'sharqiy yarim sharda joylashgan',
               'maydoni':' 783 562km/2',
               'aholisi':'86.099.039'},
    'indaneziya':{'poytaxt':' jakarta',
                  'joylashuvi':'janubiy sharqiy osiyodagi davlat',
                  'maydoni':' 1904.6 ming kv km',
                  'aholisi':' 265 ml kishi'},
    'ispaniya':{'poytaxt': 'madrid',
                'joylashuvi':"yevropaning janubi-g'arbida joylashgan",
                'maydoni':' 504.75 min kv km',
                'aholisi':' 47.27 ml kishi'}
    }

for davlat,info in davlatlar.items():
    if davlat.lower()=='Uzbekistan':
       davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
        print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
              f"\nJoylashuvi: {info['joylashuvi'].capitalize()}"
              f"\nHududi: {info['maydoni']}"
              f"\nAholisi:  {info['aholisi']}")     
    
    



























