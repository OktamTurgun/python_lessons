"""
10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
"""
# for num in range(11,100,2):
#   print(num**3)

"""
Agar natijani ro‘yxat shaklida saqlash kerak bo‘lsa, list comprehension ishlatish mumkin:
"""
# cubes = [num**3 for num in range(11, 100, 2)]
# print(cubes)

"""
Agar natijani birma-bir chiqarish kerak bo'lsa va ro'yxat saqlash 
shart bo'lmasa, generator ishlatish yaxshi:
"""
# cubes = [num**3 for num in range(11, 100, 2)]
# for cube in cubes:
#   print(cube)

"""
Agar CPU hisoblashda qiyinchilik bo'lsa, num * num * num 
oddiy ko'paytirish num**3 dan biroz tezroq bo'lishi mumkin:
"""
numbers = range(11, 20, 2)
for num in numbers:
  print(f"{num} ning kubi = {num*num*num} ga teng") # num**3 dan biroz tezroq