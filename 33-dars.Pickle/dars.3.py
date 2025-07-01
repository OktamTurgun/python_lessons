"""
Created on Thu Fri 20 09:53:14 2025

33-dars. Fayllar bilan ishlash. Pickle

@author: uktam
"""
filename = 'data/students.txt'
# with open(filename) as file:
#   for line in file:
#     print(line)

with open(filename) as file:
    talabalar = file.readlines()  # Fayldagi barcha qatorlarni o'qib olamiz

print(talabalar)  # O'qilgan talabalar ro'yxatini chiqaramiz

talabalar = [talaba.strip() for talaba in talabalar]
print(talabalar)


# 1. Faylni o'qish
with open(filename, 'r') as file:
    talabalar = file.readlines()  # Har bir qatorni ro'yxatga olamiz

# 2. Ro'yxatni ko'rish (asl holatda)
print("Asl ro'yxat:", talabalar)
# Chiqish: ['alijon valiyev\n', 'hasan olimov\n', 'rahima muminova\n', 'hamida oqilova']

# 3. Har bir satrdan \n ni olib tashlash
talabalar = [talaba.strip() for talaba in talabalar]
print("Tozalangan ro'yxat:", talabalar)
# Chiqish: ['alijon valiyev', 'hasan olimov', 'rahima muminova', 'hamida oqilova']

# 4. Har bir talabani alohida chiqarish
print("\nTalabalar ro'yxati:")
for talaba in talabalar:
    print(talaba)
