"""
Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
"""
def juft_toq():
  """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
  num = int(input("Son kiriting: "))
  if num % 2 == 0:
    print(f"{num}: Juft son.")
  elif num % 2 != 0:
    print(f"{num}: Toq son.")
  else:
    print("Musbat son kiriting!")
    
juft_toq()

''''''
def juft_toq(num):
  """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
  if num % 2 == 0:
    print(f"{num}: Juft son.")
  elif num < 0 and num % 2 == 0:
    print(f"{num}: Manfiy juft son")
  elif num < 0 and num % 2 != 0:
    print(f"{num}: Manfiy toq son")
  elif num % 2 != 0:
    print(f"{num}: Toq son.")
  else:
    print("Musbat son kiriting!")
    
juft_toq(-245)

''''''
def juft_toq():
  """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
  while True:
    try:
      num = int(input("Son kiriting: (0 chiqish uchun) "))
      if num == 0:
        print("Dastur to'xtatildi.")
        break
      elif num < 0:
        print(f"{num}: manfiy son. Mubat son kiriting.")
        continue
      elif num % 2 != 0:
        print(f"{num}: Toq son.")
      else:
        print("Juft son.") 
    except ValueError:
      print("Noto'g'ri kiritish, musbat son kiriting.")
      
juft_toq()