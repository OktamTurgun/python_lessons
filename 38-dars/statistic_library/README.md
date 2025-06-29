# 06-dars: Python `statistics` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`statistics`** kutubxonasi yordamida statistik hisob-kitoblar:
**o‘rtacha qiymat**, **moda**, **mediana**, **standart og‘ish** va **dispersiya** tushunchalarini o‘rganamiz.

---

## 📦 `statistics` kutubxonasini import qilish

```python
import statistics as stats
```

---

## 📊 Asosiy funksiyalar

| Funksiya               | Tavsif                                |
| ---------------------- | ------------------------------------- |
| `stats.mean(list)`     | O‘rtacha qiymat (arifmetik)           |
| `stats.median(list)`   | Mediana (markazdagi qiymat)           |
| `stats.mode(list)`     | Moda (eng ko‘p takrorlangan qiymat)   |
| `stats.stdev(list)`    | Standart og‘ish (standard deviation)  |
| `stats.variance(list)` | Dispersiya (o‘zgaruvchanlik darajasi) |

---

## 🧪 Amaliy misollar

```python
mahsulot_narxlari = [12000, 15000, 16000, 17000, 20000, 15000, 18000]

print("O‘rtacha:", stats.mean(mahsulot_narxlari))
print("Median:", stats.median(mahsulot_narxlari))
print("Moda:", stats.mode(mahsulot_narxlari))
print("Stdev:", stats.stdev(mahsulot_narxlari))
print("Dispersiya:", stats.variance(mahsulot_narxlari))
```

---

## 🎯 Amaliy mashq: Baholar tahlili

```python
baholar = [4, 5, 3, 4, 5, 5, 4, 3, 4, 5]
print("O‘rtacha baho:", stats.mean(baholar))
print("Moda baho:", stats.mode(baholar))
```

---

## 📝 Uyga vazifa

1. 10 ta tasodifiy sonlardan iborat ro‘yxat yarating va `mean`, `median`, `mode`, `stdev`, `variance` hisoblang.
2. Mahsulot narxlari bo‘yicha statistik tahlil qiling.
3. Talabalar baholari ro‘yxatini statistik jihatdan tahlil qiling.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/statistics.html](https://docs.python.org/3/library/statistics.html)
* Barcha funksiyalar float qiymat qaytaradi

---
