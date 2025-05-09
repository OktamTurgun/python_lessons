"""
mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
"""

# products = [
#     "non",
#     "suv (1.5L shisha)",
#     "yog' (o'simlik yog'i)",
#     "tuxum",
#     "shokolad",
#     "kartoshka",
#     "olma",
#     "guruch",
#     "go'shti",
#     "sut",
#     "un",
#     "choy",
#     "shakar",
# ]
# cart = []
# for n in range(5):
#   cart.append(input(f"Savatga {n+1}-maxsulotni qo'shing: ").strip().lower())

# if cart:
#   for product in cart:
#     if product in products:
#       print(f"{product.title()} do'konimizda bor")
#     else:
#       print(f"{product.title()} do'konimizda yo'q")
# else:
#   print("Savatingiz bo'sh!")
    
"""function yordamida yuqoridagi kodni yozing."""
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
def chek_products_in_store():
  cart = []
  empty_response = 0 # bo'sh javoblar sonini xisoblash

  for i in range(5):
      product = input(f"Savatga {i+1}-maxsulotni qo'shing: ").strip().lower()
      if product:  # Faqat bo'sh bo'lmagan stringlarni qo'shamiz
          cart.append(product)
      else:
         empty_response += 1

  if empty_response == 5:
    print("Savatingiz bo'sh!")

    retry = input("Yana urunib ko'rasizmi? (ha/yo'q): ").lower()
    if retry == "ha":
      chek_products_in_store()
    return
  
  for product in cart:
    message = f"{product.title()} do'konimizda " + ("bor" if product in products else "yo'q")
    print(message)

chek_products_in_store()
