"""
Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa,
 "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
xabarini konsolga chiqaring. Aks holda, 
 "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
"""
user = input('Ismingizni kiriting: ')
if user.lower() == 'admin':
  print("Xush kelibsiz, Admin.\nFoydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print(f"Xush kelibsiz! {user.title()}!")