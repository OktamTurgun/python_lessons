"""
Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga
qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
"""
def divide(num):
  """Berilgan sonni 2 dan 10 gacha bo'lgan sonlarga bo'linishini tekshiradi."""
  divisors = []
  for n in range(2,11):
    if num % n == 0:
      divisors.append(n)
  if divisors:
    print(f"\n{num} soni quyidagi sonlarga qoldiqsiz bo'linadi: \n"
          f"Bo'luvchilar: {', '.join(map(str, divisors))}"
          f"\n{'-'*50}")
    for divisor in divisors:
      print(f"{num} / {divisor} = {num / divisor:.1f}")  
  else:
    print(f"\n{num} 2 dan 10 gacha sonlarga qoldiqsiz bo'linmaydi"
          f"\n{'-'*50}")

numbers_to_check = [42, 13, 126, 17, 90, 2520]
for number in numbers_to_check:
  divide(number)


''''''
def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)

''''''
def divide(num):
    """Berilgan sonni 2 dan 10 gacha bo'lgan sonlarga bo'linishini tekshiradi."""
    
    # 2-10 oralig'idagi bo'luvchilarni topish
    divisors = [n for n in range(2, 11) if num % n == 0]
    
    if divisors:
        # Asosiy natijani chiqarish
        print(f"\n{'-'*50}")
        print(f"🔍 {num} soni quyidagi sonlarga qoldiqsiz bo'linadi:")
        print(f"📊 Bo'luvchilar: {', '.join(map(str, divisors))}")
        print(f"{'-'*50}")
        
        # Har bir bo'luvchi uchun batafsil
        for divisor in divisors:
            result = num / divisor
            print(f"• {num} / {divisor} = {result:.1f}")
    else:
        print(f"\n{'-'*50}")
        print(f"🔍 {num} soni 2 dan 10 gacha sonlarga qoldiqsiz bo'linmaydi")
        print(f"{'-'*50}")

# Test qilish
numbers_to_check = [42, 13, 126, 7]
for number in numbers_to_check:
    divide(number)