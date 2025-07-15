"""
Created on Sun Jun 22 15:02:46 2025

34-dars. JSON

@author: uktam
"""
'''
JSON (JavaScript Object Notation) — bu ma'lumotlarni matn (text) 
ko‘rinishida saqlovchi va oson o‘qiladigan format. 
Ko‘p dasturlarda ma’lumotlarni almashish uchun ishlatiladi.
'''
# Python'da json modulini import qilish
import json

# JSON ma'lumotlarini Python obyektlariga aylantirish uchun json.loads() funksiyasidan foydalanamiz.
# filename = 'bemor.json' 
# with open(filename) as file:
#   bemor = json.load(file)

# print(type(bemor)) 
# print(bemor)

# Python obyektini (dict, list) JSON ga aylantirish — json.dumps()
talaba = {
  "ism":"Anvar",
  "yosh":23,
  "fanlar":["matematika","fizika"]
}

json_str = json.dumps(talaba, indent=4)
print(json_str)
'''
Eslatma:
dumps() — Python obyektini JSON matn (string) ga aylantiradi

indent=4 — chiroyli formatda chiqarish
'''

# JSON matnini Python obyektiga aylantirish — json.loads()
json_str = '''
{
    "ism": "Ali",
    "yosh": 22,
    "fanlar": ["Matematika", "Fizika"]
}
'''
python_obj = json.loads(json_str)
print(python_obj["fanlar"]) # ['Matematika', 'Fizika']

# JSON'ni faylga yozish — json.dump()
with open("student.json", 'w') as file:
  json.dump(talaba, file, indent=4)
  
# Eslatma: dump() — Python obyektini to‘g‘ridan-to‘g‘ri faylga JSON formatda yozadi.

# JSON fayldan o‘qish — json.load()
with open('student.json', 'r') as file:
  data = json.load(file)
print(data["yosh"]) # 23
  
