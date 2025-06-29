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
re.sub(r"foydalanuvchi", "Anvar", s)
# Natija: "Salom, Anvar!"
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

  ## 💡 Taklif va yaxshilashlar

  ### Xatolik va kamchiliklar

  - `re.match()` va `re.fullmatch()` funksiyalari natijada `True` yoki `False` emas, balki `Match` obyekti yoki `None` qaytaradi. Kodlarda `bool()` bilan tekshirish yoki `.group()` ishlatish aniqroq bo‘ladi.
  - `re.match()` misolida natijani `bool()` yoki `.group()` bilan ko‘rsatish mumkin.
  - `re.fullmatch()` misolida ham natijani `bool()` bilan ko‘rsatish yaxshiroq.
  - Ba’zi kodlarda natijalar izoh sifatida aniq ko‘rsatilmagan.

  ### Qo‘shimcha takliflar

  - Regex qisqa belgilarini to‘liqroq va tartibliroq ro‘yxat qilish:
    - `\s` — bo‘sh joy (space, tab, newline)
    - `.` — istalgan bitta belgi (yangi qatordan tashqari)
    - `^` — satr boshi
    - `$` — satr oxiri
    - `[abc]` — a, b yoki c harflaridan biri
    - `[^abc]` — a, b, c dan tashqari harflar
  - Har bir funksiya uchun qisqa tavsif va natija misolini alohida ajratib ko‘rsatish.
  - Amaliy mashq va uyga vazifalarni yanada aniqroq va bosqichma-bosqich yozish.
  - Regex andozalarini sinab ko‘rish uchun qisqa misollar kiritish.
  - `re.compile()` funksiyasi haqida qisqacha ma’lumot qo‘shish mumkin.

  ### Qo‘shimcha manbalar

  - [Python Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
  - [Pythex — Python regex tester](https://pythex.org/)

  ### Yaxshilangan qisqa belgilar ro‘yxati

  - `\d` — raqamlar (0-9)
  - `\w` — harf yoki raqam
  - `\s` — bo‘sh joy belgisi
  - `.` — istalgan bitta belgi (yangi qatordan tashqari)
  - `^` — satr boshi
  - `$` — satr oxiri
  - `+`, `*`, `?` — takrorlash belgilar
  - `[abc]` — a, b yoki c harflaridan biri
  - `[^abc]` — a, b, c dan tashqari harflar

  ---

  **Qayerga joylashtirish tavsiyasi:**  
  Ushbu bo‘limni fayl oxirida, asosiy dars va qo‘shimcha manbalar tugagach, ya’ni `$SELECTION_PLACEHOLDER$` joyiga joylashtirish eng to‘g‘ri va chiroyli bo‘ladi. Chunki bu taklif va yaxshilashlar asosiy darsdan keyin, o‘quvchiga qo‘shimcha ma’lumot va rivojlanish uchun yo‘nalish beradi.
---