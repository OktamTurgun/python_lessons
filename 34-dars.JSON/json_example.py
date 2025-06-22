"""
Created on Sun Jun 22 05:32:46 2025

34-dars. JSON

@author: uktam
"""
import json

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

ism = "Anvar"
ism_json = json.dumps(ism)
familiya_json = json.dumps("Narzullayev")

sonlar = (12, 45, 7, 53, 23)
sonlar_json = json.dumps(sonlar)

bemor = {
  "ism":"Alijon Valiyev",
  "yosh":30,
  "oila":True,
  "farzandlar":("Ahmad","Noila"),
  "allergia":None,
  "dorilar":[
    {"nomi":"Analgin", "miqdori": 0.5},
    {"nomi":"Panadol", "miqdori": 1.2}
  ]
}

# JSON ma'lumotlarini konsolga chiqarish
bemor_json = json.dumps(bemor)
print(bemor_json)

# JSON ma'lumotlarini chiroyli formatda chiqarish
bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)

# JSON ma'lumotlarini faylga yozish va o'qish
with open('bemor.json', 'w') as file:
    json.dump(bemor,file)
 
# JSON ma'lumotlarini fayldan o'qish   
with open('bemor.json', 'r') as file:
    data = file.read().strip().replace('\n', '')

# print(data)

# JSON ma'lumotlarini faylga yozish
with open('sonlar.json', 'w') as file:
    json.dump(sonlar,file)

# JSON ma'lumotlarini fayldan o'qish
with open('sonlar.json', 'r') as file:
    dat = file.read().strip().replace('\n', '')
    
# print(dat)

# JSON ma'lumotlarini Python obyektiga aylantirish
bemor_json = '''
{
    "ism": "Alijon Valiyev",
    "yosh": 30,
    "oila": true,
    "farzandlar": ["Ahmad", "Noila"],
    "allergia": null,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2}
    ]
}
'''
bemor2 = json.loads(bemor_json)