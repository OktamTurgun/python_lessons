"""
Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching
"""
filename = 'dars_xulosasi.txt'

with open(filename, encoding='utf-8') as file:
    matn = file.readlines()  # Fayldagi barcha qatorlarni o'qib olamiz

# print(matn)  # O'qilgan talabalar ro'yxatini chiqaramiz

# xulosa = [text.strip() for text in matn]
# print(xulosa)

# print("\n" + "=" * 50)
# print(''.join(matn).strip())


# 1. Faylni o'qish
# with open(filename, 'r') as file:
#     matn = file.readlines()  # Har bir qatorni ro'yxatga olamiz

# 2. Ro'yxatni ko'rish (asl holatda)
# print("Asl matn:", matn)

# # 3. Har bir satrdan \n ni olib tashlash
# matn = [x.strip() for x in matn]
# print("Tozalangan matn:", matn)

# # 4. Har bir qatorni alohida chiqarish
print("\nDars xulosasi:")
for x in matn:
    print(x.strip())
