'''
Ro'yxat elementlari yig'indisi: Butun sonlardan iborat ro'yxatni
parametr qilib oladigan va ro'yxatdagi barcha sonlarning 
yig'indisini qaytaradigan funksiya yozing.
'''
def list_sum(numbers):
    """Butun sonlardan iborat ro'yxatni parametr qilib oladigan va ro'yxatdagi barcha sonlarning yig'indisini qaytaradi."""
    return sum(numbers)
print(list_sum([5, 4, 3, 2, 1]))  # 15
print(list_sum([10, 20, 30, 40, 50]))  # 150

''''''
def list_num(numbers: list[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(numbers)
print(list_num([5, 4, 3, 2, 1]))

''''''
def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total    
print(list_sum([12, 5, 23, 9, 43, 27, 3]))    
print(list_sum([1, 2, 3, 4, 5])) 

''''''
# Oraliqdagi sonlar: Berilgan oraliqdagi sonlarni qaytaruvchi funksiya yozing.
# Masalan, oraliq(0, 11, 2) funksiyasi 0 dan 10 gacha bo'lgan sonlarni  
def oraliq(min, max, step=1):
    """Berilgan oraliqdagi sonlarni qaytaruvchi funksiya."""
    sonlar = []
    while min <= max:
      sonlar.append(min)
      min += step
    return sonlar

print(oraliq(0, 11, 2))
    