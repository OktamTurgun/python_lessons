# # mahsulot_manager.py
# import pickle
# import os

# FILENAME = "mahsulotlar.pkl"

# class Mahsulot:
#     def __init__(self, nomi, narx):
#         self.nomi = nomi
#         self.narx = narx

#     def __repr__(self):
#         return f"{self.nomi} - {self.narx} so'm"

# def load_mahsulotlar():
#     if os.path.exists(FILENAME):
#         with open(FILENAME, "rb") as file:
#             return pickle.load(file)
#     return []

# def save_mahsulotlar(mahsulotlar):
#     with open(FILENAME, "wb") as file:
#         pickle.dump(mahsulotlar, file)

# def show_mahsulotlar():
#     mahsulotlar = load_mahsulotlar()
#     if mahsulotlar:
#         print("\n📋 Mahsulotlar ro'yxati:")
#         for m in mahsulotlar:
#             print(m)
#     else:
#         print("\n📂 Mahsulotlar ro'yxati bo‘sh.")

# def add_mahsulot():
#     nomi = input("Yangi mahsulot nomi: ")
#     try:
#         narx = int(input("Narxi: "))
#     except ValueError:
#         print("❌ Narx faqat butun son bo‘lishi kerak.")
#         return

#     mahsulotlar = load_mahsulotlar()
#     mahsulotlar.append(Mahsulot(nomi, narx))
#     save_mahsulotlar(mahsulotlar)
#     print(f"✅ {nomi} mahsuloti qo‘shildi.")
#     show_mahsulotlar()

# def delete_mahsulot():
#     nom = input("O‘chirmoqchi bo‘lgan mahsulot nomi: ").lower()
#     mahsulotlar = load_mahsulotlar()
#     yangi_royxat = [m for m in mahsulotlar if m.nomi.lower() != nom]

#     if len(mahsulotlar) == len(yangi_royxat):
#         print(f"❗ {nom} topilmadi.")
#     else:
#         save_mahsulotlar(yangi_royxat)
#         print(f"❌ {nom} o‘chirildi.")
#         show_mahsulotlar()

# def menu():
#     while True:
#         print("\n🛒 Mahsulotlar Boshqaruvi")
#         print("1. Mahsulotlarni ko‘rish")
#         print("2. Yangi mahsulot qo‘shish")
#         print("3. Mahsulotni o‘chirish")
#         print("0. Chiqish")
#         tanlov = input("Tanlovni kiriting: ")

#         if tanlov == "1":
#             show_mahsulotlar()
#         elif tanlov == "2":
#             add_mahsulot()
#         elif tanlov == "3":
#             delete_mahsulot()
#         elif tanlov == "0":
#             print("👋 Dasturdan chiqildi.")
#             break
#         else:
#             print("❌ Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")

# if __name__ == "__main__":
#     menu()

class Mahsulot:
    def __init__(self, nomi: str, narxi: int):
        self.nomi = nomi
        self.narxi = narxi

    def __repr__(self):
        return f"{self.nomi} - {self.narxi} so'm"