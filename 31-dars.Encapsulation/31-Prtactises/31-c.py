"""
Quyidagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing 
"""
from uuid import uuid4
import datetime

class Shaxs:
  __persons_num = 0
  
  """Shaxslar haqida ma'lumot"""
  def __init__(self,ism,familiya,passport,tyil):
    self.__ism = ism
    self.__familiya = familiya
    self.__passport = passport
    self.__tyil = tyil
    self.__id = uuid4()
    Shaxs.__persons_num += 1
    
  @classmethod
  def get_num_persons(cls):
    """Barcha yaratilgan shaxslar sonini qaytaradi"""
    return cls.__persons_num
    
  # Getter nethodlar
  def get_id(self):
    return self.__id
  
  def get_ism(self):
    return self.__ism
  
  def get_familiya(self): 
        return self.__familiya
  
  def get_passport(self):
    return self.__passport
  
  def get_age(self):
    """Shaxsning yoshini qaytaruvchi method"""
    joriy_yil = datetime.datetime.now().year
    return f"Yosh: {joriy_yil - self.__tyil}"
  
  def get_info(self):
    """Shahs haqida ma'lumot"""
    info = f"{self.__ism} {self.__familiya}. "
    info += f"Passport: {self.__passport}, {self.__tyil}-yilda tug'ilgan {self.get_age()}-yoshda"
    return info
  
  # Setter methodlar
  @classmethod
  def set_persons_num(cls, yangi_son):
    """Shaxslar sonini yangilash (faqat adminlar uchun)"""
    if isinstance(yangi_son, int) and yangi_son > 0:
      cls.__persons_num = yangi_son
    else:
      raise ValueError("Shaxslar soni manfiy bo'lishi mumkin emas!")
    
  @classmethod
  def persons_num_info(cls):
    """Klass haqida umumiy ma'lumot"""
    return f"Hozircha {cls.__persons_num} ta shaxs ro'yxatga olingan!"
    
  def set_ism(self, yangi_ism):
    if isinstance(yangi_ism, str) and len(yangi_ism) >= 2:
      self.__ism = yangi_ism
    else:
      raise ValueError("Ism 2 yoki undan ortiq belgidan iborat bo'lishi kerak!")
    
  def set_passport(self, new_passport):
    if isinstance(new_passport, str) and len(new_passport) == 8:
      self.__passport = new_passport
    else:
      raise ValueError("Passport 8 belgiga teng bo'lishi kerak!")
    
  def set_age(self, new_age):
    """Yoshni yangilash uchun method"""
    if not isinstance(new_age, int) or new_age <= 0:
      raise ValueError("Yosh musbat va butun son bo'lishi kerak!")
    
    joriy_yil = datetime.datetime.now().year
    self.__tyil = joriy_yil - self.__tyil
    print(f"Yosh {new_age} ga yangilandi")
  
class Student(Shaxs):
  __students_num = 0
  
  """Student klassi"""
  def __init__(self,ism,familiya,passport,tyil,bosqich = 1):
    super().__init__(ism,familiya,passport,tyil)
    self.__id = uuid4()
    self.__bosqich = bosqich
    Student.__students_num += 1
  
  @classmethod
  def get_num_students(cls):
    """Barcha yaratilgan talabalar sonini qaytaradi"""
    return cls.__students_num
    
  @classmethod
  def students_num_info(cls):
    return f"Horircha {cls.__students_num} ta talaba darsga kelgan!"
    
  # Getter methodlar
  def get_id(self):
    """Talabaning id raqamini qaytaradi"""
    return f"ID: {self.__id}"
  
  def get_bosqich(self):
    """Talabaning o'qiyotgan bosqichini qaytaradi"""
    return self.__bosqich
  
  def get_info(self):
    """Talaba xaqida ma'lumotlar"""
    info = f"Talaba: {self.get_ism()} {self.get_familiya()}, "
    info += f"Bosqich: {self.get_bosqich()}-bosqich. {self.get_id()}, "
    return info
          
  @classmethod
  def set_students_num(cls, yangi_son):
    """Talabalr soni yangilanadi"""
    if isinstance(yangi_son, int) and yangi_son >= 0:
      cls.__students_num = yangi_son
    else:
      raise ValueError("Talabalar soni manfiy bo'lishi mumkin emas!")
    
  def set_bosqich(self, yangi_bosqich):
        if isinstance(yangi_bosqich, int) and 1 <= yangi_bosqich <= 4:
            self.__bosqich = yangi_bosqich
        else:
            raise ValueError("Bosqich 1-4 oralig'ida bo'lishi kerak")
      
# Test qilish
shaxs1 = Shaxs("Ali", "Valiyev", "AB123456", 1990)
shaxs2 = Shaxs("Vali", "Aliyev", "CD654321", 1995)

talaba1 = Student("Hasan", "Husanov", "EF987654", 2000)
talaba2 = Student("Husan", "Hasanov", "GH456789", 2001)
talaba3 = Student("Eshmat", "Toshmatov", "IJ123987", 1999)

print(Shaxs.get_num_persons())  # 5 (2 shaxs + 3 talaba)
print(Student.get_num_students())  # 3

print(Shaxs.persons_num_info())  # "Hozircha 5 ta shaxs mavjud"
print(Student.students_num_info())  # "Hozircha 3 ta talaba mavjud"

# Sonlarni yangilash (masalan, ma'lumotlar bazasini yangilashda)
Student.set_students_num(5)
Shaxs.set_persons_num(7)