# 02-dars: Python `random` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`random`** kutubxonasi yordamida **tasodifiy sonlar** va **elementlar** bilan ishlashni o‘rganamiz. Bu kutubxona testlar, simulyatsiyalar, shifrlash va o‘yinlar yaratishda keng qo‘llaniladi.

---

## 📦 `random` kutubxonasini import qilish

```python
import random
```

---

## 🔢 Asosiy funksiyalar

### 🎲 Butun va haqiqiy sonlar

| Funksiya               | Tavsif                           |
| ---------------------- | -------------------------------- |
| `random.randint(a, b)` | a dan b gacha butun son tanlaydi |
| `random.uniform(a, b)` | a dan b gacha float son tanlaydi |
| `random.random()`      | 0.0 dan 1.0 gacha float son      |

### 🎯 Ro'yxatlar bilan ishlash

| Funksiya                 | Tavsif                                      |
| ------------------------ | ------------------------------------------- |
| `random.choice(list)`    | Ro‘yxatdan bitta tasodifiy element tanlaydi |
| `random.shuffle(list)`   | Ro‘yxatni joyidan aralashtiradi             |
| `random.sample(list, k)` | Ro‘yxatdan k ta elementni tanlab beradi     |

---

## 🧪 Amaliy misollar

```python
random.randint(1, 10)         # 1 dan 10 gacha butun son
random.uniform(0, 5)          # 0.0 - 5.0 oralig'ida float
random.choice(['olma', 'gilos'])  # "olma" yoki "gilos"
```

---

## 🔐 Mini loyiha: Tasodifiy parol generator

```python
import random, string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

print(generate_password())  # Masalan: 'aK7dX8sL'
```

---

## 📝 Uyga vazifa

1. Foydalanuvchidan `n` sonini olib, 1 dan n gacha tasodifiy son chiqaring.
2. Mevalar ro'yxatini aralashtirib yangi tartibda ekranga chiqaring.
3. 6 ta tasodifiy son (1 dan 49 gacha) chiqadigan mini lotoreya dasturi yozing.
4. 10 ta elementdan iborat ro‘yhatdan 3 tasini tanlab chiqaruvchi kod yozing.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)
* `random.seed(x)` — Natijalarni takrorlash uchun (testlar uchun)

---

🚀 Keyingi dars: `datetime` kutubxonasi bilan sana-vaqtlar bilan ishlash
