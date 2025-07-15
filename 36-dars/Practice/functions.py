"""
Quyidagi funksiyalarni yarating, va ularning har biri uchun test dasturlarini yozing:

Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya

Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya

Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya

Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi funksiya yozing.
"""


def max_num(a, b, c):
    """3 ta son qabul qilib eng kattasini qaytaruvchi funksiya"""
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


def capitalize_words(words):
    """Ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgartiradi"""
    for i in range(len(words)):
        words[i] = words[i].title()
    return words


def extract_even_nums(nums):
    """Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya"""
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens


def is_fibonacci(n):
    """Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi funksiya yozing."""
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0
