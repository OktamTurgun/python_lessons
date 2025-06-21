# 1-mashq: Mahsulotlar obyektini faylga yozish
import pickle

class Mahsulot:
    def __init__(self, nomi, narx):
        self.nomi = nomi
        self.narx = narx

    def __repr__(self):
        return f"{self.nomi} - {self.narx} so'm"

mahsulotlar = [
    Mahsulot("Non", 3000),
    Mahsulot("Sut", 8000),
    Mahsulot("Yog'", 17000)
]

with open("mahsulotlar.pkl", "wb") as file:
    pickle.dump(mahsulotlar, file)

print("✅ Mahsulotlar saqlandi.")


# 2-mashq: Mahsulotlar ro‘yxatini o‘qish
with open("mahsulotlar.pkl", "rb") as file:
    mahsulotlar = pickle.load(file)

print("\n📋 Mahsulotlar ro'yxati:")
for m in mahsulotlar:
    print(m)


# 3-mashq: Fayl mavjud bo‘lmasa, yaratish
import os
filename = "mahsulotlar.pkl"

if os.path.exists(filename):
    with open(filename, "rb") as file:
        mahsulotlar = pickle.load(file)
        print("\n🔁 Fayldan o‘qildi:")
        for m in mahsulotlar:
            print(m)
else:
    with open(filename, "wb") as file:
        pickle.dump([], file)
        print("❗ Fayl topilmadi. Bo‘sh fayl yaratildi.")


# 4-mashq: Yangi mahsulot qo‘shish (update)
yangi = Mahsulot("Choy", 10000)
try:
    with open(filename, "rb") as file:
        mahsulotlar = pickle.load(file)
except (FileNotFoundError, EOFError):
    mahsulotlar = []

mahsulotlar.append(yangi)

with open(filename, "wb") as file:
    pickle.dump(mahsulotlar, file)

print("✅ Yangi mahsulot qo‘shildi.")


# 5-mashq: Mahsulot o‘chirish
with open(filename, "rb") as file:
    mahsulotlar = pickle.load(file)

nom = input("\nO‘chirmoqchi bo‘lgan mahsulot nomi: ")
mahsulotlar = [m for m in mahsulotlar if m.nomi.lower() != nom.lower()]

with open(filename, "wb") as file:
    pickle.dump(mahsulotlar, file)

print(f"❌ {nom} o‘chirildi (agar mavjud bo‘lsa).")

# Qolgan mahsulotlarni ko'rsatish\print("\n🔎 Qolgan mahsulotlar:")
if mahsulotlar:
    for m in mahsulotlar:
        print(m)
else:
    print("📂 Hech qanday mahsulot qolmagan.")