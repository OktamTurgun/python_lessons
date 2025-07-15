"""
Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.

Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.

Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin
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

class Subject:
  """Fan klassi - fan nomini saqlaydi"""
  def __init__(self,nomi):
    self.nomi = nomi
  def __repr__(self):
    return self.nomi

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
    info += f"{self.manzil.get_manzil()}. Fanlar: {self.fanlar}"
    return info
  
  def fanga_yozil(self,fan):
    if fan not in self.fanlar:
      self.fanlar.append(fan)
    else:
      print(f"Siz {fan.nomi} faniga yozilgansiz!")
      
  def remove_fan(self,fan):
    if fan in self.fanlar:
      self.fanlar.remove(fan)
    else:
      print(f"Siz bu {fan.nomi} faniga yozilmagansiz!")
  
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
        hudud = f"{self.viloyat} viloyati" 
        
    manzil = f"Manzil: {hudud}, {self.tuman} tumani, "
    manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
    return manzil
  
# Manzil yaratamiz
manzil1 = Manzil(12, "Bog'bon", "Olmazor", "Toshkent shahri")

# Talaba yaratamiz
student1 = Student("Ali", "Valiyev", "AB1234567", 2001, "ST001", manzil1)

# Fanlar yaratamiz
matematika = Subject("Matematika")
fizika = Subject("Fizika")
biologiya = Subject("Biologiya")

# Fanga yozamiz
student1.fanga_yozil(matematika)
student1.fanga_yozil(fizika)

# Fanlarni ko'rish
print(student1.get_info())  # Matematika va Fizika fanlari bor bo'lishi kerak

# Biologiya fanini o‘chirishga harakat qilamiz (yo‘q fan)
student1.remove_fan(biologiya)  # => Siz bu fanga yozilmagansiz.

# Fizika fanini o‘chiramiz
student1.remove_fan(fizika)
student1.fanga_yozil(matematika)

# Yana ma'lumotlarni ko‘ramiz
print(student1.get_info())  # Endi faqat Matematika qoladi  
  

    
