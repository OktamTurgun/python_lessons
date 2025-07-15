"""
Xato yozilgan code:
"""
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun'


# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")    

# To'g'irlangan code:
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun'] # SynaxError: List "[]" qavslar yopilmagan

# cart = [] # Bo'sh ro'yxat yaratilmagan

# for n in range(5):
#   cart.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ")) # AttributeError: "int" obyektida "qo'shish" atributi yo'q

# if cart:
#   for mahsulot in cart:
#     if mahsulot in mahsulotlar:
#       print(f"Do'konimizda {mahsulot} bor")
#     else:
#       print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#   print("Savatingiz bo'sh")   

# To'g'irlangan code 2: Bu codda "savatingiz bo'sh xa ishlaydi "
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

cart = [] # Bo'sh ro'yxat yaratildi

for n in range(5):
  mahsulot = (input(f"Savatga {n+1}-mahsulotni qo'shing: ")).strip()

  if mahsulot: # Agar maxsulot bo'sh bo'lmasa
    cart.append(mahsulot)

if not cart: # Agar cart bo'sh bo'lsa
  print("Savatingiz bo'sh:")
else:
  for mahsulot in cart:
    if mahsulot in mahsulotlar:
      print(f"Do'konimizda {mahsulot} bor")
    else:
      print(f"Do'konimizda {mahsulot} yo'q")
