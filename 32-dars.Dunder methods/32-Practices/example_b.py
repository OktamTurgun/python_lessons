"""
Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga
yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(),
__getitem__, __setitem__, __len__ kabi metodlarni qo'shing.

Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing

Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing
(bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)

Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki 
fizika(talaba1)). Bu metodlarni o'zingiz istagandek talqin qiling.
"""
from uuid import uuid4
import datetime

class Shaxs:
  __persons_num = 0
  
  """Shaxslar haqida ma'lumot"""
  def __init__(self,ism,familiya,tyil):
    self.__ism = ism
    self.__familiya = familiya
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
    info += f"{self.__tyil}-yilda tug'ilgan, {self.get_age()}-yoshda, "
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
  def __init__(self,ism,familiya,tyil,bosqich = 1):
    super().__init__(ism,familiya,tyil)
    self.__id = uuid4()
    self.__bosqich = bosqich
    Student.__students_num += 1
    
  # Dunder methods
  def __repr__(self):
    """Talaba haqida ma'lumotlar"""
    info = f"Talaba: {self.get_ism()} {self.get_familiya()} "
    info += f"\n{self.get_age()}-yoshda, "
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
          
# Fan klassi         
class Fan: 
    __fanlar_soni = 0
    __fanlar_royxati = []
    __students_num = 0
    __students_list = []

    def __init__(self, nomi):
        self.nomi = nomi
        self.students = []
        Fan.__fanlar_soni += 1
        Fan.__fanlar_royxati.append(self)
    
    def remove_fan(self):
        """Fanni ro‘yxatdan chiqarish"""
        if self in Fan.__fanlar_royxati:
            Fan.__fanlar_royxati.remove(self)
            Fan.__fanlar_soni -= 1
            print(f"{self.nomi} fani ro'yxatdan chiqarildi.")
        else:
            print(f"{self.nomi} fani allaqachon ro'yxatdan chiqarilgan.")

    @classmethod
    def get_num_fanlar(cls):
        return f"Hozircha {cls.__fanlar_soni} ta fan ro'yxatga olingan."

    @classmethod
    def get_fanlar_royxati(cls):
        return [fan.nomi for fan in cls.__fanlar_royxati]
      
    @classmethod
    def get_students_num(cls):
      return f"Xozirda {cls.__students_num} ta talaba ro'yxatga olingan."
      
    @classmethod
    def get_students_list(cls):
      # return [s.get_info() for s in cls.__students_list]
      return [f"{s.get_info()}" for s in cls.__students_list]

    def add_student(self, student):
      if isinstance(student, Student):
        self.students.append(student)
        Fan.__students_num += 1
        Fan.__students_list.append(student)
      else:
        raise ValueError("Faqat Student obyektini qo'shish mumkin.")
      
    def add_students(self,*new_students):
      for student in new_students:
          if isinstance(student,Student):
              self.students.append(student)
              Fan.__students_num += 1
              Fan.__students_list.append(student)
          else:
              raise ValueError("Faqat student obyektini kiriting!")
    
    def __getitem__(self, index):
      return self.students[index]

    def __setitem__(self, index, value):
      if isinstance(value, Student):
        self.students[index] = value
      else:
        raise ValueError("Faqat Student obyektini qo'yish mumkin.")

    def __len__(self):
      return len(self.students)

    def __contains__(self, student):
      return student in self.students

    def __repr__(self):
      info = f"Fan: {self.nomi}\n"
      info += "Talabalar:\n"
      for student in self.students:
        info += f"  {student.get_info()}\n"
      return info.strip()

    def __add__(self, student):
      self.add_student(student)
      return self

    def __sub__(self, student):
      # student obyektini yoki id raqami orqali olib tashlash
      if isinstance(student, Student):
        if student in self.students:
          self.students.remove(student)
      elif isinstance(student, str):
        self.students = [s for s in self.students if s.get_id() != student]
      return self

    def __call__(self, student=None):
      if student is None:
        print(self)
      else:
        self.add_student(student)
        

# Misollar bilan sinab ko‘rish 
matematika = Fan("Oliy matematika")
kimyo = Fan("Kimyo")
fizika = Fan("Fizika")
tarix = Fan("Tarix")
programming = Fan("Sun’iy intellekt (AI)")

student1 = Student("Anvar","Olimov",2000,1)
student2 = Student("Abror","Bitirov",2001,2)
student3 = Student("Botir","Salimov",2002,2)
student4 = Student("Xoshim","Karimov",1998,4)
student5 = Student("Xurshid","Xoliqov",1995,1)
student6 = Student("Xolid","Ziyatov",1997,2)

# studentlarni fanlarga qo'shish
matematika.add_student(student1)
matematika.add_student(student2)
matematika.add_student(student3)
print(len(matematika))             # 3 ta talaba

print(student1 in matematika)      # True
print(student4 in matematika)      # False

kimyo.add_student(student3)
kimyo.add_student(student5)
# print(len(kimyo))

fizika.add_student(student4)
fizika.add_student(student2)
fizika.add_student(student1)
print(len(fizika))

programming.add_student(student1)
programming.add_student(student4)
programming.add_student(student6)
print(len(programming))

# Fanlar soni va ro'yxatini tekshirish
print(Fan.get_num_fanlar())        # Hozircha 5 ta fan ro'yxatga olingan.
print(Fan.get_fanlar_royxati())    # ['Oliy matematika', 'Kimyo', 'Fizika', 'Tarix', 'Sun’iy intellekt (AI)']

# Studentlar soni va ro'yxatini tekshirish
print(Fan.get_students_num())
print(Fan.get_students_list())

# + orqali qo‘shish, - orqali olib tashlash
matematika + student4              # student4 ni ham qo‘shadi
print(len(matematika))             # 4

matematika - student2              # student2 ni olib tashlaydi
print(len(matematika))             # 3

matematika - student3.get_id()     # ID orqali olib tashlash
kimyo - "d96a545d-edc9-45e7-bbcf-63c7a7cc243e"
print(len(kimyo))
kimyo()

# Indeks orqali kirish va o‘zgartirish
print(matematika[0])               # 0-indexdagi talabani chiqaradi

matematika[1] = student4           # 1-indexdagi talabani yangilaydi
print(matematika[1])

# __call__ orqali foydalanish
matematika()                       # print(matematika) bilan bir xil
matematika(student2)               # student2 ni yana qo‘shadi

# Fan obyektini o‘chirish
# fizika = Fan("Fizika")
# print(Fan.get_fanlar_royxati())  # ['Fizika']

# fizika.remove_fan()              # Fizika fani ro'yxatdan chiqarildi.
# print(Fan.get_fanlar_royxati())  # ['Oliy matematika', 'Kimyo', 'Fizika', 'Tarix', 'Sun’iy intellekt (AI)']

# kimyo(student5)
# kimyo()
# fizika()

'''
Yana qoshish mumkin bolgan xolatlar
Talaba qo'shishda bir xil talaba qo'shilmasligini tekshirish

Olib tashlashda bir nechta mos keluvchi talabalar bo'lsa, ular haqida ogohlantirish

Fan nomini o'zgartirish metodini qo'shish

Talabalar ro'yxatini filterlash metodlari (masalan, bosqich bo'yicha)
'''
