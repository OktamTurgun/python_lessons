"""
Created on Sun June 08 16:30:46 2025

29-dars. Obyeklar bilan ishlash

@author: uktam
"""
class Talaba:
    def __init__(self,ism,familiya,t_yil):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.bosqich = 1
        
    def set_bosqich(self,yangi_bosqich):
        self.bosqich = yangi_bosqich
        
    def update_bosqich(self):
        self.bosqich += 1
        
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi {self.t_yil}-yilda tug'ilgan"
    
    def get_fullname(self):
        return f"{self.ism} {self.familiya}"
    
# talaba1 = Talaba("Alijon","Valiyev",2002)
# print(talaba1.get_info())
# talaba1.bosqich = 2 # Tavsiya qilinmaydi
# print(talaba1.get_info())
# talaba1.update_bosqich()
# talaba1.set_bosqich(3)
# print(talaba1.get_info())

class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    # Fan klassiga kiruvchi talabalar haqida batafsil ma’lumot chiqarish:
    def show_students_info(self):
        for talaba in self.talabalar:
            print(talaba.get_info())
        
    def get_students(self):
        return [talaba.get_fullname() for talaba in self.talabalar]
    
    def get_students_num(self):
        return self.talabalar_soni
    
    # Barcha talabalarni bosqichini oshirish:
    def update_all_students(self):
       for talaba in self.talabalar:
           talaba.update_bosqich()
    
    # Fanni umumiy ma’lumotlari bilan ko‘rsatish:
    def get_info_subject(self):
        return f"{self.nomi} fanida {self.talabalar_soni} nafar talaba bor"
    
def show_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]
    
matematika = Fan("Oliy matematika")
talaba1 = Talaba("Olim","Salimov",2004)
talaba2 = Talaba("Odil","Bakirov",2005)
talaba3 = Talaba("Umid","Qosimov",2000)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

matematika.show_students_info()

print(matematika.get_info_subject()) # Oliy matematika fanida 3 nafar talaba bor

matematika.update_all_students()

# print(f"Talabalar soni: {matematika.talabalar_soni} nafar") # Talabalar soni: 3 nafar
# print(matematika.get_students()) # ['Olim Salimov', 'Odil Bakirov', 'Umid Qosimov']
# print(matematika.talabalar[2].get_info()) # Umid Qosimov. 1-bosqich talabasi
# print(matematika.talabalar[0].get_info()) # Olim Salimov. 2-bosqich talabasi 2004-yilda tug'ilgan
    
# print(show_methods(Talaba))  
# show_methods(Fan) 
# print(show_methods(str)) 

print(talaba1.__dict__) # {'ism': 'Olim', 'familiya': 'Salimov', 't_yil': 2004, 'bosqich': 2}
print(talaba1.__dict__.keys()) # dict_keys(['ism', 'familiya', 't_yil', 'bosqich'])
print(talaba3.__dict__.values()) # dict_values(['Umid', 'Qosimov', 2000, 2])

print(show_methods(talaba2)) # ['bosqich', 'familiya', 'get_fullname', 'get_info', 'ism', 'set_bosqich', 't_yil', 'update_bosqich']
        