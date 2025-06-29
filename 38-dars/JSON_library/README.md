# 10-dars: Python `json` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`json`** kutubxonasi yordamida quyidagilarni o‘rganamiz:

* Python obyektlarini JSON formatiga aylantirish
* JSON matnni Python obyektiga aylantirish
* JSON faylga yozish va fayldan o‘qish

---

## 📦 Import qilish

```python
import json
```

---

## 🔁 Python obyekt → JSON matn (`dumps`)

```python
mahsulot = {
    "nom": "Olma",
    "narx": 12000,
    "mavjud": True
}
json_matn = json.dumps(mahsulot, indent=4, ensure_ascii=False)
print(json_matn)
```

* `indent=4` — chiroyli formatda chiqaradi
* `ensure_ascii=False` — o‘zbekcha harflarni to‘g‘ri saqlaydi

---

## 🔁 JSON matn → Python obyekt (`loads`)

```python
python_dict = json.loads(json_matn)
print(python_dict["nom"])
```

---

## 📁 JSON faylga yozish (`dump`) va o‘qish (`load`)

```python
with open("mahsulot.json", "w", encoding="utf-8") as f:
    json.dump(mahsulot, f, indent=4, ensure_ascii=False)

with open("mahsulot.json", "r", encoding="utf-8") as f:
    malumot = json.load(f)
    print(malumot)
```

---

## 🧪 Amaliy mashq: Talabalar ro‘yxatini saqlash

```python
talabalar = [
    {"ism": "Ali", "yosh": 20},
    {"ism": "Laylo", "yosh": 21}
]

# Faylga yozish
with open("talabalar.json", "w", encoding="utf-8") as f:
    json.dump(talabalar, f, indent=2, ensure_ascii=False)

# Fayldan o‘qish
with open("talabalar.json", "r", encoding="utf-8") as f:
    ro‘yxat = json.load(f)
    print(ro‘yxat)
```

---

## 📝 Uyga vazifa

1. O‘zingiz haqingizdagi `dict` ma’lumotni JSON faylga yozing va o‘qing.
2. 5 ta mahsulotdan iborat ro‘yxatni JSON faylga saqlang.
3. `indent=2`, `ensure_ascii=False` parametrlarining farqini amalda ko‘rib chiqing.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)
* JSON — JavaScript Object Notation: brauzerlar, API'lar, fayllar bilan almashishda eng keng tarqalgan format.

---
