# student_manager.py
import pickle
import os

FILENAME = "students.pkl"

class Talaba:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def __repr__(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yosh"


def load_students():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "rb") as file:
        return pickle.load(file)


def save_students(students):
    with open(FILENAME, "wb") as file:
        pickle.dump(students, file)


def add_student():
    ism = input("Ism: ")
    familiya = input("Familiya: ")
    yosh = input("Yosh: ")
    student = Talaba(ism, familiya, yosh)
    students = load_students()
    students.append(student)
    save_students(students)
    print(f"✅ {ism} qo'shildi.")


def show_students():
    students = load_students()
    if not students:
        print("📂 Ro'yxat bo'sh!")
        return
    print("\n📋 Talabalar ro'yxati:")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s}")


def delete_student():
    show_students()
    students = load_students()
    if not students:
        return
    try:
        index = int(input("O'chirmoqchi bo'lgan talabani tartib raqamini kiriting: ")) - 1
        if 0 <= index < len(students):
            nom = students[index]
            del students[index]
            save_students(students)
            print(f"❌ {nom} o'chirildi.")
        else:
            print("🚫 Noto'g'ri raqam!")
    except ValueError:
        print("🚫 Raqam kiriting!")


def main():
    while True:
        print("\n🎓 Student Manager")
        print("1. Talaba qo'shish")
        print("2. Talabalarni ko'rish")
        print("3. Talabani o'chirish")
        print("4. Chiqish")
        choice = input("Tanlang (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            show_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Chiqildi. 👋")
            break
        else:
            print("🚫 Noto‘g‘ri tanlov. 1-4 oralig‘ida raqam kiriting.")


if __name__ == "__main__":
    main()
