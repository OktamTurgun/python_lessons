"""
Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya.
"""
# def tugilgan_yil():
#   """Foydalanuvchi yoshini sorab, tig'ilgan yilini xisoblovchi funksiya"""
#   name = input("Ismingizni kirting: ")
#   age = int(input("Yoshingizni kiriting: "))
#   birthofdate = 2025 - age
#   print(f"Salom {name.title()}, siz {birthofdate}-da tug'ilgansiz!")
  
# tugilgan_yil()

''''''
# Agar funksiya parametrlar orqali qiymat oladigan bo'lsa

# def t_yil(name, age):
#   print(f"Salom {name.title()}, siz {2025 - age}-yilda tugilgansiz!")
  
# name = input("Ismingizni kiriting: ").strip().lower()
# age = int(input("Yoshingizni kiriting: "))
  
# t_yil(name, age) 

''''''
# Tug'ilgan yiliga qarab maxsus mas;axatlar beruvchi dastur
def tugilgan_yil():
  name = input("Ismingizni kiriting: ")
  age = int(input("Yoshingizni kiriting: "))
  t_yil = 2025 - age
  
  if age < 12: return f"{name.title()} {t_yil}-yilda tug'ilgansiz. Siz ko'proq o'qing va yana o'qing! Ilm o'rganing."
  elif age < 20: return f"{name.title()} {t_yil}-yilda tug'ilgansiz.  Yaxshi do'stlar orttiring, ilm o'rganishda davom eting!"
  elif age < 30: return f"{name.title()} {t_yil}-yilda tug'ilgansiz.  Siz kasbingizni mustahkamlang! Behuda narsalarga chalg'imang."
  else: return f"{name.title()} {t_yil}-yilda tug'ilgansiz.  Tajribangizni yoshlarga ulashing!"
  
  
print(tugilgan_yil())