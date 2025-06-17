"""
Created on Sub Jun 17 09:18:14 2025

32-dars.  OOP. Dunder methods

@author: uktam
"""
'''
Python'da "dunder methods" (ya'ni "double underscore methods", masalan __init__, __str__, __len__) 
— bu maxsus metodlar bo‘lib, ular Pythonda obyektlar qanday ishlashini boshqaradi. 
Quyidagi jadvalda eng ko‘p ishlatiladigan dunder methodlar va ularning vazifasi,
misoli hamda natijasi berilgan:

## Python Dunder (Magic) Methods – Jadval Ko‘rinishida

Method nomi	     Maqsadi (Qachon chaqiriladi)	                    Misol kodi	                                                  Natijasi yoki Izohi
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__init__	       Obyekt yaratilganda chaqiriladi	                def __init__(self, ism):                                      obj = Talaba("Ali") → obj.ism == "Ali"
                                                                    self.ism = ism	                      
__str__	         print(obj) yoki str(obj) qilinganda	            def __str__(self):                                            print(obj) → Talaba: Ali
                                                                    return f"Talaba: {self.ism}"	              
__repr__	       repr(obj) chaqirilganda (developerlarga ko‘proq)	def __repr__(self):                                           repr(obj) → Talaba('Ali')
                                                                    return f"Talaba('{self.ism}')"	          
__len__	         len(obj) chaqirilganda	                          def __len__(self):                                            len(obj) → kurslar soni
                                                                    return len(self.kurslar)	                  
__eq__	         obj1 == obj2 qilinganda	                        def __eq__(self, other):                                      obj1 == obj2 → True/False
                                                                    return self.ism == other.ism	        
__add__	         obj1 + obj2 qilinganda	                          def __add__(self, other):                                     obj1 + obj2 → 45 (yoshlar yig‘indisi)
                                                                    return self.yosh + other.yosh	      
__getitem__	     obj[key] chaqirilganda	                          def __getitem__(self, key):                                   obj[0] → "Python"
                                                                    return self.kurslar[key]	        
__setitem__	     obj[key] = val qilinganda	                      def __setitem__(self, key, val):                              obj[1] = "JS"
                                                                    self.kurslar[key] = val	    
__delitem__	     del obj[key] qilinganda	                        def __delitem__(self, key):                                   del obj[2] → 3-kurs o‘chadi
                                                                    del self.kurslar[key]	            
__contains__	   val in obj qilinganda	                          def __contains__(self, item):                                 "Python" in obj → True/False
                                                                    return item in self.kurslar	    
'''
# Exercise: 1 Talaba Klassida Dunder Methodlar
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.kurslar = ["Python", "Django", "SQL"]

    def __str__(self):
        return f"Talaba: {self.ism}, {self.yosh} yoshda"

    def __len__(self):
        return len(self.kurslar)

    def __getitem__(self, key):
        return self.kurslar[key]

    def __contains__(self, item):
        return item in self.kurslar

    def __add__(self, other):
        return self.yosh + other.yosh
      
# Sinov:
talaba1 = Talaba("Ali", 20)
talaba2 = Talaba("Vali", 22)

# print(talaba1)             # Talaba: Ali, 20 yoshda
# print(len(talaba1))        # 3
# print(talaba1[0])          # Python
# print("Django" in talaba1) # True
# print(talaba1 + talaba2)   # 42

# Exercise: 2 

from uuid import uuid4
class Avto:
  __num_avto = 0
  
  def __init__(self,make,model,rang,yil,narh):
    """Avtomobilning xususiyatlari"""
    self.make = make
    self.model = model
    self.rang = rang
    self.yil = yil
    self.narh = narh
    self.__id = uuid4()
    Avto.__num_avto += 1
    
  # def __str__(self):
  #   formatted_narh = "{:,}".format(self.narh).replace(",", ".")
  #   return f"Company: {self.make}, Model: {self.model}, Narh: {formatted_narh}$"

  # Tavsiya qilingan method
  def __repr__(self):
      return f"Company: {self.make}, Model: {self.model}, Yil: {self.yil}, ID: {self.__id.hex}"
    
  def __eq__(self,other):
    # return self.narh == other.narh
    return self.__id == other.__id
  
  def __lt__(self,other):
    return self.narh < other.narh
  
  def __len__(self):
    return len(self.make)
  
avto1 = Avto("Mercedes_Benz","AMG EQS Sedan","Polar White",2025,147550)
# print(avto1) # Company: Mercedes_Benz, Model: AMG EQS Sedan, Narh: 147.550$

avto2 = Avto("BMW", "M5 Competition", "Sapphire Black", 2024, 125300)
avto3 = Avto("Audi", "RS7 Sportback", "Nardo Gray", 2023, 118900)
avto4 = Avto("Tesla", "Model S Plaid", "Red Multi-Coat", 2024, 109990)
avto5 = Avto("Porsche", "Taycan Turbo S", "Ice Blue", 2025, 185000)
avto6 = Avto("Lexus", "LC 500", "Infrared", 2024, 96500)

# print(avto5)
# print(avto4)
# print(avto3)

'''
Taqqoslash dunder metodlari

Dunder Metod   |        Maqsadi	                      | Ishlatilishi
-----------------------------------------------------------------
__eq__	       |        Tenglikni tekshiradi	      | a == b
__ne__	       |        Teng emaslikni tekshiradi	  | a != b
__lt__	       |        Kichiklikni tekshiradi	      | a < b
__le__	       |        Kichik yoki teng	          | a <= b
__gt__	       |        Kattalikni tekshiradi	      | a > b
__ge__	       |        Katta yoki teng	              | a >= b

'''
# print(avto1 == avto2) # False
# print(avto3 < avto1) # True
# print(avto1 > avto5) # False
# print(len(avto5)) # 

# eXERCISE: 3 __len__ method
class Cart:
    def __init__(self, products):
        self.products = products

    def __len__(self):
        return len(self.products)

cart1 = Cart(["non", "sut", "yog'", "go'sht", "olma"])
# print(f"Savatda {len(cart1)} ta maxsulot bor.")

# Exercise: 4 
class Avtosalon:
  """Avtosalon klassi"""
  def __init__(self,name):
    self.name = name
    self.avtolar = []
    
  def __repr__(self):
    return f"{self.name} avtosaloni"

  def __getitem__(self,index):
      return self.avtolar[index]
    
  def __setitem__(self,index,qiymat):
    self.avtolar[index] = qiymat
    
  def __call__(self,*value):
    if value:
      for avto in value:
          self.add_avto(avto)
    else:  
      return [avto for avto in self.avtolar]
  
  def __add__(self,value):
      if isinstance(value,Avtosalon):
          new_salon = Avtosalon(f"{self.name} {value.name}")
          new_salon.avtolar = self.avtolar + value.avtolar
          return new_salon
      elif isinstance(value,Avto):
          self.add_avto(value)
    
  def __len__(self):
    return len(self.avtolar)

  def add_avto(self,*qiymat):
      for avto in qiymat:
          if isinstance(avto,Avto):
              self.avtolar.append(avto)
          else:
              raise ValueError("Faqat avto kiriting!")
                  
avto1 = Avto("Mercedes_Benz","AMG EQS Sedan","Polar White",2025,147550)
avto2 = Avto("BMW", "M5 Competition", "Sapphire Black", 2024, 125300)
avto3 = Avto("Audi", "RS7 Sportback", "Nardo Gray", 2023, 118900)

salon1 = Avtosalon("ModernAvto")
salon2 = Avtosalon("Avto Lider")
salon1.add_avto(avto1,avto2,avto3)
# print(salon1.avtolar[1])
# print(salon1[0])
# print(salon1[2])

# 1-indexdagi avtoni o'zgartiramiz
salon1[1] = Avto("Porsche", "Taycan Turbo S", "Ice Blue", 2025, 185000)
# print(salon1.avtolar)

# salon1 ga yangi avto qo'shamiz
salon1.add_avto(avto6)
salon2(avto4,avto5,avto6)
# print(salon1.avtolar)

# Salondagi avtolar sonini chiqaramiz
print(f"Hozircha salonda {len(salon1)} ta avtomobil mavjud")


# Exercise 5. __getitem__ , __setitem__ methods
class Kitob:
    """Kitob klassi"""
    def __init__(self, nomi, muallifi, yili):
        self.nomi = nomi
        self.muallifi = muallifi
        self.yili = yili
    
    def __repr__(self):
        return f"«{self.nomi}» ({self.muallifi}, {self.yili})"

class Kutubxona:
    """Kutubxona klassi"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.kitoblar = []
    
    def __repr__(self):
        return f"{self.nomi} kutubxonasi"
    
    def __getitem__(self, index):
        # Indeks yoki slice (kesish) qabul qiladi
        if isinstance(index, slice):  # Agar kesish bo'lsa (masalan, [1:3])
            return self.kitoblar[index]
        else:  # Agar oddiy indeks bo'lsa (masalan, [0])
            return self.kitoblar[index]
          
    def __setitem__(self,index,yangi_kitob):
        # Yangi kitobni tekshiramiz
        if not isinstance(yangi_kitob,Kitob):
            raise ValueError("Faqat Kitob obyekti qo'shishingiz mumkin!")
        # Agar indeks mavjud bo'lsa, o'zgartiramiz
        if 0 <= index < len(self.kitoblar):
            self.kitoblar[index] = yangi_kitob
        # Agar indeks listdan tashqarida bo'lsa, yangi element qo'shamiz
        elif index == len(self.kitoblar):
            self.kitoblar.append(yangi_kitob)
        else:
            raise IndexError("Noto'g'ri indeks!")
            
    def __len__(self):
        return len(self.kitoblar)
    
    def qoshish(self, *kitoblar):
        for kitob in kitoblar:
            if isinstance(kitob, Kitob):
                self.kitoblar.append(kitob)
            else:
                raise ValueError("Faqat Kitob obyekti qo'shishingiz mumkin!")

# Kitoblar yaratamiz
kitob1 = Kitob("Otgan kunlar", "Abdulla Qodiriy", 1926)
kitob2 = Kitob("Mehrobdan chayon", "Abdulla Qahhor", 1952)
kitob3 = Kitob("Dunyoning ishlari", "Oʻtkir Hoshimov", 1990)
kitob4 = Kitob("Shaytanat", "Tohir Malik", 2006)
kitob5 = Kitob("Sariq devni minib", "Xudoyberdi To'xtaboyev", 1978)
kitob6 = Kitob("Shum bola", "G'ofur Gulom", 1936)

# Kutubxona yaratib, kitoblarni qo'shamiz
kutubxona = Kutubxona("Milliy kutubxona")
kutubxona.qoshish(kitob1, kitob2, kitob3, kitob4, kitob5)

# __getitem__ orqali indekslash va kesish
# print(kutubxona[0])          # 1-kitob: «Otgan kunlar» (Abdulla Qodiriy, 1926)
# print(kutubxona[1:3])        # 2 va 3-kitoblar: [«Mehrobdan chayon» (...), «Dunyoning ishlari» (...)]
# print(kutubxona[-1])         # Oxirgi kitob: «Sariq devni minib» (...)
# print(kutubxona[::2])        # Har ikkinchi kitob: [1, 3, 5-kitoblar]

# print("Boshidagi kutubxona:")
# print(kutubxona.kitoblar)  # [«Otgan kunlar» (...), «Mehrobdan chayon» (...), «Dunyoning ishlari» (...)]

# 1-indeksdagi kitobni o'zgartiramiz
kutubxona[1] = Kitob("Kecha va kunduz", "Abdulla Qodiriy", 1936)
# print("\nO'zgartirilgan kutubxona:")
# print(kutubxona.kitoblar)  # [«Otgan kunlar» (...), «Kecha va kunduz» (...), «Dunyoning ishlari» (...)]

# Yangi kitob qo'shamiz (agar indeks = len(kitoblar) bo'lsa, append qiladi)
kutubxona[3] = kitob6
# print("\nYangi kitob qo'shilgan kutubxona:")
# print(kutubxona.kitoblar) 

# Kutubxonada nechta kitob borligini chiqaramiz
print(f"Hozirda kutubxonamizda {len(kutubxona)} ta kitob mavjud.") 

