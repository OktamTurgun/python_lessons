'''
Juftsiz sonni topish uchun funksiya yozing
'''
# def find_lonely_number(numbers):
#     """Berilgan ro'yxatda bitta juftsiz sonni topish uchun funksiya."""
#     # Har bir sonni tekshiramiz
#     for number in numbers:
#         # Agar sonning ro'yxatda faqat bitta ko'rinishi bo'lsa, uni qaytaramiz
#         if numbers.count(number) == 1:
#             return number
#     return None  # Agar juftsiz son topilmasa, None qaytaradi
# # Funksiyani chaqirish
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# lonely_number = find_lonely_number(numbers)
# print(f"Juftsiz son: {lonely_number}")  # Juftsiz sonni chiqaradi 

''''''
# Variant 2
def lonely_num(nums):
  """Berilgan ro'yxatda bitta juftsiz sonni topish uchun funksiya."""
  result = 0
  for num in nums:
    result ^= num
  return result
# Funksiyani chaqirish  
nums = [1, 1, 3, 3, 5, 5, 7, 8, 9, 10, 10, 9, 14, 14, 7]
lonely_number = lonely_num(nums)
print(f"Juftsiz son: {lonely_number}")  # Juftsiz son: 8
