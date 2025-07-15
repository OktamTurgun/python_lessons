"""
Amaliy mashq:
O‘zingiz haqingizdagi ma’lumotlardan iborat Python dictionary tuzing.
Uni json faylga yozing.
Keyin o‘sha fayldan o‘qing va konsolga chiqarib bering.
"""
shaxs = {
  "ism": "Abbos",
  "familiya":"Sobitxanov",
  "yosh": 34,
  "kasb": "Duradgor",
  "manzil": [
    {
      "uy":147,
      "kocha":"Quruvchilar",
      "mahalla":"Obod",
      "tuman":"Uchqo'rg'on",
      "viloyat":"Namangan",
      "davlat":"Uzbekistan"
    }
  ],
  "oila":True,
  "farzandlar":[
    {
      "ism":"Soliha",
      "yosh":7
    },
    {
      "ism":"Ahmad",
      "yosh":3
    }
  ],
  "hobbi":["futbol", "suzish", "qo'shiq aytish"]
}

import json

# JSON faylga yozish
with open('shaxs.json', 'w') as file:
  json.dump(shaxs, file, indent=4) 
  
# JSON fayldan o'qish
with open('shaxs.json', 'r') as file:
  shaxs_dat = json.load(file)
  
print(shaxs_dat)


# JSON bilan ko‘p ishlatiladigan kodlar tayyor to‘plami

# Python -> JSON string
obj = {
    "ism": "Ali",
    "yosh": 22
}
import json
json_str = json.dumps(obj)

# JSON string -> Python
obj = json.loads(json_str)

# Python -> JSON faylga
json.dump(obj, open("file.json", "w"), indent=4)

# Fayldan JSON -> Python
obj = json.load(open("file.json"))

