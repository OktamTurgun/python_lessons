'''
Avvalga darslarda yaratilgan obyektlarga (Shaxs, Student) turli dunder metodlarni qo'shishni mashq qiling. 
Obyekt haqida ma'lumot (__rerp__)
Talabalarni bosqichi bo'yicha solishtirish (__lt__,__eg__ va hokazo)
'''
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
  
  # Dunder methods
  def __repr__(self):
    """Shahs haqida ma'lumot"""
    info = f"Shaxs: {self.__ism} {self.__familiya}. "
    info += f"\nPassport: {self.__passport}, {self.__tyil}-yilda tug'ilgan, {self.get_age()}-yoshda, "
    info += f"\nID: {self.__id}"
    return info
  
  def __eq__(self,other):
    return self.__id == other.id
  
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
    
  # Dunder methods
  def __repr__(self):
    """Talaba haqida ma'lumotlar"""
    info = f"Talaba: {self.get_ism()} {self.get_familiya()} "
    info += f"\nPassport: {self.get_passport()} \n{self.get_age()}-yoshda, "
    info += f"{self.get_bosqich()}-bosqich talabasi."
    return info
  
  def __eq__(self,other):
    return self.__bosqich == other.__bosqich
  
  def __lt__(self,other):
    return self.__bosqich < other.__bosqich
  
  def __ge__(self,other):
    return self.__bosqich >= other.__bosqich
  
  def __ne__(self, other):
    return not self.__eq__(other)

  def __gt__(self, other):
      return self.__bosqich > other.__bosqich

  def __le__(self, other):
      return self.__bosqich <= other.__bosqich
  
  def __add__(self,other):
    if isinstance(other, Student):
      return self.__bosqich + other.__bosqich
    raise ValueError("Faqat student obyektlarini qo'shish mumkin")
  
  def remove(self):
    """Talaba o'chirilganda ekranga bildirishnima chiqarssh"""
    Student.__students_num -= 1
    print(f"{self.get_ism()} ismli talaba o'chirildi! Qolgan talabalar: {Student.get_num_students()} ta.")  
    
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
          
# Tekshirih uchun na'munalar
shaxs1 = Shaxs("Anvar","Oripov","AC098761",2004)
shaxs2 = Shaxs("Orif","Tolipov","AD098762",2000)
shaxs3 = Shaxs("Abror","Zoitov","AS098763",1998)
shaxs4 = Shaxs("Abram","Tolibov","AK098764",2004)
# print(shaxs1)

student1 = Student("Olim","Xakimov","AS098765",2004,1)
student2 = Student("Mashrab","Sobirov","Ad098764",2004,2)
student3 = Student("Botir","Bekov","Ad098763",2004,3)
print(student1) # Talabaning ma'lumotlarini chiqaradi
print(student1 == student2) # False
print(student2 < student1)  # FAlse
print(student3 >= student2) # True
print(student1 + student2) # 3
student1.remove()
      