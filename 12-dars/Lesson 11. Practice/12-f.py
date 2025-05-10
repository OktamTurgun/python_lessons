"""
Xatolar bilan ishlash.
"""
# Xato yozilgan code:
# users = ['alisher1983','aziza','yasina' 'umar']

# login = input("Yangi login tanlang:' )

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")

# To'g'girlangan va yaxshilangan code:
users = ['alisher1983','aziza','yasina', 'umar'] # 'yasina' 'umar' elementlar vergul (,) bilan ajratilmagan

while True: # user band login kiritganda qayta-qayta sorash uchun while loopdan foydalanildi.
  login = input("Yangi login tanlang: ").strip() # Qo'shtirnoqlar xato (ikki xil) yozilgan va line oxirida noto'g'ri joy

  if login.lower() in users:
      print(f" '{login}' logini band, yangi login tanlang!") # Addiy string mantiqiy xatolar xam bor(tanalng) so'zini => tanlang
  else:
      print(f"Xush kelibsiz! {login} Siz ro'yxatdan muoffaqiyatli o'tdingiz!")
      break # Agar login band bo'lmasa while loop to'xtaydi 