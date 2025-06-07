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

