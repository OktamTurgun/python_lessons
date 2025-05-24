'''
Ro'yxat elementlarini yig'indisini hisoblash
Vazifa: Funksiya yarating, u ro'yxatdagi sonlarning yig'indisini hisoblab qaytarsin.
'''
'''Exercises 1'''
# def sum_nums(nums):
#   """Ro'yxatdagi sonlarning yig'indisini hisoblaydi va qaytaradi"""
#   # ro'yxatni o'zgartirmaydi
#   total = 0
#   for num in nums:
#       total += num 
#   return total

# numbers = [1, 2, 3, 4, 5]
# total_nums = sum_nums(numbers)
# print(total_nums)
# print(numbers)

'''Exercises 2'''
# def sum_nums(nums):
#   """Ro'yxatdagi sonlarning yig'indisini hisoblaydi va qaytaradi"""
#   # ro'yxatni o'zgartirmaydi
#   return sum(nums)

# numbers = [1, 2, 3, 4, 5]
# total_nums = sum_nums(numbers)    
# print(total_nums)  # 15
# print(numbers)     # [1, 2, 3, 4, 5]

'''Exercises 3'''
from functools import reduce

def sum_nums(nums):
    """Ro'yxatdagi sonlarning yig'indisini hisoblaydi va qaytaradi"""
    return reduce(lambda a, b: a + b, nums)

numbers = [1, 2, 3, 4, 5]
print(sum_nums(numbers))  # 15    
