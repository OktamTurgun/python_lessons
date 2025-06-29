# 08-dars: Python `itertools` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`itertools`** kutubxonasi yordamida:

* Kombinatorika (product, permutations, combinations)
* Yig‘indi va guruhlash (accumulate, groupby)
* Cheksiz generatorlar (count, cycle, repeat)
  bilan ishlashni o‘rganamiz.

---

## 📦 Import qilish

```python
import itertools as it
```

---

## 🔁 Kombinatorika funksiyalari

### 🔹 `product()` — kartezian ko‘paytma

```python
it.product(['A', 'B'], [1, 2])
# ('A', 1), ('A', 2), ('B', 1), ('B', 2)
```

### 🔹 `permutations()` — tartibli joylashuv

```python
it.permutations(['A', 'B', 'C'], 2)
# ('A', 'B'), ('A', 'C'), ...
```

### 🔹 `combinations()` — tartibsiz juftliklar

```python
it.combinations(['A', 'B', 'C'], 2)
# ('A', 'B'), ('A', 'C'), ('B', 'C')
```

---

## ➕ `accumulate()` — yig‘indi yoki funksional jamlovchi

```python
it.accumulate([1, 2, 3, 4])  # 1, 3, 6, 10
```

---

## 🧩 `groupby()` — elementlarni guruhlash

```python
mahsulotlar.sort(key=lambda x: x['turi'])
for turi, guruh in it.groupby(mahsulotlar, key=lambda x: x['turi']):
    print(turi, list(guruh))
```

---

## ♾️ Cheksiz generatorlar

### 🔁 `count(start)`

```python
for i in it.count(10):
    print(i)
    if i >= 13: break
```

### 🔁 `cycle(iterable)`

```python
for val in it.cycle(['A', 'B']):
    print(val)
    break after 4 iterations
```

### 🔁 `repeat(value, times)`

```python
for x in it.repeat('Hi', 3):
    print(x)
```

---

## 📝 Uyga vazifa

1. 3 ta elementdan iborat ro‘yxat uchun barcha `permutations` va `combinations` larni chiqaring.
2. `accumulate()` yordamida sonlar ro‘yxati bo‘yicha yig‘indilarni toping.
3. `groupby()` orqali mahsulotlar yoki talabalarni turiga qarab guruhlang.
4. `count`, `cycle`, `repeat` funksiyalarining ishlashini amalda ko‘rib chiqing.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/itertools.html](https://docs.python.org/3/library/itertools.html)
* Har bir generator `for` yoki `next()` yordamida chaqiriladi.

---

