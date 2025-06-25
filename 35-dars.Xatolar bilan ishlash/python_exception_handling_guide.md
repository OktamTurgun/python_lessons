# 🧠 Python'da Xatolar bilan Ishlash (Exception Handling)

Python dasturlash tilida xatolar (exceptions) bilan ishlash muhim mavzulardan biridir. Quyidagi hujjatda `try-except`, `else`, `finally`, `raise`, `if-else`, `while` kabi vositalar qanday ishlashi, ularning maqsadi va farqlari misollar hamda jadval bilan tushuntiriladi.

---

## 🔎 Umumiy Jadval: Xatolarni Boshqarish Usullari

| Usul        | Maqsad                                   | Xato bo'ladimi? | Dastur to'xtaydimi? |
|-------------|-------------------------------------------|------------------|----------------------|
| try-except  | Xatoni ushlash                           | ✅ Bo'ladi       | ❌ To'xtamaydi       |
| if-else     | Xatoni oldini olish                      | ❌ Bo'lmaydi     | ❌ To'xtamaydi       |
| while       | To'g'ri ma'lumot olinmaguncha so'rash    | ❌ Bo'lmaydi     | ❌ To'xtamaydi       |
| raise       | Qo'l bilan xato chiqarish                | ✅ Bo'ladi       | ✅ To'xtaydi         |
| else        | try ichidagi kod muvaffiyatli bo‘lsa     | ❌ Bo'lmaydi     | ❌ To'xtamaydi       |
| finally     | Har doim bajariladi                      | ❓ Farqi yo'q     | ❌ To'xtamaydi       |

---

## 📘 Har bir usulga misollar bilan izoh

### 1. `try-except` — Xatoni ushlash
```python
try:
    son = int(input("Butun son kiriting: "))
except ValueError:
    print("Faqat butun son kiriting!")
```
> 🎯 Maqsad: xato yuz berganda, dasturni to‘xtatmasdan uni ushlash.

---

### 2. `if-else` — Xatoni oldini olish
```python
son = input("Butun son kiriting: ")
if son.isdigit():
    son = int(son)
    print(f"Kiritilgan son: {son}")
else:
    print("Iltimos, son kiriting!")
```
> 🎯 Maqsad: xato bo‘lishi mumkin bo‘lgan holatni oldindan tekshirish.

---

### 3. `while` — To‘g‘ri kiritilmaguncha davom etish
```python
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        print(f"Siz {yosh} yoshdasiz.")
        break
    else:
        print("Iltimos, raqam kiriting.")
```
> 🎯 Maqsad: foydalanuvchi to‘g‘ri qiymat kiritmaguncha so‘rashda davom etish.

---

### 4. `raise` — Maxsus xatoni qo‘l bilan chiqarish
```python
yosh = int(input("Yosh kiriting: "))
if yosh < 0:
    raise ValueError("Yosh manfiy bo'lishi mumkin emas!")
```
> 🎯 Maqsad: kerakli holat buzilganda o‘zimiz xato chiqaramiz.

---

### 5. `else` — try muvaffaqiyatli bo‘lsa bajariladi
```python
try:
    son = int(input("Son kiriting: "))
except ValueError:
    print("Xato! Son emas.")
else:
    print(f"Siz kiritgan son: {son}")
```
> 🎯 Maqsad: `try` blokida xato bo‘lmasa, `else` bajariladi.

---

### 6. `finally` — Har doim bajariladi
```python
try:
    f = open("fayl.txt")
except FileNotFoundError:
    print("Fayl topilmadi.")
finally:
    print("Dastur tugadi.")
```
> 🎯 Maqsad: nima bo‘lishidan qat’iy nazar kod bajariladi.

---

## ✅ Yakuniy Tavsiyalar

- Har doim `try-except` blokidan foydalaning **foydalanuvchidan ma'lumot olish**, **fayl ochish**, **tarmoqdan ma'lumot olish** kabi noaniq holatlarda.
- Xato bo‘lishi mumkin bo‘lgan joyni **oldindan tahlil qilib**, uni `try-except` bilan o‘rab oling.
- Iloji bo‘lsa, xatolarni `if-else` yoki `while` orqali **oldini olishga harakat qiling**.
- Katta loyihalarda `raise` orqali kerakli joyda maxsus xatolarni chiqarish orqali **dastur oqimini nazorat qilish** mumkin.
- `finally` blokida resurslarni (fayl, tarmoq, ulanish) **yopish va tozalash ishlarini** bajaring.

---

## 🧾 Xulosa:

- `try-except` — xatolarni ushlash
- `if-else` — xatolarni oldini olish
- `while` — foydalanuvchidan to‘g‘ri ma’lumot olinmaguncha davom ettirish
- `raise` — maxsus xatoni o‘zingiz chiqarasiz
- `else` — `try` muvaffaqiyatli tugasa ishlaydi
- `finally` — har doim ishlaydi

Bu vositalarni birgalikda ishlatish orqali mustahkam, foydalanuvchi xatolariga bardoshli dasturlar yaratish mumkin.