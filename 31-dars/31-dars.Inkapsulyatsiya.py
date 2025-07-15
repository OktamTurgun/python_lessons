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

'''
Klassga xos xususiyatlar va metodlar
Tushuncha
Turi	                                     Tavsif
Obyektga xos xususiyat	                   self. bilan e’lon qilinadi
Klassga xos xususiyat	                     Barcha obyektlar uchun umumiy (ClassName. orqali)
Obyektga xos metodlar	                     Oddiy metodlar (self)
Klassga xos metodlar	                     @classmethod va cls bilan
Statik metodlar	                           @staticmethod — obyektga ham, klassga ham bog‘liq emas
'''
# Example:
class Talaba:
    universitet = "TATU"  # Klassga xos xususiyat

    def __init__(self, ism, yosh):
        self.ism = ism           # Obyektga xos xususiyat
        self.__yosh = yosh       # Inkapsulyatsiya (private)

    def get_yosh(self):          # Getter
        return self.__yosh

    @classmethod
    def univers_nomi(cls):       # Klassga xos metod
        return cls.universitet

    @staticmethod
    def hisobla_yosh(t_yil):
        from datetime import date
        return date.today().year - t_yil
      
# Ishlatish:
talaba1 = Talaba("Olim", 25)
print(talaba1.ism)               # Obyekt xossasi
print(talaba1.get_yosh())        # Private xossaga kirish
print(Talaba.univers_nomi())     # Klass metodi
print(Talaba.hisobla_yosh(1999)) # Statik metod

'''
Jadval bilan umumlashtirish

| Turi           | Belgilanishi      | Kirish usuli                         | Misol                       |
| -------------- | ----------------- | ------------------------------------ | --------------------------- |
| Obyekt xossasi | `self.ism`        | `obj.ism`                            | `talaba1.ism`               |
| Klass xossasi  | `Class.ism`       | `obj.klass_nomi`, `Class.klass_nomi` | `Talaba.universitet`        |
| Obyekt metodi  | `def metod(self)` | `obj.metod()`                        | `talaba1.get_info()`        |
| Klass metodi   | `@classmethod`    | `Class.metod()`                      | `Talaba.get_count()`        |
| Statik metod   | `@staticmethod`   | `Class.metod()`                      | `Talaba.hisobla_yosh(1990)` |

Yodda tuting! 

| Qoidalar                                              | Tavsiyalar                               |
| ----------------------------------------------------- | ---------------------------------------- |
| `self` — obyektga tegishli narsa uchun                | Har doim `__init__` va metodlarda kerak  |
| `cls` — klassga tegishli narsa uchun                  | Faqat `@classmethod` metodda ishlatiladi |
| `@staticmethod` — klassdan mustaqil funksiyalar uchun | Hech `self` ham, `cls` ham kerak emas    |

'''

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
print(avto1.get_km(), "km")
avto1.add_km(-10000) # Mashinaning km ni kamaytirib bo'lmaydi! 

# Exercise: 3
class Avto:
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        if km>0:
            self.__km += km
        else:
            print("Mashinaning km ni kamaytirib bo'lmaydi!")

avto2 = Avto("Chevrolet","Tahoe","Qora",2024,85000,10000)
print(avto2.get_km()) # 1000
print(avto2.get_id()) # 223d1063-5a41-4e81-8310-0aca0e801624
avto2.add_km(7000)
print(avto2.get_km()) # 1700

avto3 = Avto("Mercedes_Benz","AMG EQS Sedan","Polar White",2025,147550)
avto4 = Avto("Porsche","718 Cayman","Black",2025,74800)
avto5 = Avto("Ferrari","Ferrari Daytona SP3","Red",2025,2223935)
print(Avto.get_num_avto()) # 4
            