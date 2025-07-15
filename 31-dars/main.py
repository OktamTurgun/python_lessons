# import avto

# avto1 = avto.Avto("Mercedes_Benz","AMG EQS Sedan","Polar White",2025,147550)
# avto2 = avto.Avto("Porsche","718 Cayman","Black",2025,74800)
# avto3 = avto.Avto("Ferrari","Ferrari Daytona SP3","Red",2025,2223935)
# print(avto.Avto.get_num_avto())

from avto import Avto, Bus, Train, Student,  Airplane

# Avto class uchun tekshirish namunalari
avto1 = Avto("Mercedes_Benz","AMG EQS Sedan","Polar White",2025,147550)
avto2 = Avto("Porsche","718 Cayman","Black",2025,74800)
avto3 = Avto("Ferrari","Ferrari Daytona SP3","Red",2025,2223935)
print(avto2.get_info())  # Avto: Porsche 718 Cayman, Rangi: Black, Yili: 2025, Narxi: $74800, Km: 0, ID: c972ed86-8e6a-45a5-b5c3-618187965b34
print(Avto.get_num_avto())

# Bus class uchun tekshirish
bus1 = Bus("Mercedes Tourismo", 50, 2023, "Qatarbus", "Toshkent-Samarqand", 25000)
print(bus1.get_km())  # 25000
print(bus1.get_id())  # Masalan: 5a3e8b2c-1f4d-4e76-a2c3-9b1d5e7f8a2c
bus1.add_km(500)
print(bus1.get_km())  # 25500
bus1.change_route("Toshkent-Buxoro")
print(bus1.route)  # Toshkent-Buxoro

bus2 = Bus("MAN Lion's Coach", 60, 2024, "Uzbus", "Toshkent-Andijon")
bus3 = Bus("Yutong", 55, 2022, "Safarbus", "Toshkent-Nukus")
print(Bus.get_num_bus())  # 3
print(bus3.get_info()) # Avtobus: Yutong, Sig'imi: 55 yo'lovchi, Yili: 2022, Kompaniya: Safarbus, Marshrut: Toshkent-Nukus, Km: 0, ID: 58ab5770-1896-49ee-87ab-d8f015d5aaa3

# Train class teksirish
train1 = Train("Afrosiyob", 250, 7, "Toshkent-Xiva", "Talgo")
print(train1.carriages)  # 7
print(train1.get_id())  # Masalan: 8b2e1d4f-3c6a-49e7-b5f0-6d1e2c3a4b5d
train1.add_carriage(2)
print(train1.carriages)  # 9
train1.change_speed(220)
print(train1.speed)  # 220

train2 = Train("Sharq", 140, 12, "Toshkent-Qo'qon", "Hyundai Rotem")
train3 = Train("Registon", 160, 10, "Samarqand-Termiz", "CNR")
print(Train.get_num_train())  # 3

# Student class teksirish
student1 = Student("Ali", 20, "Harvard", 2, 3.8)
print(student1.gpa)  # 3.8
print(student1.get_id())  # Masalan: 2c4e6d8a-1b3f-49e7-85c0-7d2e1f3a4b5c
student1.update_gpa(4.0)
print(student1.gpa)  # 4.0
student1.promote()
print(student1.course)  # 3

student2 = Student("Vali", 21, "MIT", 3, 3.5)
student3 = Student("Hasan", 19, "Stanford", 1, 3.9)
print(Student.get_num_student())  # 3
print(student1.get_info()) # Talaba: Ali, Yosh: 20, Universitet: Harvard, Kurs: 3, GPA: 4.0, ID: 65cda400-7ea9-4af7-be36-c1b9c2f4bea4

# Airplane class teksirish
airplane1 = Airplane("Boeing 787", "Uzbekistan Airways", 300, 13100, 45)
print(airplane1.get_flights())  # 45
print(airplane1.get_id())  # Masalan: 1a3e5c7d-2b4f-68e9-71c3-9d2e4f6a8b0c
airplane1.add_flight()
print(airplane1.get_flights())  # 46
airplane1.change_airline("Qatar Airways")
print(airplane1.airline)  # Qatar Airways

airplane2 = Airplane("Airbus A320", "Turkish Airlines", 180, 12000)
airplane3 = Airplane("Boeing 777", "Emirates", 350, 14000, 120)
print(Airplane.get_num_airplane())  # 3
print(airplane3.get_info()) # Samolyot: Boeing 777, Aviakompaniya: Emirates, Sig'imi: 350 yo'lovchi, Maximal balandlik: 14000 m, Uchishlar soni: 120, ID: c8997697-5bbe-499c-ab72-232a87b1a81f