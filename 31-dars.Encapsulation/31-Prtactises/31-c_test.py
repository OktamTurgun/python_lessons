from exmple_c import Shaxs, Student

shaxs1 = Shaxs("Ali", "Valiyev", "AB123456", 1990)
shaxs2 = Shaxs("Vali", "Aliyev", "CD654321", 1995)

talaba1 = Student("Hasan", "Husanov", "EF987654", 2000)
talaba2 = Student("Husan", "Hasanov", "GH456789", 2001)
talaba3 = Student("Eshmat", "Toshmatov", "IJ123987", 1999)

'''Shaxs klassining metodlari uchun testlar:'''

# get_info() metodi
print(shaxs1.get_info())  # "Ali Valiyev. Passport: AB123456, 1990-yilda tug'ilgan Yosh: 34-yoshda"

# get_age() metodi
print(shaxs2.get_age())  
# "Yosh: 29" (2023-yil uchun)

# set_ism() metodi
shaxs1.set_ism("Alijon")
print(shaxs1.get_ism())  # "Alijon"

# set_passport() metodi
shaxs2.set_passport("XY876543")
print(shaxs2.get_passport())  # "XY876543"

# set_age() metodi (xato holat)
try:
    shaxs1.set_age(-5)
except ValueError as e:
    print(e)  # "Yosh musbat va butun son bo'lishi kerak!"
    
'''Student klassining metodlari uchun testlar:'''

# get_info() metodi
print(talaba1.get_info())  
# "Talaba: Hasan Husanov, Bosqich: 1-bosqich. ID: 123e4567-e89b-12d3-a456-426614174000"

# get_bosqich() metodi
print(talaba2.get_bosqich())  # 1

# set_bosqich() metodi
talaba3.set_bosqich(3)
print(talaba3.get_bosqich())  # 3

# set_bosqich() xato holat
try:
    talaba1.set_bosqich(5)
except ValueError as e:
    print(e)  # "Bosqich 1-4 oralig'ida bo'lishi kerak"
    
'''Klass metodlari uchun testlar:'''

# set_persons_num() metodi
Shaxs.set_persons_num(10)
print(Shaxs.get_num_persons())  # 10

# set_students_num() metodi
Student.set_students_num(8)
print(Student.get_num_students())  # 8

# set_persons_num() xato holat uchun misol
try:
    Shaxs.set_persons_num(-3)
except ValueError as e:
    print(e)  # "Shaxslar soni manfiy bo'lishi mumkin emas!"
    
'''Getter metodlar uchun qo'shimcha testlar:'''

# get_id() metodi
print(type(shaxs1.get_id()))  # <class 'uuid.UUID'>
print(type(talaba1.get_id()))  # <class 'str'>

# get_familiya() metodi
print(talaba2.get_familiya())  # "Hasanov"