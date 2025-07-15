from manager.storage import load_mahsulotlar, save_mahsulotlar
from manager.product import Mahsulot

def menu():
    while True:
        print("\n📋 Mahsulotlar menyusi")
        print("1. Mahsulotlarni ko‘rish")
        print("2. Yangi mahsulot qo‘shish")
        print("3. Mahsulotni o‘chirish")
        print("0. Chiqish")

        tanlov = input("Tanlov: ").strip()

        if tanlov == "1":
            mahsulotlar = load_mahsulotlar()
            if not mahsulotlar:
                print("📂 Mahsulotlar ro‘yxati bo‘sh.")
            else:
                for m in mahsulotlar:
                    print(f"🟢 {m}")
        elif tanlov == "2":
            nomi = input("Mahsulot nomi: ")
            try:
                narxi = int(input("Narxi: "))
            except ValueError:
                print("❗ Narx raqam bo‘lishi kerak.")
                continue
            mahsulotlar = load_mahsulotlar()
            mahsulotlar.append(Mahsulot(nomi, narxi))
            save_mahsulotlar(mahsulotlar)
            print("✅ Yangi mahsulot qo‘shildi.")
        elif tanlov == "3":
            nom = input("O‘chirmoqchi bo‘lgan mahsulot nomi: ")
            mahsulotlar = load_mahsulotlar()
            yangi = [m for m in mahsulotlar if m.nomi.lower() != nom.lower()]
            if len(yangi) == len(mahsulotlar):
                print("❗ Bunday mahsulot topilmadi.")
            else:
                save_mahsulotlar(yangi)
                print(f"❌ {nom} o‘chirildi.")
        elif tanlov == "0":
            print("👋 Dastur yakunlandi.")
            break
        else:
            print("⚠️ Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")