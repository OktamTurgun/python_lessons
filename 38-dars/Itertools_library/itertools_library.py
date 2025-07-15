"""
08-dars: Python itertools kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda itertools kutubxonasi bilan quyidagilarni o‘rganamiz:
 - product, permutations, combinations
 - accumulate, groupby
 - count, cycle, repeat
"""

import itertools as it
import operator

# product - barcha kombinatsiyalar
ranglar = ['qizil', 'yashil']
shakllar = ['doira', 'kvadrat']
print("product:")
for p in it.product(ranglar, shakllar):
    print(p)

# permutations - tartiblangan variantlar
harflar = ['A', 'B', 'C']
print("permutations:")
for p in it.permutations(harflar, 2):
    print(p)

# combinations - tartibsiz variantlar
print("combinations:")
for c in it.combinations(harflar, 2):
    print(c)

# accumulate - yig‘indilar
sonlar = [1, 2, 3, 4]
print("accumulate:")
for a in it.accumulate(sonlar):
    print(a)

# groupby - guruhlash
mahsulotlar = [
    {'nom': 'olma', 'turi': 'meva'},
    {'nom': 'sabzi', 'turi': 'sabzavot'},
    {'nom': 'banan', 'turi': 'meva'},
    {'nom': 'kartoshka', 'turi': 'sabzavot'},
]
mahsulotlar.sort(key=lambda x: x['turi'])
print("groupby:")
for turi, guruh in it.groupby(mahsulotlar, key=lambda x: x['turi']):
    print(turi, list(guruh))

# count, cycle, repeat (cheksiz generatorlar)
print("count:")
for i in it.count(10):
    print(i)
    if i >= 13:
        break

print("cycle:")
i = 0
for val in it.cycle(['A', 'B']):
    print(val)
    i += 1
    if i == 4:
        break

print("repeat:")
for r in it.repeat('Hello', 3):
    print(r)

# # Amaliy mashqlar:

# 1. product yordamida 3 ta ro'yxatdan barcha kombinatsiyalarni toping
print("product (3 ta ro'yxat):")
for p in it.product([1, 2], ['a', 'b'], ['x', 'y']):
    print(p)

# 2. permutations yordamida 'ABCD' harflarining barcha 3 ta harfli tartiblangan variantlarini chiqaring
print("permutations (3 ta harf):")
for p in it.permutations('ABCD', 3):
    print(''.join(p))

# 3. combinations yordamida 5 ta son ichidan 2 tasini tanlash variantlarini chiqaring
print("combinations (2 ta son):")
for c in it.combinations([10, 20, 30, 40, 50], 2):
    print(c)

# 4. accumulate yordamida max funksiyasi bilan eng katta qiymatlarni topib boring
print("accumulate (max):")
for a in it.accumulate([3, 1, 4, 2, 5], func=max):
    print(a)

# 5. groupby yordamida so'zlarni uzunligiga qarab guruhlang
sozlar = ['olma', 'banan', 'gilos', 'nok', 'ananas', 'olcha']
sozlar.sort(key=len)
print("groupby (uzunlik):")
for uzunlik, guruh in it.groupby(sozlar, key=len):
    print(f"Uzunligi {uzunlik}: {list(guruh)}")

# 6. count yordamida 5 tadan boshlab 2 qadam bilan 5 ta son chiqaring
print("count (boshlanish=5, qadam=2):")
for i, val in zip(range(5), it.count(5, 2)):
    print(val)

# 7. cycle yordamida 'AB' ni 6 marta aylantiring
print("cycle (6 marta):")
for i, val in zip(range(6), it.cycle('AB')):
    print(val)

# 8. repeat yordamida 'Python' so'zini 4 marta chiqaring
print("repeat ('Python', 4):")
for r in it.repeat('Python', 4):
    print(r)
