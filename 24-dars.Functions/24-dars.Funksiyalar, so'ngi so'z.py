"""
Created on Mon June 02 12:00:21 2025

24-dars. "Funksiyalar, so'ngi so'z" (lambda)

@author: uktam
"""

import math

# def nom(argument):
#   return argument

# Nomsiz funksiyalar
# Nomsiz funksiyalar (lambda funksiyalar) - bu qisqa va tez yoziladigan funksiyalar
# va ular asosan bir marta ishlatiladigan qisqa kod bloklari uchun mo'ljallangan.
# Lambda funksiyalarni yaratish sintaksisi:
# lambda argumentlar: ifoda
# Misol:
multiply = lambda x, y: x * y

# Lambda funksiyalarni ishlatish

print(multiply(5, 3))  # Natija: 15

# Lambda funksiyalarni ro'yxatlarda ishlatish
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Natija: [1, 4, 9, 16, 25]

# Lambda funksiyalarni filtrda ishlatish
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(filtered_numbers)  # Natija: [2, 4]

# Lambda funksiyalarni tartiblashda ishlatish
sorted_numbers = sorted(numbers, key=lambda x: -x)  # Katta qiymatdan kichik qiymatga
print(sorted_numbers)  # Natija: [5, 4, 3, 2, 1]


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def calculate_area(radius):
    return (lambda r: math.pi * r**2)(radius)


print(calculate_area(5))  # Natija: 78.53981633974483


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def is_even(num):
    return (lambda x: x % 2 == 0)(num)


print(is_even(4))  # Natija: True


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def greet(name):
    return (lambda n: f"Salom, {n}!")(name)


print(greet("Uktam"))  # Natija: Salom, Uktam!


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def add(x, y):
    return (lambda a, b: a + b)(x, y)


print(add(3, 5))  # Natija: 8


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
# def multiply(x, y):
#     return (lambda a, b: a * b)(x, y)


# print(multiply(4, 6))  # Natija: 24

# uzunlik = lambda pi, r: 2 * pi * r
# print(uzunlik(math.pi, 10))  # Natija:

# kvadrat = lambda a, b: a**b
# print(kvadrat(5, 3))


def daraja(n):
    return lambda x: x**n

# print(daraja(3)(2))  # Natija: 8
# print(daraja(2)(5))  # Natija: 25

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kavdrati: {kvadrat(3)} ga teng \n"
      f"kubi esa: {kub(3)} ga teng")

# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def is_prime(num):
    return (lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)))(num)


print(is_prime(7))  # Natija: True
print(is_prime(10))  # Natija: False


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def factorial(n):
    return (lambda x: 1 if x == 0 else x * factorial(x - 1))(n)


print(factorial(5))  # Natija: 120


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def fibonacci(n):
    return (lambda x: x if x <= 1 else fibonacci(x - 1) + fibonacci(x - 2))(n)


print(fibonacci(5))  # Natija: 5


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def reverse_string(s):
    return (lambda x: x[::-1])(s)


print(reverse_string("Salom"))  # Natija: "molaS"


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def count_vowels(s):
    return (lambda x: sum(1 for char in x if char.lower() in "aeiou"))(s)


print(count_vowels("Salom, Dunyo!"))  # Natija: 5


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def to_uppercase(s):
    return (lambda x: x.upper())(s)


print(to_uppercase("salom"))  # Natija: "SALOM"


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def to_lowercase(s):
    """Bu funksiya berilgan matnni kichik harflarga o'giradi.
    Args:
        s (str): Katta harflardan iborat matn.
        Returns:
        str: Kichik harflarga o'girgan matn.
    """
    return (lambda x: x.lower())(s)


print(to_lowercase("SALOM"))  # Natija: "salom"


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def is_palindrome(s):
    return (lambda x: x == x[::-1])(s)


print(is_palindrome("radar"))  # Natija: True
print(is_palindrome("hello"))  # Natija: False


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def sum_of_digits(n):
    return (lambda x: sum(int(digit) for digit in str(x)))(n)


print(sum_of_digits(12345))  # Natija: 15


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def is_anagram(s1, s2):
    return (lambda x, y: sorted(x) == sorted(y))(s1, s2)


print(is_anagram("listen", "silent"))  # Natija: True
print(is_anagram("hello", "world"))  # Natija: False


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def find_max(numbers):
    return (lambda nums: max(nums))(numbers)


print(find_max([1, 2, 3, 4, 5]))  # Natija: 5


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def find_min(numbers):
    return (lambda nums: min(nums))(numbers)


print(find_min([1, 2, 3, 4, 5]))  # Natija: 1


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def calculate_average(numbers):
    return (lambda nums: sum(nums) / len(nums))(numbers)


print(calculate_average([1, 2, 3, 4, 5]))  # Natija: 3.0


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def is_sorted(numbers):
    return (lambda nums: nums == sorted(nums))(numbers)


print(is_sorted([1, 2, 3, 4, 5]))  # Natija: True
print(is_sorted([5, 4, 3, 2, 1]))  # Natija: False


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def remove_duplicates(numbers):
    return (lambda nums: list(set(nums)))(numbers)


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Natija: [1, 2, 3, 4, 5]


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def flatten(nested_list):
    return (lambda lst: [item for sublist in lst for item in sublist])(nested_list)


print(flatten([[1, 2], [3, 4], [5]]))  # Natija: [1, 2, 3, 4, 5]


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def zip_lists(list1, list2):
    return (lambda l1, l2: list(zip(l1, l2)))(list1, list2)


print(zip_lists([1, 2, 3], ["a", "b", "c"]))  # Natija: [(1, 'a'), (2, 'b'), (3, 'c')]


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def unzip_list(pairs):
    return (lambda lst: list(zip(*lst)))(pairs)


print(
    unzip_list([(1, "a"), (2, "b"), (3, "c")])
)  # Natija: [(1, 2, 3), ('a', 'b', 'c')]


# Lambda funksiyalarni qisqa kod bloklari uchun ishlatish
def find_common_elements(list1, list2):
    return (lambda l1, l2: list(set(l1) & set(l2)))(list1, list2)


print(find_common_elements([1, 2, 3], [2, 3, 4]))  # Natija: [2, 3]
