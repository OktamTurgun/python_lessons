from collections import Counter

"""
Mavzu: Practice. Matndagi unli harflar sonini hisoblash
Muallif: Uktam Turgunov
Sana: 2025-07-07
Vazifa:
Matn ichidagi unli harflarni sanab, ularning sonini qaytaradigan funksiya yozing.
(O‘zbekcha unlilar: a, e, i, o, u, o‘)
"""

# Exercise: 1


def unli_sana(matn):
    """Matndagi unli harflar sonini hisoblaydi"""
    unli = 'aeiouöüóàèìòù'
    sanash = sum(1 for harf in matn.lower() if harf in unli)
    return sanash


print(unli_sana("Bugun o'zbekistonda ajoyib kun!"))

# # Exercise: 2: filter va lambda yordamida


def unli_sana_v3(matn):
    """Matndagi unli harflar sonini hisoblaydi (filter/lambda yordamida)"""
    unli = set('aeiouöüóàèìòù')
    return len(list(filter(lambda x: x in unli, matn.lower())))


print(unli_sana_v3("Bugun o'zbekistonda ajoyib kun!"))

# # Exercise: 3: collections.Counter yordamida


def unli_sana_v4(matn):
    """Matndagi unli harflar sonini hisoblaydi (Counter yordamida)"""
    unli = set('aeiouöüóàèìòù')
    counter = Counter(matn.lower())
    return sum(counter[harf] for harf in unli)


print(unli_sana_v4("Bugun o'zbekistonda ajoyib kun!"))

# Alternativ 4: map va sum yordamida


def unli_sana_v5(matn):
    """Matndagi unli harflar sonini hisoblaydi (map yordamida)"""
    unli = set('aeiouöüóàèìòù')
    return sum(map(lambda x: x in unli, matn.lower()))


print(unli_sana_v5("Bugun o'zbekistonda ajoyib kun!"))
