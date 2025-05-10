"""
Xatolar bilan ishlash:
"""
# Xato yozilgan code:
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: '))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahslot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# To'g'irlangan code:
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: ')) # Bu yerda bir tirnoqdan ('') foydalanilgani uchun xato bergan

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot) # NameError: o'zgaruvchi nomi xato yozilgan. (To'girlandi)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  if len(mavjud_emas) == 1: # Agar mahsulot 1 ta bolsa "lar " qoshimchasini ishlatmaydi
     print("Do'konimizda quyidagi mahsulot yo'q:")
  else:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
  print(mahsulot)
else:
  if len(bor_mahsulotlar) == 1:
     print("Siz so'ragan quyidagi mahsulot do'konimizda bor:")
  else:
    print("Siz so'ragan quyudagi mahsulotlar do'konimizda bor:")
  for mahsulot in bor_mahsulotlar:
    print(mahsulot)