from uuid import uuid4
class Avto:
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        if km>0:
            self.__km += km
        else:
            print("Mashinaning km ni kamaytirib bo'lmaydi!")
            
    def get_info(self):
        return (f"Avto: {self.make} {self.model}, Rangi: {self.rang}, "
                f"Yili: {self.yil}, Narxi: ${self.narh}, "
                f"Km: {self.get_km()}, ID: {self.get_id()}")
            
class Bus:
    __num_bus = 0
    
    def __init__(self, model, capacity, year, company, route, km=0):
        self.model = model
        self.capacity = capacity
        self.year = year
        self.company = company
        self.route = route
        self.__km = km
        self.__id = uuid4()
        Bus.__num_bus += 1
        
    @classmethod
    def get_num_bus(cls):
        return cls.__num_bus
        
    def get_km(self):
        return self.__km
        
    def get_id(self):
        return self.__id
        
    def change_route(self, new_route):
        self.route = new_route
        print(f"Avtobus {new_route} marshrutiga o'zgardi")
        
    def add_km(self, km):
        if km > 0:
            self.__km += km
        else:
            print("Avtobus km ni kamaytirib bo'lmaydi!")
            
    def get_info(self):
        return (f"Avtobus: {self.model}, Sig'imi: {self.capacity} yo'lovchi, "
                f"Yili: {self.year}, Kompaniya: {self.company}, "
                f"Marshrut: {self.route}, Km: {self.get_km()}, ID: {self.get_id()}")

class Train:
    __num_train = 0
    
    def __init__(self, name, speed, carriages, route, manufacturer):
        self.name = name
        self.speed = speed
        self.carriages = carriages
        self.route = route
        self.manufacturer = manufacturer
        self.__id = uuid4()
        Train.__num_train += 1
        
    @classmethod
    def get_num_train(cls):
        return cls.__num_train
        
    def get_id(self):
        return self.__id
        
    def add_carriage(self, number=1):
        self.carriages += number
        print(f"{number} ta vagon qo'shildi. Jami {self.carriages} vagon")
        
    def change_speed(self, new_speed):
        self.speed = new_speed
        print(f"Poyezd tezligi {new_speed} km/h ga o'zgartirildi")
        
    def get_info(self):
      return (f"Poyezd: {self.name}, Tezligi: {self.speed} km/soat, "
              f"Vagonlar soni: {self.carriages}, "
              f"Marshrut: {self.route}, Ishlab chiqaruvchi: {self.manufacturer}, "
              f"ID: {self.get_id()}")


class Student:
    __num_student = 0
    
    def __init__(self, name, age, university, course, gpa):
        self.name = name
        self.age = age
        self.university = university
        self.course = course
        self.gpa = gpa
        self.__id = uuid4()
        Student.__num_student += 1
        
    @classmethod
    def get_num_student(cls):
        return cls.__num_student
        
    def get_id(self):
        return self.__id
        
    def promote(self):
        if self.course < 4:  # assuming 4 is max course
            self.course += 1
            print(f"{self.name} {self.course}-kursga ko'tarildi")
        else:
            print(f"{self.name} bitiruvchi!")
            
    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        print(f"{self.name}ning GPA {new_gpa} ga yangilandi")
        
    def get_info(self):
      return (f"Talaba: {self.name}, Yosh: {self.age}, "
              f"Universitet: {self.university}, Kurs: {self.course}, "
              f"GPA: {self.gpa}, ID: {self.get_id()}")
    
class Airplane:
    __num_airplane = 0
    
    def __init__(self, model, airline, capacity, max_altitude, flights=0):
        self.model = model
        self.airline = airline
        self.capacity = capacity
        self.max_altitude = max_altitude
        self.__flights = flights
        self.__id = uuid4()
        Airplane.__num_airplane += 1
        
    @classmethod
    def get_num_airplane(cls):
        return cls.__num_airplane
        
    def get_id(self):
        return self.__id
        
    def get_flights(self):
        return self.__flights
        
    def add_flight(self):
        self.__flights += 1
        print(f"Uchish soni yangilandi. Jami {self.__flights} marta uchgan")
        
    def change_airline(self, new_airline):
        self.airline = new_airline
        print(f"Samolyot {new_airline} aviakompaniyasiga o'tkazildi")
        
    def get_info(self):
      return (f"samolyot: {self.model}, Aviacompany: {self.airline}, "
              f"Sig'imi: {self.capacity} yo'lovchi, "
              f"Max balandlik: {self.max_altitude}, "
              f"Uchishlar soni: {self.get_flights()}, ID: {self.get_id()}.")
      
    def get_info(self):
        return (f"Samolyot: {self.model}, Aviakompaniya: {self.airline}, "
                f"Sig'imi: {self.capacity} yo'lovchi, "
                f"Maximal balandlik: {self.max_altitude} m, "
                f"Uchishlar soni: {self.get_flights()}, ID: {self.get_id()}")

