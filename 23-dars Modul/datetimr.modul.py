'''
Pythonda datetime moduli bilan ishkash uchun misollar:
'''
from datetime import datetime, date, time, timedelta 
import locale # Lokalizatsiya uchun

# 1. Hozirgi vaqtni olish
hozir = datetime.now()
print(f"1. Hozirgi vaqt: {hozir}")

# 2. Faqat sanani olish
bugun = date.today()
print(f"\n2. Bugungi sana: {bugun}")

# 3. Maxsus vaqt yaratish
sana = date(2023, 12, 31)
vaqt = time(23, 59, 59)
maxsus_vaqt = datetime.combine(sana, vaqt)
print(f"\n3. Yangi yil arafasi: {maxsus_vaqt}")

# 4. Sana formatlari
print("\n4. Sana formatlari:")
print(f"ISO format: {hozir.isoformat()}")
print(f"Strftime bilan: {hozir.strftime('%A, %d-%B, %Y-yil %H:%M')}")

# 5. Lokalizatsiya (o'zbekcha)
print("\n5. O'zbekcha sana ko'rinishi:")
locale.setlocale(locale.LC_TIME, 'uz_UZ.UTF-8')  # Linux uchun
# locale.setlocale(locale.LC_TIME, 'uz')  # Windows uchun
print(hozir.strftime("%A, %d %B %Y-yil"))

# 6. Sana hisoblash
print("\n6. Sana hisoblash:")
ertaga = bugun + timedelta(days=1)
print(f"Ertangi sana: {ertaga}")

bir_hafta_oldin = hozir - timedelta(weeks=1)
print(f"Bir hafta oldin: {bir_hafta_oldin}")

# 7. Sana farqlari
print("\n7. Sana farqlari:")
tugilgan_sana = date(1990, 5, 15)
yosh = bugun - tugilgan_sana
print(f"Siz {yosh.days // 365} yoshdasiz")

# 8. Vaqtni parse qilish
print("\n8. Stringdan sana o'qish:")
sana_matni = "2023-08-15 14:30:00"
parsed_sana = datetime.strptime(sana_matni, "%Y-%m-%d %H:%M:%S")
print(f"O'qilgan sana: {parsed_sana}")

# 9. Unix timestamp
print("\n9. Unix vaqt:")
timestamp = datetime.timestamp(hozir)
print(f"Joriy timestamp: {timestamp}")
print(f"Timestampdan sana: {datetime.fromtimestamp(timestamp)}")

# 10. Vaqt zonalari (timezone)
print("\n10. Vaqt zonalari:")
from datetime import timezone
utc_vaqt = datetime.now(timezone.utc)
print(f"UTC vaqt: {utc_vaqt}")
print(f"Local vaqt: {utc_vaqt.astimezone()}")

# 11. Ish vaqtini hisoblash
print("\n11. Ish vaqtini hisoblash:")
boshlanish = datetime(2023, 1, 1)
tugash = datetime(2023, 12, 31)
farq = tugash - boshlanish
print(f"2023 yildagi kunlar soni: {farq.days}")

# 12. Sana solishtirish
print("\n12. Sana solishtirish:")
sana1 = date(2023, 1, 1)
sana2 = date(2023, 12, 31)
print(f"{sana1} > {sana2} = {sana1 > sana2}")

# 13. Kabisa yilini tekshirish
def is_leap_year(year):
    """Kabisa yilini tekshiradi"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print("\n13. Kabisa yili tekshiruvi:")
print(f"2024 yil kabisa yilimi? {is_leap_year(2024)}")

# 14. Oy oxirgi kuni
from calendar import monthrange

def last_day_of_month(year, month):
    """Oyning oxirgi kunini qaytaradi"""
    return monthrange(year, month)[1]

print("\n14. Oy oxirgi kuni:")
print(f"Fevral 2023 oxirgi kuni: {last_day_of_month(2023, 2)}")
print(f"Fevral 2024 oxirgi kuni: {last_day_of_month(2024, 2)}")