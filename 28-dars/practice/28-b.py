"""
Klass komponentlari

Komponent	               Tavsifi	                                                         Misol
__init__	               Konstruktor - ob'ekt yaratilganda avtomatik ishlaydi	             def __init__(self, x):
self	                   Joriy ob'ektga havola (har bir metodda birinchi parametr)	       self.nom = nom
Class atribut	           Barcha ob'ektlar uchun umumiy (klassga tegishli)	                 tur = "odam"
Instance atribut	       Har bir ob'ekt uchun alohida	                                     self.ism = ism
Static metod	           Klassga tegishli, lekin ob'ektga bog'liq bo'lmagan metod	         @staticmethod def info():
Class metod	             Klassga tegishli metod (ob'ekt emas)	                             @classmethod def create(cls):
"""
class Avto:
  # Class atribut
  price = 10000 # Barcha avtolar uchun umumiy
  
  def __init__(self,model,rang,yil):
    # Instance atributlar
    self.model = model
    self.rang = rang
    self.yil = yil
    self.km = 0
    
  # Oddiy method  
  def drive(self,masofa):
    self.km += masofa
    print(f"{masofa} km yurildi, Jami: {self.km} km")
    
  # Class method
  @classmethod
  def narhni_oshir(cls, foiz):
    cls.price *= (1 + foiz/100)
    print(f"Yangi narh: {cls.price}")
    
  # Static method
  @staticmethod
  def tekshir(yil):
    return "yangi" if yil > 2024 else "Eski"
  
# Obyekt yaratish
avto1 = Avto("Tesla","qora",2023)
avto2 = Avto("BMW","oq",2020)

# Methodlarni chaqirish
avto1.drive(200) # 200 km yurildi, Jami: 200 km
Avto.narhni_oshir(10) # Yangi narh: 11000.0
print(Avto.tekshir(avto2.yil)) # Eski



 