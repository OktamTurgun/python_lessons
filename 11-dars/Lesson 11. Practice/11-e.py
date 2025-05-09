"""
users nomli ynagi ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring
"""

# users = ['ahmad_04', 'asror_01', 'bobur_03', 'jasur_03', 'olim_05']
# login = input("Yangi login tanlang: ").lower().strip()

# if login in users:
#   print("Login band, yangi login tanlang!")
# else: 
#   print(f'Xush kelibsiz, {login.title()}!')

"""Set sifatida saqlash tezroq qidirish uchun"""
users = {'ahmad_04', 'asror_01', 'bobur_03', 'jasur_03', 'olim_05'}
login = input("Yangi login tanlang: ").lower().strip()

message = "Login band, yangi login tanlang!" if login in users else f"Xush kelibsiz! {login.title()}"
print(message)