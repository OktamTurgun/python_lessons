""" 
Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
"""
# print("Buyurtma qabul qilamiz.")
# maxsulotlar = []
# while True:
#   buyurtma = input("Maxsulotni kiriting: ")
#   maxsulotlar.append(buyurtma)
#   takrorlash = input("Yana maxsulot qo'shasizmi? (ha/yo'q) ").lower()
#   if takrorlash != 'ha':
#     break
# print("Maxsulotlar ro'yxati:")
# for maxsulot in maxsulotlar:
#   print(maxsulot.capitalize())

'''
Yuqoridagi tasturni optimallashgan korinishi
'''  
print("Buyurtma qabul qilamiz.")
products = {}
counter = 0  # Kiritilgan ma'lumotlar sonini hisoblash uchun
ask_threshold = 5  # Qanchadan keyin so'rov chiqarish

while True:
    # Maxsulotni so'rash
    while True:
        product = input("Sotin olmoqchi bolgan maxsulot nomini kiriting: ").strip()
        if product:  # Bo'sh emasligini tekshirish
            break
        print("Iltimos, maxsulot kiriting!")
    
    # Miqdorni so'rash
    while True:
        quantity_input = input(f"{product.title()}ning miqdorini kiriting: ").strip()
        if quantity_input.isdigit():  # Faqat raqam kiritilganligini tekshirish
            quantity = int(quantity_input)
            break
        print("Iltimos, to'g'ri son kiriting (faqat raqam)!")
    
    products[product] = quantity
    counter += 1
    
    # Har 5 ta kiritgandan keyin yoki birinchi marta so'rov chiqarish
    if counter % ask_threshold == 0:
        javob = input(f"{counter} ta maxsulot kiritdingiz. Yana qo'shasizmi? (ha/yo'q) ").lower()
        if javob != 'ha':
            break

print("\nBuyurtma qilingan maxsulotlar:")
for product, quantity in products.items():
    print(f"{product.title():<15}: {quantity}-kg")
  
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n += 1
#     if takrorlash != 'ha':
#         break
# print("Dostlringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
