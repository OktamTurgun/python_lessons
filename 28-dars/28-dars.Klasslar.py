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