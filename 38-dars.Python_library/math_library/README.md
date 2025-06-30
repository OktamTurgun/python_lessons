# 01-dars: Python `math` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python dasturlash tilida eng ko‘p ishlatiladigan **`math`** kutubxonasi bilan ishlashni o‘rganamiz. Bu kutubxona matematik hisob-kitoblar uchun kerakli funksiyalarni taqdim etadi.

---

## 📦 `math` kutubxonasini import qilish

```python
import math
```

---

## 🧮 Asosiy funksiyalar va konstantalar

### 📌 Konstantalar

| Funktsiya | Tavsif                   |
| --------- | ------------------------ |
| `math.pi` | Pi (π ≈ 3.14159)         |
| `math.e`  | Euler soni (e ≈ 2.71828) |

### ✅ Daraja, ildiz, modul

| Funktsiya           | Tavsif                |
| ------------------- | --------------------- |
| `math.sqrt(x)`      | Kvadrat ildiz         |
| `math.pow(x, y)`    | x^y                   |
| `math.fabs(x)`      | Mutlaq qiymat (modul) |
| `math.factorial(n)` | n! faktoriali         |

### 🔢 Yaxlitlash

| Funktsiya       | Tavsif                          |
| --------------- | ------------------------------- |
| `math.floor(x)` | Pastga yaxlitlash (butun son)   |
| `math.ceil(x)`  | Yuqoriga yaxlitlash (butun son) |
| `math.trunc(x)` | Butun qismini kesish            |

### 🔺 Trigonometrik funksiyalar

*(Burchaklar radianlarda ishlatiladi)*

| Funktsiya     | Tavsif  |
| ------------- | ------- |
| `math.sin(x)` | Sinus   |
| `math.cos(x)` | Kosinus |
| `math.tan(x)` | Tangens |

### 📈 Logarifmlar va eksponentlar

| Funktsiya           | Tavsif       |
| ------------------- | ------------ |
| `math.log(x, base)` | log₍base₎(x) |
| `math.log10(x)`     | log₁₀(x)     |
| `math.exp(x)`       | e^x          |

---

## 🧪 Amaliy misollar

```python
print(math.sqrt(25))           # 5.0
print(math.pow(3, 4))          # 81.0
print(math.sin(math.pi/2))    # 1.0
print(math.log(8, 2))          # 3.0
```

---

## 🎯 Amaliy mashq

**Masala:** Radiusi berilgan doiraning yuzini hisoblang.

```python
def doira_yuzasi(r):
    return math.pi * math.pow(r, 2)

print(doira_yuzasi(7))  # 153.93...
```

---

## 📝 Uyga vazifa

1. Foydalanuvchidan son olib uning ildizi, kvadrati va faktorialini hisoblang.
2. Burchak berilganda uning `sin`, `cos`, `tan` qiymatlarini chiqaring.
3. Quyidagi ifodani hisoblang:
   **z = √(a² + b²)**  (a va b foydalanuvchidan olinadi)

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)
* Radian vs gradus: `math.radians(degree)` — gradusni radianlarga o‘tkazadi

---
