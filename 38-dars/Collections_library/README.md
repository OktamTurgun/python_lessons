# 07-dars: Python `collections` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`collections`** kutubxonasidagi muhim sinflar:
**`Counter`**, **`defaultdict`**, **`namedtuple`**, **`deque`** bilan ishlashni o‘rganamiz.

---

## 📦 Import qilish

```python
from collections import Counter, defaultdict, namedtuple, deque
```

---

## 🧮 Counter — elementlarni sanash

```python
so‘zlar = ['olma', 'banan', 'olma', 'anor', 'banan', 'olma']
hisob = Counter(so‘zlar)
print(hisob)                 # {'olma': 3, 'banan': 2, 'anor': 1}
print(hisob.most_common(1))  # [('olma', 3)]
```

---

## 🧰 defaultdict — standart qiymatli lug‘at

```python
yoshlar = defaultdict(lambda: 18)
yoshlar['Ali'] = 20
print(yoshlar['Hasan'])  # 18 (standart qiymat)
```

---

## 📋 namedtuple — strukturaviy obyekt

```python
Talaba = namedtuple('Talaba', ['ism', 'yosh', 'kurs'])
t1 = Talaba('Dilshod', 21, 3)
print(t1.ism)   # Dilshod
print(t1.kurs)  # 3
```

➡️ Obyekt sifatida ishlatish mumkin, lekin tuple tezligida ishlaydi.

---

## 🔄 deque — ikki taraflama navbat

```python
navbat = deque(['Ali', 'Vali'])
navbat.append('Hasan')         # oxiriga
navbat.appendleft('Sardor')    # boshiga
navbat.pop()                   # oxiridan
navbat.popleft()               # boshidan
print(navbat)
```

➡️ `deque` — listdan tezroq navbatlar uchun.

---

## 📝 Uyga vazifa

1. So‘zlar ro‘yxatidan `Counter` yordamida eng ko‘p uchraganini toping.
2. `defaultdict` yordamida har bir sinf uchun o‘quvchilar ro‘yxatini shakllantiring.
3. `namedtuple` orqali `Kitob` tuzilmasi yarating (`nomi`, `muallif`, `narx`).
4. `deque` navbatga 5 kishi qo‘shib, 2 tasini chiqarib ko‘ring.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/collections.html](https://docs.python.org/3/library/collections.html)

---
