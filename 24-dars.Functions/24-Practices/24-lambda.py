"""
Foydalanuvchidan sonlar ro'yxatini qabul qilib, ularning kubini hisoblovchi dastur.
"""

# Exercise: 1
# son = input("Sonlar ro'yxatini kiriting (vergul bilan ajratilgan): ")
# sonlar = list(map(float, son.split(",")))  # Foydalanuvchidan sonlar ro'yxatini olish
# kub_sonlar = list(map(lambda x: x**3, sonlar))  # Har bir sonning kubini hisoblash
# print(
#     "Sonlar ro'yxati:", sonlar
# )  # Foydalanuvchidan olingan sonlar ro'yxatini chiqarish
# print("Sonlarning kubi:", kub_sonlar)  # Natijani chiqarish

# Exercise: 2
f1 = lambda x: x * 10  # 10 ga ko'paytiruvchi lambda funksiyasi
print(f1(10))  #

f2 = lambda x, y: x * y  # Ikkita sonni ko'paytiruvchi lambda funksiyasi
print(f2(5, 4))  # Natija: 20

f3 = lambda x, y, z: x + y + z  # Uchta sonni yig'indisini hisoblovchi lambda funksiyasi
result = f3(10, 20, 30)
print(result)  # Natija: 60

f4 = lambda x: x**2  # Sonni kvadratga oshiruvchi lambda funksiyasi
son_kvadrati = f4(7)  # Natija: 49
