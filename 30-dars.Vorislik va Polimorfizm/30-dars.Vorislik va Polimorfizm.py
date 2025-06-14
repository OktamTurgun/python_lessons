"""
Created on Fri Jun 13 21:59:14 2025

30-dars.  Vorislik va Polimorfizm (Inheritance & Polymorphism)

@author: uktam
"""
class Shaxs:
  """Shaxslar haqida ma'lumot"""
  def __init__(self,ism,familiya,passport,tyil):
    self.ism = ism
    self.familiya = familiya
    self.passport = passport
    self.tyil = tyil
    
  def get_info(self):
    """Shahs haqida ma'lumot"""
    info = f"{self.ism} {self.familiya}. "
    info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
    return info
  
  def get_age(self,yil):
    """Shaxsning yoshini qaytaruvchi method"""
    return f"Yosh: {yil - self.tyil}"

person1 = Shaxs("Hasan","Olimov","FB0011223",2002)
person2 = Shaxs("Abdulloh","Karimov","AN0007456",1990)

# print(person1.get_info()) # Hasan Olimov. Passport: FB0011223, 2002-yilda tug'ilgan
# print(person2.get_info()) # Abdulloh Karimov. Passport: AN0007456, 1990-yilda tug'ilgan
# print(person1.get_age(2025)) # 23
# print(person2.get_age(2025)) # 35""

class Student(Shaxs):
  """Student klassi"""
  def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
    super().__init__(ism,familiya,passport,tyil)
    self.idraqam = idraqam
    self.bosqich = 1
    self.manzil = manzil
    
  def get_id(self):
    """Talabaning id raqamini qaytaradi"""
    return f"ID raqam: {self.idraqam}"
  
  def get_bosqich(self):
    """Talabaning o'qiyotgan bosqichini qaytaradi"""
    return self.bosqich
  
  def get_info(self):
    """Talaba xaqida ma'lumotlar"""
    info = f"{self.ism} {self.familiya}. "
    info += f"{self.get_bosqich()}-bosqich. {self.get_id()}. "
    info += f"{self.manzil.get_manzil()}."
    return info
  
class Manzil:
  """manzil saqlash uchu class"""
  def __init__(self,uy,kocha,tuman,viloyat):
    self.uy = uy
    self.kocha = kocha
    self.tuman = tuman
    self.viloyat = viloyat
    
  def get_manzil(self):
    """Manzilni ko'rish"""
    # Agar 'shahar' so'zi bo'lsa, o'zini yozamiz
    if 'shahar' in self.viloyat.lower():
        hudud = self.viloyat  # Masalan: Toshkent shahri
    else:
        hudud = f"{self.viloyat} viloyati"  # Masalan: Andijon viloyati
        
    manzil = f"{hudud}, {self.tuman} tumani, "
    manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
    return manzil
    
  

# student2 = Student("Bunyod","Jumanov","PS000123",1999,"NS098765")

# print(student1.get_id()) # ID: NO009876
# print(student2.get_bosqich()) # Bosqich: 1
# print(student2.get_info()) # Ahmad Imomov. 1-bosqich. ID raqam: NO009876.
# print(student2.get_age(2025)) # Yosh: 26

student1_manzil = Manzil(47,"Olmozor","Chilonzor","Toshkent shahar")
student1 = Student("Ahmad","Imomov","DS232233",1997,"NO009876",student1_manzil)
student2_manzil = Manzil(12,"Mavazor","Narpay","Samarqand")
student2 = Student("Bunyod","Jumanov","PS000123",1999,"NS098765",student2_manzil)

print(student1.manzil.get_manzil())

print(student1.get_info())
print(student2.get_info())
