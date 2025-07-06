"""
Mavzu: Practice. Basic & Syntaxni mustaxkamlash
Muallif: Uktam Turgunov
Sana: 2025-07-06
Vazifa:
1 dan 100 gacha bo‘lgan sonlardan 3 ga ham, 5 ga ham bo‘linadiganlarini chiqarish.
"""
numbers = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        numbers.append(i)
print(f"1dan 100 gacha sonlardan 3 va 5 ga bolinadigan sonlar royxati: \n"
      f"{numbers}")
