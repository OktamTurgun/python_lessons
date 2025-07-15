# 1-BOSQICH: Faylga yozish va o‘qish (matnli fayl)

# Exercise 1: Foydalanuvchi ismini faylga yozish
# ism = input("Ismingizni kiriting: ")

# with open("ism.txt", 'w') as file:
#   file.write(ism) 
  
# # Exercise 2: Fayldan o'qish va foydalanuvchiga salom berish
# with open("ism.txt", 'r') as file:
#   ism = file.read()
# print(f"Salom, {ism}!") # Salom, Olim!

# Exercise 3: Foydalanuvchi yoshini faylga yozish va o'qish
# yosh = input("Yoshingizni kiriting: ")
# with open("yosh.txt", 'w') as file:
#     file.write(yosh)
    
# with open("yosh.txt", 'r') as file:
#     yosh = file.read()
# print(f"Siz {yosh} yoshdasiz.")  # Siz 25 yoshdasiz.

# Exercise 4: Foydalanuvchi yoshini faylga yozish va o'qish (tavsiya etilgan usul)
# yosh = input("Yoshingizni kiriting: ")
# with open("yosh.txt", 'w') as file:
#     file.write(yosh.strip())  # bo'shliqlarni olib tashlash
    
# with open("yosh.txt", 'r') as file:
#     yosh = file.read().strip()  # bo'shliqlarni olib tashlash
# print(f"Siz {yosh} yoshdasiz.")  # Siz 25 yoshdasiz.

# 2-BOSQICH: Ro‘yxatlar bilan ishlash
# Exercise 1: Bir nechta ismlarni yozish

# foydalanuvchidan 5 ta ism olib faylga yozing
with open("ismlar.txt", 'w') as file:
  for _ in range(5):
    ism = input("Guruh uchun 5 ta ism kiriting: ")
    file.write(ism + '\n')

# Exercise 2: Fayldan har bir ismni o‘qib, salomlashish
with open("ismlar.txt", 'r') as file:
  ismlar = file.readlines()
  
for ism in ismlar:
  print(f"Salom {ism.strip()} yangi guruhga Xush kelibsizlar!")
  