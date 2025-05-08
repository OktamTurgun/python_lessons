"""
Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa
 "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
"""
# num = int(input("Juft son kiriting: "))
# if num % 2 == 0:
#   print("Raxmat")
# else:
#   print("Bu son juft emas!")

'''
Loop bilan foydalanuvchi to'g'ri son kiritmaguncha so'rash:
'''
# while True:
#   num = int(input("Juft son kiriting: "))
#   if num % 2 == 0:
#     print("Raxmat")
#     break
#   else: 
#     print("Bu son juft emas! Qaytadan urunib ko'ring.")

'''
Qisqaroq yozish xam mumkin
'''
num = int(input("Juft son kiriting: "))
print("Raxmat" if num % 2 == 0 else "Bu juft son emas")