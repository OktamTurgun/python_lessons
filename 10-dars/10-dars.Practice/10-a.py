"""
Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling
"""
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car == 'gm':
#     print(car.upper())
#   else:
#     print(car.title())

"""
Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
"""
# if car != 'gm':
#   print(car.title())
# else:
#   print(car.upper())

"""
List comprehension va join() dan foydalanish 
(agar barcha natijalarni bir qatorda chiqarmoqchi bo'lsangiz):
"""
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# print("\n" .join(car.upper() if car == 'gm' else car.title() for car in cars))
print("\n" .join(car.title() if car != 'gm' else car.upper() for car in cars))

