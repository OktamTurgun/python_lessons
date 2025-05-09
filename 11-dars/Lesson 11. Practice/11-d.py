"""
mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
"""

products = [
    "non",
    "suv (1.5L shisha)",
    "yog' (o'simlik yog'i)",
    "tuxum",
    "shokolad",
    "kartoshka",
    "olma",
    "guruch",
    "go'shti",
    "sut",
    "un",
    "choy",
    "shakar",
]
cart = []
for n in range(5):
  cart.append(input(f"Savatga {n+1}-maxsulotni qo'shing: ").strip().lower())

if cart:
  for product in cart:
    if product in products:
      print(f"{product.title()} do'konimizda bor")
    else:
      print(f"{product.title()} do'konimizda yo'q")
else:
  print("Savatingiz bo'sh!")
    
