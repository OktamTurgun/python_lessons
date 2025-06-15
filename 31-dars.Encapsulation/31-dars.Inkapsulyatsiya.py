"""
Created on Sub Jun 15 11:17:14 2025

31-dars.  OOP. Inkapsuyyatsiya. Klassga xos xususiyat va methodlar

@author: uktam
"""
# Inkapsulyatsiya — klass ichidagi ma’lumotlar va funksiyalarni tashqi
# koddan yashirish (himoyalash). Bu orqali noto‘g‘ri ishlov berishdan himoyalanadi.

'''
| Daraja                   | Belgisi    | Tavsif                                                    |
| ------------------------ | ---------- | --------------------------------------------------------- |
| Ochiq (public)           | `self.x`   | Klass tashqarisidan foydalanish mumkin                    |
| Himoyalangan (protected) | `_self.x`  | Tashqaridan ishlatish mumkin, lekin bu tavsiya qilinmaydi |
| Yashirin (private)       | `__self.x` | Klass tashqarisidan foydalanish mumkin emas (bevosita)    |

'''
# Exercise:
class BankHisobi:
    def __init__(self, ism, balans):
        self.ism = ism               # Ochiq
        self._balans = balans       # Himoyalangan
        self.__pin = "1234"         # Yashirin (private)

    def get_pin(self):
        return self.__pin

    def set_pin(self, yangi_pin):
        self.__pin = yangi_pin

# Ishlatish:
hisob = BankHisobi("Anvar", 5000)
# print(hisob.ism)        # OK
# print(hisob._balans)    # MUMKIN, lekin tavsiya qilinmaydi1
# print(hisob.__pin)      # ERROR: private maydon
# print(hisob.get_pin())  # To‘g‘ri yo‘l: getter orqali olish

# Exercise: 2
from uuid import uuid4

class Avto:
  """Avtomobil klassi"""
  def __init__(self,make,model,rang,yil,narh,km=0):
    self.make = make
    self.model = model
    self.rang = rang
    self.yil = yil
    self.narh = narh
    self.__km = km
    self.__id = uuid4()
    
  def get_km(self):
    return self.__km
  
  def get_id(self):
    return self.__id

  def add_km(self,km):
      """Amshinaning kmga yana km qo'shadi"""
      if km>0:
          self.__km += km
      else:
          print("Mashinaning km ni kamaytirib bo'lmaydi!")

avto1 = Avto("GM","Malibu","Oq",2024,35000,20000)
print(avto1.get_km(), "km")
print(f"ID: {avto1.get_id()}")
avto1.add_km(2300)
print(avto1.get_km())
avto1.add_km(-10000) # 














