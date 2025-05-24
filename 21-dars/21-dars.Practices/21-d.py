'''
Ro'yxatdagi eng katta sonni topish
Vazifa: Funksiya yarating, u ro'yxatdagi eng katta sonni topib qaytarsin.
'''
# Example 1
def max_num(nums):
  """ Ro'yxatdagi eng katta sonni topadi """
  if not nums:
      return None  # Agar ro'yxat bo'sh bo'lsa, None qaytaradi
  return max(nums)

numbers = [2, 5, 7, 23, 37, 67, 87]
max_number = max_num(numbers)
print(max_number)

''''''
# Exmple 2
def eng_katta(royxat):
    """Ro'yxatdagi eng katta sonni topadi"""
    if not royxat:
        return None
    max_num = royxat[0]
    for num in royxat:
        if num > max_num:
            max_num = num
    return max_num

sonlar = [10, 5, 20, 3, 37]
max_number = eng_katta(sonlar)
print(max_number)
