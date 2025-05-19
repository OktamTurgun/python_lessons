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
        product = input("Sotib olmoqchi bo'lgan maxsulot nomini kiriting: ").strip()
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
    
""" Yuqoridagi dastur yana o'zgartirildi """
print("Buyurtma qabul qilamiz.")
products = {}
categories = {
    'meva': {'olma', 'banan', 'nok', 'apelsin', 'mandarin', 'uzum', 'anor', 'shaftoli', 'gilos'},
    'sabzavot': {'kartoshka', 'sabzi', 'piyoz', 'baqlajon', 'qalampir', 'bodring', 'pomidor'},
    'gosht': {'mol', 'qoy', 'tovuq', 'baliq', 'go\'sht'},
    'sut': {'sut', 'yog\'', 'qatiq', 'smetana', 'tvorog'},
    'don': {'guruch', 'loviya', 'no\'xat', 'mosh', 'bug\'doy'},
    'ichimlik': {'suv', 'limonad', 'cola', 'fanta', 'pepsi', 'choy', 'kofe'},
    'boshqa': set()
}

measure_units = {
    'meva': 'kg',
    'sabzavot': 'kg',
    'gosht': 'kg',
    'sut': 'litr',
    'don': 'kg',
    'ichimlik': 'litr',
    'boshqa': 'dona'
}

counter = 0
ask_threshold = 5

while True:
    while True:
        product = input("Sotib olmoqchi bo'lgan mahsulot nomini kiriting: ").strip().lower()
        if product:
            break
        print("Iltimos, mahsulot kiriting!")
    
    # Mahsulot turini aniqlash
    category = None
    for cat, items in categories.items():
        if product in items:
            category = cat
            break
    if category is None:
        category = 'boshqa'
        categories['boshqa'].add(product)  # Yangi mahsulotni "boshqa" turiga qo'shamiz
    
    unit = measure_units[category]
    
    while True:
        quantity_input = input(f"{product.title()}ning miqdorini kiriting ({unit}): ").strip()
        if quantity_input.replace('.', '', 1).isdigit():  # O'nlik sonlar uchun
            quantity = float(quantity_input) if '.' in quantity_input else int(quantity_input)
            break
        print(f"Iltimos, to'g'ri son kiriting (faqat raqam, {unit})!")
    
    products[product] = {'quantity': quantity, 'unit': unit, 'category': category}
    counter += 1
    
    if counter % ask_threshold == 0:
        javob = input(f"{counter} ta mahsulot kiritdingiz. Yana qo'shasizmi? (ha/yo'q) ").lower()
        if javob != 'ha':
            break

print("\nBuyurtma qilingan mahsulotlar:")
print("{:<20} {:<10} {:<10} {:<15}".format("Nomi", "Miqdori", "Birlik", "Kategoriya"))
print("-" * 55)
for product, data in products.items():
    print("{:<20} {:<10} {:<10} {:<15}".format(
        product.title(),
        data['quantity'],
        data['unit'],
        category.title()
    ))

# Qo'shimcha statistikalar
print("\nStatistika:")
category_stats = {}
for data in products.values():
    cat = data['category']
    if cat not in category_stats:
        category_stats[cat] = 0
    category_stats[cat] += data['quantity']

print("Kategoriya bo'yicha jami miqdorlar:")
for cat, total in category_stats.items():
    print(f"{cat.title():<15}: {total} {measure_units[cat]}")
  