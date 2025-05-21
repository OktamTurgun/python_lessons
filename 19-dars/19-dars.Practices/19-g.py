"""
Eng katta son: Uchta sonni parametr qilib oladigan va ular orasidagi eng katta sonni qaytaradigan funksiya yozing.
"""
# def eng_katta_son(x, y, z):
#     if x>y and x>z:
#         return x
#     elif y>x and y>z:
#         return y
#     else:
#         return z
# print(eng_katta_son(123, 46, 25))

''''''
def max_number(x, y, z):
    """Uchta sonni parametr qilib oladigan va ular orasidagi eng katta sonni qaytaradigan funksiya."""
    return max(x, y, z)
print(max_number(123, 432, 234))

''''''
def find_max(a, b, c):
  """Uchta sonni parametr qilib oladigan va ular orasidagi eng katta sonni qaytaradigan funksiya."""
  max = a
  if b > max:
    max = b
  if c > max:
    max = c
  return max
print(find_max(12, 53, 23))

''''''
def mux_num(*args):
    """Ixtiyoriy miqdordagi sonlarni qabul qilib, eng kattasini qaytaradi."""
    return max(args)
print(mux_num(12, 23, 34, 42, 54, 65, 78))

''''''
def find_max_num(*args):
  """Ixtiyoriy miqdordagi sonlarni qabul qilib, eng kattasini qaytaruvchi funksiya."""
  if not args:
    return None
  max_num = args[0]
  for num in args[1:]:
    if num > max_num:
      max_num = num
  return max_num
print(find_max_num(12, 23, 34, 42, 54, 65, 78))
print(find_max_num(3, 88, 5, 33, 17, 65, 36, 2, 99))
print(find_max_num()) 