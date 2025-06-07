"""
Created on Sat June 07 06:30:46 2025

28-dars. Klasslar

@author: uktam
"""
class Talaba:
    def __init__(self,ism,familiya,t_yil):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        
    def get_name(self):
        return self.ism
    def get_lastname(self):
        return self.familiya
    
    def get_age(self,yil):
        return yil - self.t_yil
    
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya} {self.t_yil}-yilda tug'ilganman"
        
        
talaba1 = Talaba("Olim","Alimov",2002)
talaba2 = Talaba("Ahmad","Bakirov",1999)
talaba3 = Talaba("Otabek","Usmonov",2005)

# Klass yaratish va ishlatish
class Ishchi:
    # Konstruktor (__init__ metodi)
    def __init__(self, ism, yosh):
        self.ism = ism  # instance atribut
        self.yosh = yosh
    
    # Metod
    def tanishtir(self):
        return f"Mening ismim {self.ism}, men {self.yosh} yoshdaman"

# Klassdan ob'ekt yaratish
hisobchi = Ishchi("Ali", 25)
usta1 = Ishchi("Kozim", 32)
usta2 = Ishchi("Botir", 35)
print(hisobchi.tanishtir())  # Mening ismim Ali, men 25 yoshdaman
print(usta1.tanishtir())  # Mening ismim Kozim, men 32 yoshdaman
print(usta2.tanishtir())  # Mening ismim Botir, men 35 yoshdaman

"""
Klass komponentlari

Komponent	           Tavsifi	                                                                  Misol

__init__	           Konstruktor - ob'ekt yaratilganda avtomatik ishlaydi	                      def __init__(self, x):
self	               Joriy ob'ektga havola (har bir metodda birinchi parametr)	                self.nom = nom
Class atribut	       Barcha ob'ektlar uchun umumiy (klassga tegishli)	                          tur = "odam"
Instance atribut	   Har bir ob'ekt uchun alohida	                                              self.ism = ism
Static metod	       Klassga tegishli, lekin ob'ektga bog'liq bo'lmagan metod	                  @staticmethod def info():
Class metod	         Klassga tegishli metod (ob'ekt emas)	                                      @classmethod def create(cls):
"""
# Exercises 2
class Avto:
    # Class atribut
    narx = 10000  # Barcha avtolar uchun umumiy
    
    def __init__(self, model, rang, yil):
        # Instance atributlar
        self.model = model
        self.rang = rang
        self.yil = yil
        self.km = 0
    
    # Oddiy metod
    def drive(self, masofa):
        self.km += masofa
        print(f"{masofa} km yurildi. Jami: {self.km} km")
    
    # Klass metodi
    @classmethod
    def narxni_oshir(cls, foiz):
        cls.narx *= (1 + foiz/100)
        print(f"Yangi narx: {cls.narx}")
    
    # Static metod
    @staticmethod
    def tekshir(yil):
        return "Yangi" if yil > 2020 else "Eski"

# Ob'ekt yaratish
avto1 = Avto("Tesla", "qora", 2022)
avto2 = Avto("BMW", "oq", 2018)

# Metodlarni chaqirish
avto1.drive(150)  # 150 km yurildi. Jami: 150 km
Avto.narxni_oshir(10)  # Yangi narx: 11000
print(Avto.tekshir(avto2.yil))  # Eski
