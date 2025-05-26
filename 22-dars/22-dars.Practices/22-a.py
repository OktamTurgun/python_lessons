'''
Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
'''
# Example: 1
def kopaytma(*sonlar):
    """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya"""
    natija = 1
    for son in sonlar:
        natija *= son
    return natija
# Misol uchun:
print(kopaytma(2, 3))          # 6
print(kopaytma(1, 2, 3, 4))    # 24

''''''
# Example: 2
def multiply(*args):
    """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya"""
    if not args:  # Agar hech qanday argument berilmasa
        return None
    result = 1
    for num in args:
        result *= num
    return result
# Misol uchun:
print(multiply(2, 3))          # 6
print(multiply(1, 2, 3, 4))    # 24
 