"""
Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan 
sonni 2 dan 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini tekshirib, 
 konsolga chiqaring. 
"""
num = int(input("Butun son kiriting: "))
# Option 1
for i in range(2,11):
  if num % i == 0:
    print(f"{num} soni {i} ga qoldiqsiz bo'linadi")

# Option 2
for n in range(2,11):
    if not (num%n):
        print(f"{num} soni {n} ga qoldiqsiz bo'linadi")