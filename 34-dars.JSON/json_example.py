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

bemor_json = json.dumps(bemor)
print(bemor_json)

bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)

with open('bemor.json', 'w') as file:
    json.dump(bemor,file)
    
bemor2 = json.loads(bemor_json)

with open('bemor.json', 'r') as file:
    data = file.read().strip().replace('\n', '')
    
with open('sonlar.json', 'w') as file:
    json.dump(sonlar,file)
    
with open('sonlar.json', 'r') as file:
    dat = file.read().strip().replace('\n', '')

print(data)
print(dat)



