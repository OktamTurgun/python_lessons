"""
Keyin main.py faylda bu moduldan foydalanib, oddiy kalkulyator dasturi yozing.
"""

from calculator import add, subtract, multiply, divide, power, sqrt
from person import create_person, dict_to_person, display_person, update_person


def main_calc():
    print("Kalkulyator dasturi")
    print("1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")
    print("5. Darajaga ko'tarish")
    print("6. Kvadrat ildiz olish")

    choice = input("Tanlovingizni kiriting (1-6): ")

    if choice in ["1", "2", "3", "4", "5", "6"]:
        a = float(input("Birinchi sonni kiriting: "))
        b = float(input("Ikkinchi sonni kiriting: ")) if choice != "6" else None

        if choice == "1":
            print(f"Natija: {add(a, b)}")
        elif choice == "2":
            print(f"Natija: {subtract(a, b)}")
        elif choice == "3":
            print(f"Natija: {multiply(a, b)}")
        elif choice == "4":
            print(f"Natija: {divide(a, b)}")
        elif choice == "5":
            print(f"Natija: {a} ning {b} darajasi {power(a, b)} ga teng")
        elif choice == "6":
            print(f"Natija: {sqrt(a)}")
    else:
        print("Noto'g'ri tanlov!")


""""""


def main():
    # Yangi shaxslar yaratish
    person1 = create_person("Ali", 23, "erkak", "Toshkent", "Shifokor")
    person2 = create_person("Noila", 18, "ayol", "Samrqand", "talaba")
    person3 = create_person("Anvar", 30, "erkak", "Buxoro")

    # Shaxs ma'lumotlarini ko'rsatish
    print("\nDastlabki ma'lumotlar:")
    display_person(person1)
    display_person(person2)
    display_person(person3)

    # Shaxs ma'lumotlarini yangilash
    person1 = update_person(person1, age=24, city="Andijon")
    person2 = update_person(person2, accupation="dasturchi")
    person3 = update_person(
        person3, name="Anvarbek", age=31, city="Navoiy", accupation="muhandis"
    )

    # Yangilangan shaxs ma'lumotlarini ko'rsatish
    print("\nYangilangan ma'lumotlar:")
    display_person(person1)
    display_person(person2)
    display_person(person3)

    # Yangi shaxs qo'shish
    print("\nYnagi shaxs qo'shamiz:")
    name = input("Ism: ")
    age = int(input("Yosh: "))
    gender = input("Jins (erkak/ayol): ")
    city = input("Shahar: ")
    accupation = input("Kasb (Ixtiyoriy, bo'sh qoldirish mumkin): ") or None

    new_person = create_person(name, age, gender, city, accupation)
    display_person(new_person)
    print("\nYangi shaxs qo'shildi:")


if __name__ == "__main__":
    main()
