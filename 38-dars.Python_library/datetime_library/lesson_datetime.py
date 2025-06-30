"""
Created on Sat Jun 28 10:03:45 2025. Sana: 2025-06-28

38-dars. PYTHON KUTUBXONASI (02-dars: Python datetime kutubxonasi)

Muallif: Uktam Turgunov

Ushbu darsda datetime kutubxonasi yordamida sana va vaqtlar bilan ishlashni o'rganamiz:
 - Hozirgi sana-vaqt
 - Maxsus sanalar yaratish
 - Formatlash (strftime)
 - Sana farqlari (timedelta)
"""

from datetime import datetime, date, time, timedelta
import datetime as dt

# datetime()

hozirgi_vaqt = dt.datetime.now()
# print(hozirgi_vaqt)

# # Sanani ajratib olish
# print(hozirgi_vaqt.date())

# # Vaqtni ajratib olish
# print(hozirgi_vaqt.time())

# # Soatni ajratib olish
# print(hozirgi_vaqt.hour)

# # Daqiqadni ajratib olish
# print(hozirgi_vaqt.minute)

# # Soniyani ajratib olish
# print(hozirgi_vaqt.second)

# # date()
bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")

ertaga = dt.date(2025, 6, 29)
# print(f"Ertangi sana: {ertaga}")

# # time()
hozir = dt.datetime.now()
# print(f"Xozirgi vaqt: {hozir}")
vaqtHozir = hozir.time()
# print(f"Xozirgi soat: {vaqtHozir}")
vaqtKeyin = dt.time(15, 10, 20)
# print(f"4 soatdan keyin soat: {vaqtKeyin}")

# # Sanalar orasida farq
bugun = dt.date.today()
tugilganKun = dt.date(2025, 7, 5)
farq = tugilganKun - bugun
# print(farq)
# print(f"Mustafoning tug'ilgan kuniga {farq.days} kun qoldi.")

# # soatlar orasidagi farq
hozir = dt.datetime.now()
birthday = dt.datetime(2025, 7, 5, 15, 10, 00)
farq = birthday - hozir
soniyalar = farq.seconds
daqiqalar = int(soniyalar / 60)
soatlar = int(daqiqalar / 60)
print(
    f"Mustafoning tug'ilgan kuniga {farq.days} kun, {soatlar} soat, {daqiqalar} daqiqa, {soniyalar} soniya qoldi.")

# Hozirgi vaqt va sana
hozir = datetime.now()
print("Hozirgi sana-vaqt:", hozir)
print("Yil:", hozir.year)
print("Oy:", hozir.month)
print("Kun:", hozir.day)
print("Soat:", hozir.hour)
print("Daqiqa:", hozir.minute)

# Faqat sana yoki vaqt
bugun = date.today()
print("Bugungi sana:", bugun)

vaqt = time(14, 30, 15)
print("Maxsus vaqt:", vaqt)

# Yangi sana yaratish
bayram = date(2025, 12, 31)
print("Bayram kuni:", bayram)

# Sana formatlash
# "%d-%m-%Y %H:%M" - formatlash
print("Formatlangan sana:", hozir.strftime("%d-%m-%Y %H:%M"))

# Sana farqi (timedelta)
farq = bayram - bugun
print("Yil oxirigacha qolgan kunlar:", farq.days)

# Amaliy mashq: Tug'ilgan kundan beri qancha vaqt o'tdi


def yosh_hisobla(tugilgan_kun):
    tugilgan_sana = datetime.strptime(tugilgan_kun, "%Y-%m-%d")
    hozir = datetime.now()
    farq = hozir - tugilgan_sana
    return farq.days // 365


print("Yosh (1990-06-15):", yosh_hisobla("1990-06-15"))
