"""
e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
"""
products = {}
ishora = True
while ishora:
  product = input("Maxsulot nomini kiriting: ").strip()
  price = input(f"{product.title()}nimg narhini kiriting: ")
  products[product] = int(price)
  javob = input("Yana maxsulot qo'shasizmi? (ha/yo'q) ")
  if javob == "yo'q":
    ishora = False
    
for product, price in products.items():
  print(f"{product.title():<10}: {price} so'm")
  
