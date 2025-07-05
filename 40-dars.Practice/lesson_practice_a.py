"""
📌 Mavzu: 1–100 ichidan tushib qolgan sonni topish
📦 Muallif: Uktam Turgunov
📅 Sana: 2025-07-05
🎯 Maqsad: 1–100 oralig‘idagi bitta tushib qolgan sonni topishning turli yechimlari.
"""

import random

print("\n============================")
print("🎓 Dars: Tushib qolgan sonni topish")
print("============================\n")


# ============================
# 🔷 Exercise 1 — sum() va range()
# ============================

def top_sum_range(sonlar):
    """
    1–100 yig‘indisidan berilgan sonlar yig‘indisini ayirib topish.
    """
    return sum(range(1, 101)) - sum(sonlar)


sonlar = list(range(1, 101))
tushib_qolgan_1 = sonlar.pop(random.randint(0, 99))
print(f"Exercise 1: Tushib qolgan son: {top_sum_range(sonlar)}")


# ============================
# 🔷 Exercise 2 — List comprehension + sum()
# ============================

def top_sum_listcomp(sonlar):
    """
    List comprehension yordamida bitta sonni olib tashlab,
    sum() bilan topish.
    """
    return sum(range(1, 101)) - sum(sonlar)


tushib_qolgan_2 = random.randint(1, 100)
sonlar = [x for x in range(1, 101) if x != tushib_qolgan_2]
print(f"Exercise 2: Tushib qolgan son: {top_sum_listcomp(sonlar)}")


# ============================
# 🔷 Exercise 3 — set yondashuvi
# ============================

def top_set_yondashuv(toliq_set, berilgan_set):
    """
    To‘plamlar yordamida farqni topish.
    """
    return (toliq_set - berilgan_set).pop()


n = 100
tushib_qolgan_3 = random.randint(1, n)
toliq_set = set(range(1, n+1))
berilgan_set = toliq_set - {tushib_qolgan_3}
print(
    f"Exercise 3: Tushib qolgan son: {top_set_yondashuv(toliq_set, berilgan_set)}")


# ============================
# 🔷 Exercise 4 — Gauss formulasi
# ============================

def top_gauss_formula(sonlar):
    """
    Gauss formulasi: n*(n+1)//2 – sum(sonlar)
    """
    n = 100
    toliq_yigindi = n * (n + 1) // 2
    return toliq_yigindi - sum(sonlar)


sonlar = list(range(1, 101))
tushib_qolgan_4 = sonlar.pop(random.randint(0, 99))
print(f"Exercise 4: Tushib qolgan son: {top_gauss_formula(sonlar)}")


# ============================
# 🔷 Exercise 5 — O‘yin (pop bilan)
# ============================

def oyin_pop(numbers):
    """
    O‘yin: random sonni yashirib, uni chiqarib tashlash.
    """
    x = numbers.pop(random.randint(0, len(numbers)-1))
    print(f"Exercise 5: Tushib qolgan son (oyin): {x}")
    return x


numbers = list(range(1, 101))
oyin_pop(numbers)

# ============================
# 🔷 Exercise 6 — XOR yondashuvi
# ============================


def top_xor_yondashuv(sonlar):
    """
    XOR yordamida tushib qolgan sonni topish.
    """
    xor_full = 0
    xor_partial = 0
    for i in range(1, 101):
        xor_full ^= i
    for s in sonlar:
        xor_partial ^= s
    return xor_full ^ xor_partial


sonlar = list(range(1, 101))
tushib_qolgan_6 = sonlar.pop(random.randint(0, 99))
print(f"Exercise 6: Tushib qolgan son (XOR): {top_xor_yondashuv(sonlar)}")

# ============================
# 🔷 Xulosa
# ============================

"""
✅ Qaysi yechim optimal?
— Kichik sonlar uchun: Exercise 4 (Gauss formulasi) eng oddiy va tezkor.
— Katta sonlar va noyoblikni tekshirish kerak bo‘lsa: Exercise 3 (set) qulay.
— O‘yin uchun: Exercise 5 (pop) yaxshi.

🚀 Tavsiya: 4-usulni asosiy sifatida ishlating!
"""
