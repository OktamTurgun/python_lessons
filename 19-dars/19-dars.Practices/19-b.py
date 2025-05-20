"""
Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
"""
def hisobla():
  """Foydalanuvchidan son qabul qilib, sonni kvadrati va kubini qaytaruvchi funksiya"""
  num = int(input("Son kiriting: "))
  square = num ** 2
  cube = num ** 3
  print(f"{num} ning kavdrati: {square}\n"
        f"{num} ning kubi: {cube}")
  
hisobla()

''''''
# Yanada optimallashgan versiyada
def kvadrat_kub(num: int) -> tuple:
  """Berilgan sonni kvadrati va kubini hisoblaydi"""
  return num **2, num **3
def hisobla():
  """Foydalanuvchidan son qabul qilib, uning kvadrati va kubini chiqaradi."""
  while True:
    try:
      num = int(input("Son kiriting: "))
      kvadrat, kub = kvadrat_kub(num)
      print(f"{num} ning kvadrati: {kvadrat}\n"
            f"{num} ning kubi: {kub}")
      return
    except ValueError:
      print("Noto'g'ri kiritish! Faqat butun son kiriting.")
  
if __name__ == "__main__":
  hisobla()
  