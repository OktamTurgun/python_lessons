# Eslatmalar:
# json.loads() string formatdagi JSON ni o'qiydi

# json.load() esa fayl obyektini o'qiydi

"""
# Example 1:
Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: 
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
"""
import json

data = {
  "Model":"Malibu",
  "Rang":"Qora",
  "Yil":2024,
  "Narh":40000
}

avto_json = json.dumps(data, indent=4)
# print(avto_json)
# print(type(avto_json))
# print(type(data))

# Example 2:
# Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring: 
talaba_json = """
{
  "ism":"Hasan",
  "familiya":"Husanov",
  "tyil":2000
}
"""
# JSON matnni Python obyektiga aylantirish
talaba = json.loads(talaba_json)
# Obyektdan ism va familiyani chiqarish
print(f"Talaba ismi: {talaba['ism']}")
print(f"Talaba familiyasi: {talaba['familiya']}")

# Example 3:
# Ushbu JSON faylni oching, va talabaning ismi va familiyasini  konsolga chiqaring:
# talaba.json faylni oching.

# JSON fayldan o'qish
with open('C:/Users/User/Documents/GitHub/python_lessons/python_lessons/34-dars.JSON/data/talaba.json', 'r') as file:
    talaba = json.load(file)
# Obyektdan ism va familiyani chiqarish
print(f"Talaba ismi: {talaba['ism']}")
print(f"Talaba familiyasi: {talaba['familiya']}")

# Example 4:
# Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
with open('data.json', 'w') as file:
  json.dump(data,file)
  
with open('talaba1.json', 'w') as file:
  json.dump(talaba,file)


# Quyidagi JSON faylni yuklab oling. 
# Faylda 3 ta talabaning ism va familiyasi saqlangan.
# Ularning har birini alohida qatordan 
# "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida konsolga chiqaring.

# with open(r'C:\Users\User\Documents\GitHub\python_lessons\python_lessons\34-dars.JSON\data\students_1.json', 'r') as f:
#   data = json.load(f)
  
# for talaba in data['student']:
#   print(f"Talaba: {talaba['name']} {talaba['lastname']}, {talaba['year']}-kurs, {talaba['faculty']} fakulteti talabasi")
  
with open(r'C:\Users\User\Documents\GitHub\python_lessons\python_lessons\34-dars.JSON\data\shaxs.json', 'r', encoding='utf-8') as file:
  shaxs = json.load(file)
  
print(f"Ism: {shaxs['ism']} {shaxs['familiya']}, Yosh: {shaxs['yosh']}, Kasb: {shaxs['kasb']}")

print(f"{shaxs['ism']} {shaxs['familiya']} ({shaxs['yosh']} yosh)")
print(f"Kasbi: {shaxs['kasb']}")
print("\nFarzandlar:")
for i, farzand in enumerate(shaxs['farzandlar'], 1):
    print(f"{i}. {farzand['ism']} ({farzand['yosh']} yosh)")
    
manzil = shaxs['manzil'][0]
print(f"Manzil: {manzil['uy']}-uy, {manzil['kocha']} ko'chasi")

print(f"""Oilali: {'Ha' if shaxs['oila'] else "Yo'q"}""")
