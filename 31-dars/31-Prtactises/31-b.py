"""
Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq 
xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
"""
from uuid import uuid4
import datetime

class Shaxs:
  """Shaxslar haqida ma'lumot"""
  def __init__(self,ism,familiya,passport,tyil):
    self.__ism = ism
    self.__familiya = familiya
    self.__passport = passport
    self.__tyil = tyil
    self.__id = uuid4()
    
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
  __num_student = 0
  
  """Student klassi"""
  def __init__(self,ism,familiya,passport,tyil,manzil,bosqich = 1):
    super().__init__(ism,familiya,passport,tyil)
    self.__id = uuid4()
    self.__bosqich = bosqich
    self.__manzil = manzil
    Student.__num_student += 1
  
  @classmethod
  def get_num_students(cls):
    return cls.__num_student
    
  # Getter methodlar
  def get_id(self):
    """Talabaning id raqamini qaytaradi"""
    return f"ID: {self.__id}"
  
  def get_manzil(self):
    return self.__manzil 
  
  def get_bosqich(self):
    """Talabaning o'qiyotgan bosqichini qaytaradi"""
    return self.__bosqich
  
  def get_info(self):
    """Talaba xaqida ma'lumotlar"""
    info = f"Talaba: {self.get_ism()} {self.get_familiya()}, "
    info += f"Bosqich: {self.get_bosqich()}-bosqich. {self.get_id()}, "
    info += f"Manzil: {self.__manzil.get_manzil()}."
    return info
  
  def show_manzil(self):
    return str(self.__manzil.get_manzil())  # yoki self.__manzil.get_manzil()
  
  # Setter methodlar
  def change_manzil(self,yangi_manzil):
    self.__manzil = yangi_manzil
    print(f"Manzil o'zgartirildi: {yangi_manzil.get_manzil()}")
    
  def update_manzil(self, uy, kocha, tuman, viloyat):
        """Manzilni parametrlar orqali yangilash"""
        self.__manzil = Manzil(uy, kocha, tuman, viloyat)
        print("Manzil yangilandi!")
        
  def set_bosqich(self, yangi_bosqich):
        if isinstance(yangi_bosqich, int) and 1 <= yangi_bosqich <= 4:
            self.__bosqich = yangi_bosqich
        else:
            raise ValueError("Bosqich 1-4 oralig'ida bo'lishi kerak")
    
  def set_manzil(self, yangi_manzil):
      if isinstance(yangi_manzil, Manzil):
          self.__manzil = yangi_manzil
      else:
          raise ValueError("Manzil, Manzil klassidagi obyekt bo'lishi kerak")
  
  def get_info(self):
      """Talaba haqida ma'lumot"""
      info = f"Talaba: {self.get_ism()} {self.get_familiya()}, "
      info += f"Bosqich: {self.__bosqich}-bosqich. ID: {self.__id}, "
      info += f"Manzil: {self.__manzil.get_manzil()}."
      return info
    
class Manzil:
  """manzil saqlash uchu class"""
  def __init__(self,uy,kocha,tuman,viloyat):
    self.__uy = uy
    self.__kocha = kocha
    self.__tuman = tuman
    self.__viloyat = viloyat
    
  def get_uy(self):
    return self.__uy
    
  def get_manzil(self):
    """Manzilni ko'rish"""
    # Agar 'shahar' so'zi bo'lsa, o'zini yozamiz
    if 'shahar' in self.__viloyat.lower():
        hudud = self.__viloyat  # Masalan: Toshkent shahri
    else:
        hudud = f"{self.__viloyat} viloyati"  # Masalan: Andijon viloyati
        
    manzil = f"{hudud}, {self.__tuman} tumani, "
    manzil += f"{self.__kocha} ko'chasi, {self.__uy}-uy"
    return manzil
  
  # def get_manzil(self):
  #       """Formatlangan manzilni qaytarish"""
  #       hudud = self.__viloyat if 'shahar' in self.__viloyat.lower() else f"{self.__viloyat} viloyati"
  #       return f"{hudud}, {self.__tuman} tumani, {self.__kocha} ko'chasi, {self.__uy}-uy"
      
  def set_uy(self, yangi_uy):
    if isinstance(yangi_uy, int) and yangi_uy > 0:
      self.__uy = yangi_uy
    else:
      raise ValueError("Uy raqami musbat va butun son bo'lishi kerak!")
  
  def __str__(self):
        return self.get_manzil()
  
# Student classi tekshirish 
student1_manzil = Manzil(147,"Jarqo'rg'on","Chelak","Buxoro")
student1 = Student("Anvar","Qobilov","AB098123",2000,student1_manzil)

student2_manzil = Manzil(73,"Obodon","Norin","Namangan")
student2 = Student("Sobit","Obidov","Ak098435",2002,student2_manzil)

student3_manzil = Manzil(7,"Mustaqillik","Qamashi","Qashqadaryo")
student3 = Student("Asror","Kamolov","AB098123",1998,student3_manzil)

print(Student.get_num_students())
print(student2.get_info())
print(student2.show_manzil())

yangi_manzil1 = Manzil(111,"Bodomzor","Olot","Qashqadaryo")
student2.change_manzil(yangi_manzil1)
print(student2.show_manzil())
print(student2.get_info())

student1.update_manzil(30, "Yangi ariq", "Chilonzor", "Toshkent shahar")
print(student1.show_manzil())

# Shaxs klassi uchun tekshirish
# shaxs1 = Shaxs("Ali","Valiyev","AC123OB6",2005)
# print(shaxs1.get_info())

# Manzil yaratish
manzil1 = Manzil(77, "Mustaqillik", "Mirzo Ulug'bek", "Toshkent shahar")

# Talaba yaratish
talaba1 = Student("Ali", "Valiyev", "AB123456", 1999, manzil1)

# Ma'lumotlarni o'qish
print(talaba1.get_info())
print(f"Yoshi: {talaba1.get_age()}")
print(f"Manzil: {talaba1.get_manzil()}")

# Ma'lumotlarni o'zgartirish
talaba1.set_ism("Alijon")
talaba1.set_bosqich(2)
talaba1.get_manzil().set_uy(15)

print("\nO'zgartirilgan ma'lumotlar:")
print(talaba1.get_info())
