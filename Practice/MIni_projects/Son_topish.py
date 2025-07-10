"""
Mavzu: Practice. Mini projects
Muallif: Uktam Turgunov
Sana: 2025-07-10
"""
import random


def son_topish():
    print("🎲 1–100 oralig‘ida son o‘yladim, topa olasizmi?")
    target = random.randint(1, 100)
    urinishlar = 0

    while True:
        urinishlar += 1
        taxmin = int(input("Son kiriting: "))
        if taxmin < target:
            print("🔼 Kattaroq son kiriting.")
        elif taxmin > target:
            print("🔽 Kamroq son kiriting.")
        else:
            print(
                f"🎉 Topdingiz! {urinishlar} ta urinishda {target} sonini topdingiz!")
            break


son_topish()
