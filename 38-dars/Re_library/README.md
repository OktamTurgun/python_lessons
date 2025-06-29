# 12-dars: Python `re` kutubxonasi bilan ishlash (Regular Expressions)

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`re` kutubxonasi** yordamida matndan andoza asosida izlash, tekshirish va o‘zgartirishni o‘rganamiz:

* `findall()` — barcha mosliklarni topish
* `search()` — birinchi moslikni qidirish
* `match()` — matn boshidan tekshirish
* `sub()` — so‘z yoki raqamni almashtirish
* `fullmatch()` — to‘liq moslik tekshiruvi

---

## 📦 Import qilish

```python
import re
```

---

## 🔍 `findall()` — barcha mos elementlarni topish

```python
matn = "2 ta olma, 3 ta banan, 1 ta shaftoli"
re.findall(r"\d+", matn)
# Natija: ['2', '3', '1']
```

---

## 🔍 `search()` — birinchi moslikni topish

```python
matn = "Email: info@example.com"
mos = re.search(r"[\w.-]+@[\w.-]+\.\w+", matn)
mos.group()  # info@example.com
```

---

## 🔎 `match()` — matn boshidan tekshirish

```python
s = "Python3"
re.match(r"Python", s)  # Boshi "Python" bo‘lsa True
```

---

## ✂️ `sub()` — matnni almashtirish

```python
s = "Salom, foydalanuvchi!"
re.sub(r"foydalanuvchi", "Uktam", s)
# Natija: "Salom, Uktam!"
```

---

## ✅ `fullmatch()` — to‘liq moslik

```python
re.fullmatch(r"\d+", "12345")  # True
re.fullmatch(r"\d+", "12a45")  # False
```

---

## 🧪 Amaliy mashq

```python
def raqammi(s):
    return bool(re.fullmatch(r"\d+", s))

print(raqammi("12345"))  # True
print(raqammi("12a45"))  # False
```

---

## 📝 Uyga vazifa

1. Berilgan matndan barcha raqamlarni ajrating.
2. Email manzilni ajratib oling.
3. `re.sub()` yordamida so‘zlarni o‘zgartiring.
4. Telefon raqam: `\+998\d{9}` regex andozasini yozing.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
* Regex generator: [https://regex101.com](https://regex101.com)
* Regex qisqa belgilar:

  * `\d` — raqamlar (0-9)
  * `\w` — harf yoki raqam
  * `+`, `*`, `?` — takrorlash belgilar

---