"""
Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

Avtosalonga yangi avtomobillar qo'shish uchun metod yozing

Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring

dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)
"""
class Avtosalon:
    """Avtomobil sotuvchi salonni ifodalovchi klass"""
    
    def __init__(self, nomi, manzili):
        """Avtosalon konstruktori"""
        self.nomi = nomi
        self.manzili = manzili
        self.sotuvdagi_avtomobillar = []
    
    def avto_qoshish(self, avto):
        """Salonga yangi avtomobil qo'shish metodi"""
        self.sotuvdagi_avtomobillar.append(avto)
        print(f"{avto} avtomobili sotuvga qo'shildi.")
    
    def avtomobillar_haqida(self):
        """Salondagi avtomobillar haqida ma'lumot qaytaruvchi metod"""
        if not self.sotuvdagi_avtomobillar:
            return "Hozircha sotuvda avtomobillar mavjud emas."
        
        info = f"{self.nomi} avtosalonidagi avtomobillar:\n"
        for idx, avto in enumerate(self.sotuvdagi_avtomobillar, 1):
            info += f"{idx}. {avto}\n"
        return info
    
    def __str__(self):
        """Avtosalon haqida asosiy ma'lumot"""
        return f"{self.nomi} avtosalon, manzili: {self.manzili}"
      
def show_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]

# Klassni tekshirish
if __name__ == "__main__":
    # Yangi avtosalon yaratamiz
    salon = Avtosalon("Yulduz Avto", "Toshkent shahri, Yunusobod tumani")
    print(salon)
    
    # Yangi avtomobillar qo'shamiz
    salon.avto_qoshish("Malibu 2.5 LTZ")
    salon.avto_qoshish("Gentra 1.5")
    salon.avto_qoshish("Tracker")
    
    # Avtomobillar haqida ma'lumot olamiz
    print(salon.avtomobillar_haqida())
    
    # dir() va __dict__ yordamida tekshirish
    print("\nAvtosalon klassining metodlari va xususiyatlari:")
    print(dir(Avtosalon))
    
    print("\nAvtosalon obyektining xususiyatlari:")
    print(salon.__dict__)
    
    # Pythondagi boshqa klasslarni tekshirish
    print("\nstr klassining metodlari:")
    print(dir(str))
    
    print("\nint klassining metodlari:")
    print(dir(int))
    
print(show_methods(Avtosalon))
    
