"""
Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
"""
def max_num(x, y, z):
    """Uchta sonni parametr qilib oladigan va ular orasidagi eng katta sonni qaytaruvchi funksiya."""
    return max(x, y, z)
print(max_num(12, 23, 34))

''''''
def max_num(x,y,z):
    """3 ta son qabul qilib eng kattasini qaytaruvchi funksiya"""
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    return max
print(max_num(16, 15, 14))

''''''
def find_max_num(*args):
    """Ixtiyoriy miqdordagi sonlarni qabul qilib, eng kattasini qaytaruvchi funksiya."""
    # Agar argumentlar bo'lmasa, None qaytaradi
    if not args:
        return None
    # Dastlabki eng katta sonni birinchi argumentga tenglaymiz
    max_num = args[0]
    for num in args[1:]:
        if num > max_num:
            max_num = num
    # Eng katta sonni qaytaramiz
    return max_num
# Funksiyani chaqirish
numbers = find_max_num(1,2,3,4,5,6)
print(numbers)