"""
Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq 
xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
"""
from uuid import uuid4

class Shaxs:
  """Shaxslar haqida ma'lumot"""
  def __init__(self,ism,familiya,passport,tyil):
    self.ism = ism
    self.familiya = familiya
    self.__passport = passport
    self.tyil = tyil
    self.__id = uuid4()
    
  def get_id(self):
    return self.__id
  
  def get_info(self):
    """Shahs haqida ma'lumot"""
    info = f"{self.ism} {self.familiya}. "
    info += f"Passport: {self.__passport}, {self.tyil}-yilda tug'ilgan"
    return info
  
  def get_age(self,yil):
    """Shaxsning yoshini qaytaruvchi method"""
    return f"Yosh: {yil - self.tyil}"
  
class Student(Shaxs):
  __num_student = 0
  """Student klassi"""
  def __init__(self,ism,familiya,passport,tyil,manzil):
    super().__init__(ism,familiya,passport,tyil)
    self.__id = uuid4()
    self.bosqich = 1
    self.__manzil = manzil
    Student.__num_student += 1
    
  @classmethod
  def get_num_students(cls):
    return cls.__num_student
    
  def get_id(self):
    """Talabaning id raqamini qaytaradi"""
    return f"ID raqam: {self.__id}"
  
  def get_bosqich(self):
    """Talabaning o'qiyotgan bosqichini qaytaradi"""
    return self.bosqich
  
  def get_info(self):
    """Talaba xaqida ma'lumotlar"""
    info = f"{self.ism} {self.familiya}. "
    info += f"{self.get_bosqich()}-bosqich. {self.get_id()}. "
    info += f"{self.__manzil.get_manzil()}."
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
  
student1_manzil = (147,"Jarqo'rg'on","Chelak","Buxoro")
student1 = Student("Anvar","Qobilov","AB098123",2000,student1_manzil)

student2_manzil = (73,"Obodon","Norin","Namangan")
student2 = Student("Sobit","Obidov","Ak098435",2002,student2_manzil)

student3_manzil = (7,"Mustaqillik","Qamashi","Qashqadaryo")
student3 = Student("Asror","Kamolov","AB098123",1998,student3_manzil)

print(Student.get_num_students())