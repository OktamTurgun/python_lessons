"""
Xatolar bilan ishlash
"""
# Xato yozilgan code: Code xato yozilmagan, ishlaydi. Biz uni takomillashtiramiz
son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n): # # Agar son n ga qoldiqsiz bo'linsa (ya'ni son%n == 0 bo'lsa)
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# Takomillashtirilgan code:
son = int(input("Istalgan butun son kiriting: "))
son_abs = abs(son) # Manfiy sonlarni xam musbat ko'rinishida tekshiramiz va yangi o'zgaruvchiga yuklaymiz
bor = False # Hozircha bo'linuvchi topilmadi

for n in range(2,11):
    if son_abs % 2 == 0: # # Agar son n ga qoldiqsiz bo'linsa (ya'ni son%n == 0 bo'lsa)
        print(f"{son_abs} soni {n} ga qoldiqsiz bo'linadi")
        bor = True # Kamida 1 ta bo'linuvchi topildi

if not bor:  # Agar son 2-10 oraliqidagi hech bir songa bo'linmasa (bor=False bo'lsa)
    print(f"{son} soni 2 dan 10 gacha bo'lgan sonlarning xech biriga bo'linmaydi")
    