# 03-dars: Python `datetime` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`datetime`** kutubxonasi yordamida **sana** va **vaqt** bilan ishlashni o‘rganamiz.
Bu kutubxona sana yaratish, vaqt farqlarini hisoblash va formatlash uchun juda foydali.

---

## 📦 `datetime` kutubxonasini import qilish

```python
from datetime import datetime, date, time, timedelta
```

---

## 🗓️ Asosiy funksiyalar

### 🕒 Hozirgi sana-vaqt

```python
now = datetime.now()
print(now)                # 2025-06-28 11:23:45.123456
print(now.year)           # 2025
date.today()              # faqat sana (YYYY-MM-DD)
```

### 🧱 Sana yoki vaqt yaratish

```python
bayram = date(2025, 12, 31)
vaqt = time(14, 30, 0)     # 14:30:00
```

### 🧮 Sana farqlari: `timedelta`

```python
d1 = date(2025, 12, 31)
d2 = date.today()
farq = d1 - d2
print(farq.days)           # Qolgan kunlar soni
```

### 🔁 Sana formatlash: `strftime()`

```python
now.strftime("%d-%m-%Y")   # Masalan: '28-06-2025'
now.strftime("%H:%M")     # Masalan: '11:25'
```

### 🔁 Matndan sanaga: `strptime()`

```python
sana = datetime.strptime("1990-06-15", "%Y-%m-%d")
```

---

## 🎯 Amaliy mashq: Yosh hisoblovchi funksiya

```python
def yosh_hisobla(tugilgan_kun):
    tugilgan_sana = datetime.strptime(tugilgan_kun, "%Y-%m-%d")
    hozir = datetime.now()
    farq = hozir - tugilgan_sana
    return farq.days // 365

print(yosh_hisobla("1990-06-15"))  # 34
```

---

## 📝 Uyga vazifa

1. Foydalanuvchidan tug‘ilgan sanasini olib, yoshini hisoblang.
2. Yangi yilgacha necha kun qolganini aniqlang.
3. Hozirgi vaqtni `soat:dakika` ko‘rinishida chiqaring.
4. 7 kun oldingi sanani chop eting.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)
* `%d`, `%m`, `%Y`, `%H`, `%M` — formatlash kodlari

---

🚀 Keyingi dars: `os` kutubxonasi bilan fayl va papkalar bilan ishlash
