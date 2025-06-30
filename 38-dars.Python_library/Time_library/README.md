# 14-dars: Python `time` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning `time` kutubxonasi yordamida vaqt bilan ishlash, kutish, vaqt o‘lchash va taymer funksiyalarini o‘rganamiz:

* `time.time()` — joriy vaqt (timestamp)
* `time.ctime()` — o‘qiladigan vaqt
* `time.sleep()` — kutish
* Taymer, progress indikator, vaqtni o‘lchash

---

## 📦 Import qilish

```python
import time
```

---

## 🕰️ Asosiy funksiyalar

```python
print(time.time())       # Vaqt (sekundlarda) — 1970-yildan boshlab
print(time.ctime())      # Hozirgi vaqt matn ko‘rinishida
```

---

## ⏱️ Kutish funksiyasi

```python
print("3 soniya kuting...")
time.sleep(3)
print("Davom etamiz!")
```

---

## 📏 Operatsiya vaqtini o‘lchash

```python
t0 = time.time()
for i in range(1_000_000):
    i ** 2
print("Vaqt:", round(time.time() - t0, 4), "sekund")
```

---

## ⏳ Taymer funksiyasi

```python
def taymer(sekund):
    while sekund:
        print(f"Qolgan vaqt: {sekund} s", end="\r")
        time.sleep(1)
        sekund -= 1
    print("\n⏰ Vaqt tugadi!")

taymer(5)
```

---

## 🧪 Qo‘shimcha amaliy mashqlar

### 📢 1. Rejalashtirilgan xabar chiqarish

```python
print("5 soniyadan so‘ng xabar...")
time.sleep(5)
print("📢 Endi xabar chiqarildi!")
```

### 📊 2. Progress indikator (10 soniyalik)

```python
def progress_bar(sekund):
    for i in range(sekund):
        print(f"[{i+1}/{sekund}] Kuting...", end="\r")
        time.sleep(1)
    print("\n✅ Tayyor!")

progress_bar(10)
```

### 🔁 3. Har 2 sekundda salom chiqarish

```python
for i in range(5):
    print(f"{i+1}. Salom!")
    time.sleep(2)
```

---

## 📝 Uyga vazifa

1. 10 soniyalik taymer yozing
2. Har 3 soniyada so‘z chiqaradigan funksiya yozing
3. Vaqt o‘lchash uchun test dasturi yarating

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html)
* `sleep()` — threading, asyncio kutubxonalarida ham mavjud

---
