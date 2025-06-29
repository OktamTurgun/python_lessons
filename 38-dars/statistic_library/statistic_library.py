"""
06-dars: Python statistics kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda statistics kutubxonasi yordamida statistik hisob-kitoblarni o‘rganamiz:
 - mean (o‘rtacha)
 - median (mediana)
 - mode (moda)
 - stdev (standart og‘ish)
 - variance (dispersiya)
"""

import statistics as stats

mahsulot_narxlari = [12000, 15000, 16000, 17000, 20000, 15000, 18000]

# O‘rtacha qiymat
print("O‘rtacha narx:", stats.mean(mahsulot_narxlari))

# Mediana
print("Median narx:", stats.median(mahsulot_narxlari))

# Moda (eng ko‘p takrorlangan qiymat)
print("Moda:", stats.mode(mahsulot_narxlari))

# Standart og‘ish (standard deviation)
print("Standart og‘ish:", stats.stdev(mahsulot_narxlari))

# Dispersiya (variance)
print("Dispersiya:", stats.variance(mahsulot_narxlari))

# Amaliy mashq: Baholar ustida statistik hisob
baholar = [4, 5, 3, 4, 5, 5, 4, 3, 4, 5]
print("Baholar o‘rtachasi:", stats.mean(baholar))
print("Eng ko‘p baho (moda):", stats.mode(baholar))
# Amaliy mashq: Ijtimoiy tarmoqlardagi postlar ustida statistik hisob
post_likes = [100, 150, 200, 150, 300, 250, 200, 150]
print("Postlar o‘rtacha like soni:", stats.mean(post_likes))
