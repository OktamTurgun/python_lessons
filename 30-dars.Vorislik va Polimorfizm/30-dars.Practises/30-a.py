"""
Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. 
Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida
bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
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

class Student(Shaxs):
  """Student klassi"""
  def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
    super().__init__(ism,familiya,passport,tyil)
    self.idraqam = idraqam
    self.bosqich = 1
    self.manzil = manzil
    self.fanlar = []
    
  def get_id(self):
    """Talabaning id raqamini qaytaradi"""
    return f"ID raqami: {self.idraqam}"
  
  def get_bosqich(self):
    """Talabaning o'qiyotgan bosqichini qaytaradi"""
    return self.bosqich
  
  def get_info(self):
    """Talaba xaqida ma'lumotlar"""
    info = f"{self.ism} {self.familiya}. "
    info += f"{self.get_bosqich()}-bosqich talabasi. {self.get_id()}. "
    info += f"{self.manzil.get_manzil()}. {self.fanlar}"
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
        
    manzil = f"Manzil: {hudud}, {self.tuman} tumani, "
    manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
    return manzil
  
student1_manzil = Manzil(12,"Anxor","Yunusobod","Toshkent shahar")  
student1 = Student("Anvar","Qosimov","AB112233",2000,"ID009988",student1_manzil)
print(student1.get_info())