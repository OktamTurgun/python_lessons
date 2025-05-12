"""
otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga 
shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri
manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring
   :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
"""
family = {
  'otam': {
    'ism':'Abdulloh', 
    'birth_year':1956,
    'address':'Samarqand shahri',
    'profession':"o'qituvchi"
  },
  'onam': {
    'ism':'Halima',
    'birth_year':1960,
    'address':"farg'ona shahri",
    'profession':'shifokor',
  },
  'akam': {
    'ism':'Xurshid',
    'birth_year':1988,
    'address':'toshkent shahri',
    'profession':'uchuvchi'
  },
  'singlim': {
    'ism':'Gulhumor',
    'birth_year':1999,
    'address':'toshkent shahri',
    'profession':"o'quvchi"
  }
}
''' Oddiy usul xar bir a'zo uchun alohida '''
# print(f"Otamning ismi: {family['otam']['ism'].capitalize()}, "
#       f"Tug'ulgan yili: {family['otam']['birth_year']}-yil, "
#       f"Manzili: {family['otam']['address'].capitalize()}, "
#       f"Kasbi: {family['otam']['profession'].capitalize()}")

# print(f"Onamning ismi: {family['onam']['ism'].capitalize()}, "
#       f"Tug'ulgan yili: {family['onam']['birth_year']}-yil, "
#       f"Manzili: {family['onam']['address'].capitalize()}, "
#       f"Kasbi: {family['onam']['profession'].capitalize()}")

''' For loop yordamida (barcha a'zolar uchun) '''
for member, info in family.items():
  print(f"{member.capitalize()}ning ismi: {info['ism']}, "
        f"Tug'ilgan yili: {info['birth_year']}-yil, "
        f"Manzili: {info['address']}da tug'ilgan, "
        f"Kasbi: {info['profession']}")
  
''' Chiroyli formatlash f-string'dan foydalanib '''
for relation, info in family.items():
  print(f"""
        {relation.upper()} HAQIDA:
        Ismi: {info['ism']}
        Tug'ilgan yili: {info['birth_year']}-yil
        Kasbi: {info['profession'].capitalize()}
        Manzili: {info['address'].title()}
        """)
