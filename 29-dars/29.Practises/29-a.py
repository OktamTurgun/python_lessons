"""
Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan
bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. 
Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
"""
class Avto:
  def __init__(self,company,model,rang,korobka,narh,yil):
    self.company = company
    self.model = model
    self.rang = rang
    self.korobka = korobka
    self.narh = narh
    self.yil = yil
    self.km = 0
    
  def __str__(self):
    return self.get_info()
  
  def made_by(self):
    return self.company
  
  def get_info(self):
    return f"{self.company} {self.model}, {self.rang}, {self.korobka}, Yili: {self.yil}, Price: {self.narh}$"
  
  def update_info(self,new_value):
    self.get_info(new_value)
    
  
avto1 = Avto("Tesla","Cybertruck","qora","avtomat", 57000, 2024)
print(avto1.get_info())

# Exercises 2
class Avto:
    def __init__(self, company, model, rang, korobka, narh, yil, km=0):
        self.company = company
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yil = yil
        self.km = km
        
    def __str__(self):
        return self.get_info()
        
    def get_info(self):
        """Avtomobil haqida to'liq ma'lumot qaytaradi"""
        info = (f"Kompaniya: {self.company}\n"
                f"Model: {self.model}\n"
                f"Rangi: {self.rang}\n"
                f"Korobka: {self.korobka}\n"
                f"Narxi: {self.narh}$\n"
                f"Ishlab chiqarilgan yili: {self.yil}\n"
                f"Yurgan kilometri: {self.km} km")
        return info
    
    def update_km(self, new_km):
        """Avtomobilning kilometrajini yangilaydi"""
        if new_km >= self.km:
            self.km = new_km
        else:
            print("Kilometrni kamaytirib bo'lmaydi!")
    
    def set_narh(self, new_price):
        """Avtomobil narxini yangilaydi"""
        self.narh = new_price
    
    def set_color(self, new_color):
        """Avtomobil rangini yangilaydi"""
        self.rang = new_color
    
    def set_korobka(self, new_korobka):
        """Avtomobil korobkasini yangilaydi"""
        self.korobka = new_korobka


# Test qilish
avto1 = Avto("Tesla", "Cybertruck", "qora", "avtomat", 57000, 2024)
print(avto1.get_info())

# Kilometrni yangilash
avto1.update_km(1500)
print("\nKilometr yangilangandan keyin:")
print(avto1)

# Narxni yangilash
avto1.set_narh(60000)
print("\nNarx yangilangandan keyin:")
print(avto1.get_info())

# Rangni yangilash
avto1.set_color("Kulrang")
print("\nRang yangilangandan keyin:")
print(avto1)
'''
Har bir atributni yangilash uchun alohida metodlar (set_narh, set_color, set_korobka)

__str__ metodi qo'shildi, shunchaki print(avto1) deb yozsangiz ham ma'lumot chiqadi

update_km metodida tekshiruv qo'shildi - kilometrni kamaytirib bo'lmasligi uchun

Docstring qo'shildi - har bir metod nima qilishini tushuntirib beradi

km parametriga standart qiymat (0) berildi
'''