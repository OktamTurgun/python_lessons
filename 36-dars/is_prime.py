# Mantiqiy qiymatlarni tekshirish
# import math

# Exercise: 1
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):  # faqat toq sonlarni tekshiramiz
        if n % i == 0:
            return False
    return True

# Exercise: 2
# def is_prime(n):
#     """Tub sonlarni tekshirish funksiyasi"""
#     # 1 dan kichik yoki teng sonlar tub emas
#     if n <= 3:
#         return n > 1  # 2 va 3 uchun True, 1 dan kichiklar uchun False
#     # 2 va 3 dan katta bo'lgan juft sonlar tub emas
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     # 5 dan n ning kvadrat ildiziga bo'linish qobilyatini tekshirish
#     for i in range(5, int(n**0.5) + 1, 6): # 5, 11, 17, ... va 7, 13, 19, ... larni tekshiramiz
#         # 6 ga bo'linmaydigan sonlar (6k ± 1) ni tekshiramiz
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#     return True

# Exercise: 3
# def is_prime(n):
#     # 1 dan kichik yoki teng sonlar tub emas
#     if n <= 1:
#         return False
#     # 2 yagona juft tub son
#     if n == 2:
#         return True
#     # 2 dan katta bo'lgan juft sonlar tub emas
#     if n % 2 == 0:
#         return False

#     # 3 dan n ning kvadrat ildiziga bo'linish qobiliyatini tekshiring,
#     # faqat toq raqamlarni tekshirish uchun 2 ga oshirish
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False

#     return True
