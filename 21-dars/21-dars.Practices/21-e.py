'''
Ro'yxat elementlarini teskari tartibda qaytarish
Vazifa: Funksiya yarating, u ro'yxat elementlarini teskari
tartibda qaytarsin (asl ro'yxatni o'zgartirmasdan).
'''
''''''
# Example 1
def reverse_list(lst):
    """Ro'yxat elementlarini teskari tartibda qaytaradi"""
    # ro'yxatni o'zgartirmaydi
    return lst[::-1]

numbers = ['one', 'two', 'three', 'four', 'five', 'six']
reversed_numbers = reverse_list(numbers)
print(reversed_numbers)  # ['six', 'five', 'four', 'three', 'two', 'one']
print(numbers)  # ['one', 'two', 'three', 'four', 'five', 'six']

''''''
# Example 2
def reverse_list(lst):
    """Ro'yxat elementlarini teskari tartibda qaytaradi"""
    # ro'yxatni o'zgartirmaydi
    return list(reversed(lst))  
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)
print(reversed_numbers)  # [5, 4, 3, 2, 1]
''''''
# Example 3
def reverse_list(lst):
    """Ro'yxat elementlarini teskari tartibda qaytaradi"""
    # ro'yxatni o'zgartirmaydi
    return lst.copy()[::-1]  # asl ro'yxatdan nusxa olib teskari qiladi
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)
print(reversed_numbers)  # [5, 4, 3, 2, 1]
''''''
# Example 4
def reverse_list(lst):
    """Ro'yxat elementlarini teskari tartibda qaytaradi"""
    # ro'yxatni o'zgartirmaydi
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)  # har bir elementni boshiga qo'shadi
    return reversed_lst
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)
print(reversed_numbers)  # [5, 4, 3, 2, 1]

''''''
# Example 5
def teskari(lst):
    """Ro'yxat elementlarini teskari tartibda qaytaradi"""
    # ro'yxatni o'zgartirmaydi
    return [lst[i] for i in range(len(lst) - 1, -1, -1)]  # indekslarni teskari yuritadi
numbers = [1, 2, 3, 4, 5]
reversed_numbers = teskari(numbers)
print(reversed_numbers)  # [5, 4, 3, 2, 1]

''''''
# Example 6
def teskari(royxat):
    """Ro'yxat elementlarini teskari tartibda qaytaradi"""
    if not royxat:
        return [] # Agar ro'yxat bo'sh bo'lsa, bo'sh ro'yxat qaytaradi
    # ro'yxatni o'zgartirmaydi
    # return list(reversed(royxat))  # reversed funksiyasidan foydalanadi
    return royxat[::-1]  # slicing orqali teskari qiladi
fruits = ['appla', 'banana', 'cherry']
reversed_fruits = teskari(fruits)   
print(reversed_fruits)  # ['cherry', 'banana', 'appla']
