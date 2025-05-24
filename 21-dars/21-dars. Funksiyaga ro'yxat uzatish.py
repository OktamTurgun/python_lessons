"""
Created on Fri May 23 20:35:42 2025

21-dars. Funksiyaga ro'yxat uzatish ((Passing Lists to Functions in Python))

@author: uktam
"""
def bahola(ismlar):
    # Talabalar ro'yxatini qabul qilib, baholarni so'raydi
    # va natijani lug'at ko'rinishida qaytaradi
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input((f"Talaba {ism.title()}ning bahosini kiriting: "))
        baholar[ism] = int(baho)
    return baholar
talabalar = ['ali', 'vali', 'olim', 'hasan', 'husan']
baholar = bahola(talabalar[:])

print("Talabalrning baholari:")
for ism, baho in baholar.items():
    print(f"{ism.title()}ning bahosi: {baho}")
    
# print(baholar)

''''''
def royxatni_korsat(royxat):
    # Ro'yxatni qabul qilib, har bir elementini chiqaradi
    for element in royxat:
        print(element)
        
fruits = ['apple', 'banana', 'pear', 'peach']
royxatni_korsat(fruits)

'''
Ro'yxatni o'zgartirish
Funksiya ichida ro'yxatga o'zgartirish kiritilsa, asl ro'yxat ham o'zgaradi
(chunki ro'yxat mutable va reference orqali uzatiladi).
'''

def qoshish(royxat):
    # Ro'yxatga yangi element qo'shadi
    # va asl ro'yxatni o'zgartiradi
    royxat.append("new element")
    
numbers = [1, 2, 3]
qoshish(numbers)
print(numbers)

# Eslatma: Funksiya ro'yxatning nusxasini emas, balki havolasini (reference) oladi!

'''
Ro'yxatni nusxalash (Avoiding Side Effects)
Agar asl ro'yxat o'zgarishini istamasangiz, nusxa olishingiz kerak.
'''
def qoshish_yangi(royxat):
    # Ro'yxatga yangi element qo'shadi
    # va yangi ro'yxatni qaytaradi
    yangi_royxat = royxat.copy()
    yangi_royxat.append("new element")
    return yangi_royxat
eski_royxat = [1, 2, 3]
yangi_royxat = qoshish_yangi(eski_royxat)
print(eski_royxat) # [1, 2, 3]
print(yangi_royxat) # [1, 2, 3, 'new element']

'''
Ro'yxatni parametr sifatida ishlatish.
Funksiyaga bir nechta ro'yxat uzatish mumkin.
'''
def birlashtir(list1, list2):   
    """Ikkita ro'yxatni birlashtiradi va yangi ro'yxatni qaytaradi"""
    return list1 + list2

a = ['a', 'b', 'c']
b = ['e', 'f', 'g']
c = a[:] + b[:]
print(c)                # ['a', 'b', 'c', 'e', 'f', 'g']
print(birlashtir(a, b)) # ['a', 'b', 'c', 'e', 'f', 'g']

'''
Ro'yxat mutable ekanligi: Funksiya ichida ro'yxat
 o'zgartirilsa, asl ro'yxat ham o'zgaradi.

Nusxa olish: Agar asl ro'yxatni saqlab qolish kerak bo'lsa,
 .copy() yoki royxat[:] dan foydalaning.

Argument sifatida uzatish: Ro'yxat nomini to'g'ri berish
 (funksiya parametri bilan mos kelishi kerak).
'''

''''''
# Ro'yxat lementlarini kvadratga oshirish
def kvadrat(list):
    """Ro'yxatdagi har bir elementni kvadratga oshiradi va asl ro'yxatni o'zgartiradi"""
    for i in range(len(list)):
        #list[i] **= 2 # shortcut for list[i] = list[i] ** 2
        list[i] = list[i] ** 2

nums = [1, 2, 3]
kvadrat(nums)
print(nums) # [1, 4, 9]

''''''
# Ro'yxatdagi juft sonlarni ajratish
def juft_sanash(royxat):
    """Ro'yxatdagi juft sonlarni ajratadi va yangi ro'yxatni qaytaradi"""
    juftlar = []
    for son in royxat:
        if son % 2 == 0:
            juftlar.append(son)
    return juftlar

print(juft_sanash([1, 2, 3, 4, 5, 6])) # [2, 4, 6]

''''''
def add(royxat):
    """Ro'yxatdagi har bir elementga 5 qo'shadi va yangi ro'yxatni qaytaradi"""
    # royxatni o'zgartirmaydi
    new_numbers = []
    for x in royxat:
        new_numbers.append(x + 5)
    return new_numbers

numbers = [10, 20, 30]
new_numbers = add(numbers)
print(f"Eski ro'yaxat: {numbers}")
print(f"Yangi ro'yaxat: {new_numbers}")

''''''
def add_five(royxat):
    """Ro'yxatdagi har bir elementga 5 qo'shadi va yangi ro'yxatni qaytaradi"""
    # royxatni o'zgartirmaydi
    return [x + 5 for x in numbers]

numbers = [10, 20, 30]
new_numbers = add_five(numbers)
print(f"Eski ro'yxat: {numbers}")
print(f"Yangi ro'yxat: {new_numbers}")

''''''
def add_five(royxat):   
    """Ro'yxatdagi har bir elementga 5 qo'shadi va yangi ro'yxatni qaytaradi"""
    # royxatni o'zgartirmaydi   
    yangi = royxat.copy()  # asl ro'yxatdan nusxa
    for i in range(len(yangi)):
        yangi[i] += 5
    return yangi

numbers = [10, 20, 30]
print(add_five(numbers))      # [15, 25, 35]
print(numbers)                # [10, 20, 30]
        
































