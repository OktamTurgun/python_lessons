"""
Quyidagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)

Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.

Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.

Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating. 

Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.
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
  
class Professor(Shaxs):
  def __init__(self,ism,familiya,passport,tyil,specialty,academic_degree):
    super().__init__(self,ism,familiya,passport,tyil)
    self.specialty = specialty
    self.academic_degree = academic_degree
    
  def get_info(self):
    info =  super().get_info()
    info += f", Mutaxasislik: {self.specialty}, Ilmiy darajasi: {self.academic_degree}."
    return info
    
class User(Shaxs):
  def __init__(self,ism,familiya,passport,tyil,username,email):
    super().__init__(ism,familiya,passport,tyil)
    self.username = username
    self.email = email
    
  def get_info(self):
    info = super().get_info()
    info += f", Username: {self.username}, Email: {self.email}."
    return info
  
  def get_age(self, yil):
    return super().get_age(yil)
  
class Admin(User):
  def __init__(self,ism,familiya,passport,tyil,username,email,privilages=None):
    super().__init__(ism,familiya,passport,tyil,username,email)
    self.privilages = privilages if privilages else []
    
  def get_info(self):
    info = super().get_info()
    info += f"Imtiyozlar: {", ".join(self.privilages) if self.privilages else "Yo'q"}"
    return info
    
  def ban_user(self,user):
    print(f"Foydalanuvchi: {user.username} bloklandi!")
    
  def unban_user(self, user):
      print(f"Foydalanuvchi: {user.username} blockdan chiqarildi!")
    
 
# Tekshirish namanalari:   
user1 = User("Ali","Valiyev","AB232345",1988,"ali1988valiyev","Example@gmail.com")
admin1 = Admin("Hasan","Husanov","AD123456",2005,"hasan123456","Example@7gmail.com",["ban", "edit", "delete"])
print(user1.get_info())
print(user1.get_age(2025))
print(admin1.get_info())
admin1.ban_user(user1) # Foydalanuvchi: ali1988valiyev bloklandi!
admin1.unban_user(user1) # Foydalanuvchi: ali1988valiyev blockdan chiqarildi!

    
class Seller(Shaxs):
  def __init__(self,ism,familiya,passport,tyil,dokon_nomi,ish_staji=0,maosh=0,tel=None):
    super().__init__(ism,familiya,passport,tyil)
    self.dokon_nomi = dokon_nomi
    self.ish_staji = ish_staji
    self.maosh = maosh
    self.tel_number = tel
    self.sotilgan_maxsulotlar = []
    self.faol = True
    
  def get_info(self):
    info =  super().get_info()
    info += f", Do'kon: {self.dokon_nomi}, Ish staji: {self.ish_staji} yil, Maoshi: {self.maosh} so'm "
    if self.tel_number:
      info += f", Tel: {self.tel_number}"
    info += f", Faol: {"Ha" if self.faol else "Yo'q"}"
    return info
    
  def get_fullname(self):
   return f"{self.ism} {self.familiya}"
  
  def add_product(self, product):
    self.sotilgan_maxsulotlar.append(product)
  
  def get_sales_count(self):
    return len(self.sotilgan_maxsulotlar)
    
  def display_sales_product(self):
    return self.sotilgan_maxsulotlar
    
  def get_ish_haqqi(self,hafta_soni):
    return self.maosh / hafta_soni
    
  def faolligini_ozgartir(self):
    self.faol = not self.faol

# Tekshirish namunalari:    
# sotuvchi1 = Seller("Aziza","Tolipova","AD112233",2004,"Safia",ish_staji=3,maosh=5000000,tel="+998901234567")
# sotuvchi1.add_product("Tort Admiral")
# sotuvchi1.add_product("Julyetta torti")
# sotuvchi1.add_product("Kiyevskiy Bantik torti")

# print(sotuvchi1.get_info())
# print("Sotilgan maxsulotlar soni:", sotuvchi1.get_sales_count(), "ta")
# print("Sotilgan maxsulotlar:", sotuvchi1.display_sales_product())
# print("Ish haqqi:", sotuvchi1.get_ish_haqqi(4), "so'm (Haftasiga)")
# sotuvchi1.faolligini_ozgartir()
# print(f"Yangi xolat: {sotuvchi1.get_fullname()} {'faol' if sotuvchi1.faol else 'Nofaol'}")

class Manzil:
  """manzil saqlash uchun class"""
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

class Client(Shaxs):
  def __init__(self,ism,familiya,passport,tyil,manzil,tel=None):
    super().__init__(ism,familiya,passport,tyil)
    self.manzil = manzil
    self.tel = tel
    self.buyurtmalar = []
  
  def get_age(self, yil):
    return super().get_age(yil)
  
  def get_info(self):
    info =  super().get_info()
    info += f", Manzil: {self.manzil.get_manzil()}"
    if self.tel:
      info += f", Tel: {self.tel}"
    info += f", Buyurtmalar soni: {len(self.buyurtmalar)} ta"
    return info
    
  def add_order(self,order):
    self.buyurtmalar.append(order)
    
  def get_orders(self):
    return self.buyurtmalar

# Tekshirish namunalari:
# client1_manzil = Manzil(27,"Azimov","Yashnobod","Toshkent shahar")
# client1 = Client("Akmal","Sobirov","AA098765",1998,client1_manzil,tel="+998909876543")
# client1.add_order("Samsung Galaxy A56")
# client1.add_order("Planshet CCIT Kids Tablet")
# client1.add_order("Notebook ASUS Vivobook S 16X M5602")
# print(client1.get_info())
# print(client1.get_age())
# print(f"Buyurtmalari: {client1.get_orders()}")
    
