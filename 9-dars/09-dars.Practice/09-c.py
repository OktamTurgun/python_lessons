"""
Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, 
va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
"""
films = []
print("Iltimos! 5 ta eng sevimli kinoyingizni kiriting: \n>>>")
for n in range(5):
  films.append(input(f"{n+1}-eng sevimli kinoyingiz: ").title())
print(f"\nSiz sevgan 5ta filmlar:\n" + ', ' .join(films))