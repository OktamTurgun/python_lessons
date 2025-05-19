"""
Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
"""

products = {
    "kartoshka": 8000,
    "piyoz": 5000,
    "sabzi": 3000,
    "go'sht": 85000,
    "sut": 9000,
    "non": 5000,
    "guruch": 27000,
    "makaron": 16000,
    "nohat": 22500,
    "yong'oq": 43000,
    "yog'": 21000,
    "olma": 16000,
    "banan": 22000,
    "uzum":33000,
    "shaftoli": 25000,
    "gilos": 28000,
    "sarimsoq_piyoz": 15000,
    "qalampir": 3000,
    "qoyun": 27000,
    "tarvuz": 20000,
    "xandalak": 24000, 
    "un": 11000,
    "suv": 6000,
    "grechka": 13000,
    "quruq_choy": 18000,
    "tuz": 5000
}
# buyurtmalar = ['non', 'olam', 'anjir', 'nok', 'suv', 'banan', 'tovuq-goshti']

# while buyurtmalar:
#   buyurtma = buyurtmalar.pop()
#   if buyurtma in products.keys():
#     narh = products[buyurtma]
#     print(f"{buyurtma.title()} - {narh} so'm")
#   else:   
#     print(f"Bizda {buyurtma.title()} qolmadi")
    
# Yuqoridagi dasturni foydalanuvchi tomonidan kiritilgan maxsulotlar bilan solishtirish
orders = []
print("Maxsulotlarni kiriting: (tugatish uchun 'stop' deb yozing) ")
while True:
  order = input("Maxsulot nomi: ").strip().lower()
  if order == 'stop':
    break
  orders.append(order)
  
if not orders:
  print("Siz hech qanday maxsulot buyurtma qilmadingiz!") 
else:
  print('\nBuyurtmalaringiz:')
  for order in orders:
    if order in products:
      print(f"{order.title()} - {products[order]} so'm")
    else:
      print(f"Afsuski, bizda {order.capitalize()} qolmadi!")

  

    
# buyurtmalar = []

# print("Mahsulotlarni kiriting (tugatish uchun 'stop' deb yozing):")
# while True:
#     buyurtma = input("Mahsulot nomi: ").lower()
#     if buyurtma == 'stop':
#         break
#     buyurtmalar.append(buyurtma)

# if not buyurtmalar:
#     print("Siz hech qanday mahsulot buyurtma bermadingiz!")
# else:
#     print("\nBuyurtmalaringiz:")
#     for buyurtma in buyurtmalar:
#         if buyurtma in products:
#             print(f"{buyurtma.title()} - {products[buyurtma]} so'm")
#         else:
#             print(f"Bizda {buyurtma.title()} qolmadi")  
  