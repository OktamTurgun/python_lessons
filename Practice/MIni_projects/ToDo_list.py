"""
Mavzu: Practice. Mini projects
Muallif: Uktam Turgunov
Sana: 2025-07-10
"""


def todo():
    vazifalar = []

    while True:
        print("\n📝 To-do List")
        print("1️⃣ Vazifa qo‘shish")
        print("2️⃣ Vazifalar ro‘yxati")
        print("3️⃣ Vazifa o‘chirish")
        print("0️⃣ Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            vazifa = input("Yangi vazifa: ")
            vazifalar.append(vazifa)
            print("✅ Vazifa qo‘shildi.")
        elif tanlov == "2":
            if not vazifalar:
                print("🚫 Vazifalar yo‘q.")
            else:
                for i, v in enumerate(vazifalar, 1):
                    print(f"{i}. {v}")
        elif tanlov == "3":
            if not vazifalar:
                print("🚫 O‘chirish uchun vazifa yo‘q.")
            else:
                for i, v in enumerate(vazifalar, 1):
                    print(f"{i}. {v}")
                index = int(input("O‘chiradigan vazifa raqami: ")) - 1
                if 0 <= index < len(vazifalar):
                    print(f"🗑️ {vazifalar.pop(index)} o‘chirildi.")
                else:
                    print("🚫 Noto‘g‘ri raqam.")
        elif tanlov == "0":
            print("🚪 Dasturdan chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov.")


todo()
