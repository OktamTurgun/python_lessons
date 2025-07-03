from fuzzywuzzy import fuzz, process

# Bazadagi ismlar
name_db = [
    "Ali", "Vali", "Sami", "Salim", "Jasur", "Jamshid", "Dilshod", "Aziz", "Azamat"
]


def main():
    print("📋 Ismni aniqlash yordamchisi")
    print("Ro‘yxatda mavjud ismlardan eng yaqinini topib beradi.")
    print("Ro‘yxat:", ", ".join(name_db))
    print("-" * 40)

    query = input("Ism kiriting: ")

    # Eng yaqin bitta moslik
    match = process.extractOne(query, name_db)
    if match:
        print(f"✅ Eng yaqin ism: {match[0]} ({match[1]}% o‘xshash)")
    else:
        print("❌ Hech qanday moslik topilmadi.")


if __name__ == "__main__":
    main()
