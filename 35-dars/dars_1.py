"""
Created on Mon Jun 23 22:02:14 2025

35-dars. Xatolar bilan ishlash. Exception handling 

@author: uktam
"""
# ZeroDevisionError - nolga bo'lish xatosi

# Exercise: 1
import json
x, y = 5, 10
try:
    z = y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas!")

# Exercise: 2


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Xato: {e}. Nolga bo'lish mumkin emas!")
        return None
    else:
        return result

# ValueError - noto'g'ri qiymat xatosi


def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        print(f"Xato: {e}. Iltimos, faqat butun son kiriting!")
        return None

# FileNotFoundError - fayl topilmagan xatosi


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"Xato: {e}. Fayl topilmadi!")
        return None

# TypeError - noto'g'ri turdagi qiymat xatosi


def add_numbers(a, b):
    try:
        return a + b
    except TypeError as e:
        print(f"Xato: {e}. Iltimos, raqamlarni qo'shing!")
        return None

# KeyError - kalit topilmagan xato


# Exercise: 1
user = {
    "username": "sariqdev",
    "status": "admin",
    "email": "admin@sariq.dev",
    "phone": "998971234567"
}
key = "email"
try:
    print(f"Foydalanuvchi: {user[key]}")
except KeyError:
    print("Xato! Bunday kalit mavjud emas.")

# Exercise: 2


def get_value_from_dict(dictionary, key):
    try:
        return dictionary[key]
    except KeyError as e:
        print(f"Xato: {e}. Kalit topilmadi!")
        return None

# IndexError - indeks topilmagan xato


# Exercise: 1
mevalar = ("olam", "anor", "uzum", "anjir")
try:
    print(mevalar[7])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")

# Exercise: 2


def get_item_from_list(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        print(f"Xato: {e}. Indeks ro'yxatdan tashqarida!")
        return None

# AttributeError - atribut topilmagan xato


def get_length_of_string(s):
    try:
        return len(s)
    except TypeError as e:
        print(f"Xato: {e}. Iltimos, satr yoki ro'yxat kiriting!")
        return None

# ImportError - modul topilmagan xato


def import_module(module_name):
    try:
        module = __import__(module_name)
        return module
    except ImportError as e:
        print(f"Xato: {e}. Modul topilmadi!")
        return None

# AssertionError - tekshirish xatosi


def assert_positive(value):
    try:
        assert value > 0, "Qiymat musbat bo'lishi kerak!"
    except AssertionError as e:
        print(f"Xato: {e}")
        return None
    else:
        return value

# RuntimeError - bajarilish xatosi


def risky_operation():
    try:
        # Bu yerda xato yuz berishi mumkin
        raise RuntimeError("Bajarilish xatosi yuz berdi!")
    except RuntimeError as e:
        print(f"Xato: {e}")
        return None
    else:
        return "Operatsiya muvaffaqiyatli bajarildi!"


# FieldNotFoundError - fayl topilmagan xatosi
# Exercise: 1
# filename = "data.txt"  # Bunday file mavjud emas.
# try:
#     with open(filename) as file:
#         text = file.read()
# except FileNotFoundError:
#     print(f"Xato! {filename} mavjud emas.")

# Exercise: 2
files = ['data/talaba1.json', 'data/talaba2.json',
         'data/talaba3.json', 'data/talaba4.json']
for file in files:
    try:
        # Xato kelib chiqishi mumkin bo'lgan kod
        with open(file) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        # Xato yuz berganda bajariladigan kod
        print(f"{file} mavjud emas!")
        # Yoki xech narsa bajarmasdan o'tib ketishi uchun
        # pass # oberatoridan foydalanamiz
    else:
        print(f"Talaba ismi: {talaba['ism']}")

# Exercise: 3
n = input("Butun son kiriting: ")


def divide_by_input(n):
    """Foydalanuvchi kiritgan son bilan 20 ni bo'lish"""
    try:
        n = int(n)
        if n < 0:
            raise ValueError(
                "Son manfiy bo'lishi mumkin emas! Iltimos, musbat son kiriting.")
        result = 20 / n
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Xato: Noto'g'ri format! Faqat son kiriting.")
        else:
            print(f"Xato: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"Xato: {e}. Nolga bo'lish mumkin emas!")
        return None
    except Exception as e:
        print(f"Umumiy xato: {e}. Iltimos, qayta urinib ko'ring!")
        return None
    else:
        return result
    finally:
        print("Bolish operatsiyasi tugadi.")


result = divide_by_input(n)
if result is not None:
    print(f"20 ni {n} ga bo'lish natijasi: {result}")

# Exercise: 4


def field_not_found_error():
    try:
        # Bu yerda xato yuz berishi mumkin
        raise FileNotFoundError("Fayl topilmadi!")
    except FileNotFoundError as e:
        print(f"Xato: {e}")
        return None
    else:
        return "Fayl muvaffaqiyatli topildi!"


# OOP xatolar bilan ishlash


class CustomError(Exception):
    """Maxsus xato sinfi"""
    pass


class MyClass:
    def __init__(self, value):
        if not isinstance(value, int):
            raise CustomError("MyClass ga faqat butun son kiritilishi kerak!")
        self.value = value

    def get_value(self):
        return self.value

# MyClass dan obyekt yaratish va xatolarni boshqarish


def create_my_class_instance(value):
    try:
        instance = MyClass(value)
        return instance
    except CustomError as e:
        print(f"Xato: {e}")
        return None


# Test funksiyalarini chaqirish
if __name__ == "__main__":
    print("Nolga bo'lish:", divide_numbers(10, 0))
    print("Noto'g'ri qiymat:", convert_to_int("abc"))
    print("Faylni o'qish:", read_file("nonexistent.txt"))
    print("Noto'g'ri turdagi qo'shish:", add_numbers(5, "10"))
    print("Kalit topilmagan:", get_value_from_dict({"a": 1}, "b"))
    print("Indeks ro'yxatdan tashqarida:", get_item_from_list([1, 2, 3], 5))
    print("Atribut topilmagan:", get_length_of_string(123))
    print("Modul topilmagan:", import_module("nonexistent_module"))
    print("Tekshirish xatosi:", assert_positive(-5))
    print("Bajarilish xatosi:", risky_operation())
    print(f"20 ni {n} ga bo'lish natijasi:", divide_by_input(n))
    print("Fayl topilmagan xato:", field_not_found_error())
# OOP xatolar bilan ishlash
    my_instance = create_my_class_instance(10)
    if my_instance:
        print("MyClass instance:", my_instance.get_value())
    my_instance = create_my_class_instance("abc")  # Bu yerda xato yuz beradi
    if my_instance:
        print("MyClass instance:", my_instance.get_value())

# Ushbu kodda turli xil xatolarni qanday aniqlash va ularga qanday javob berish ko'rsatilgan
# Har bir funksiya o'ziga xos xatolarni aniqlaydi va ularga mos ravishda javob beradi
# Xatolarni aniqlash va ularga javob berish uchun try-except bloklaridan foydalaniladi
