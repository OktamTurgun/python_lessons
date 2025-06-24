"""
Created on Mon Jun 23 22:02:14 2025

35-dars. Xatolar bilan ishlash. Exception handling 

@author: uktam
"""
# ZeroDevisionError - nolga bo'lish xatosi


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


def get_value_from_dict(dictionary, key):
    try:
        return dictionary[key]
    except KeyError as e:
        print(f"Xato: {e}. Kalit topilmadi!")
        return None

# IndexError - indeks topilmagan xato


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

    my_instance = create_my_class_instance(10)
    if my_instance:
        print("MyClass instance:", my_instance.get_value())
    my_instance = create_my_class_instance("abc")  # Bu yerda xato yuz beradi
    if my_instance:
        print("MyClass instance:", my_instance.get_value())

# Ushbu kodda turli xil xatolarni qanday aniqlash va ularga qanday javob berish ko'rsatilgan
# Har bir funksiya o'ziga xos xatolarni aniqlaydi va ularga mos ravishda javob beradi
# Xatolarni aniqlash va ularga javob berish uchun try-except bloklaridan foydalaniladi
