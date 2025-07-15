# 19-dars: Python `pprint` kutubxonasi — Chiroyli va tartibli chiqarish

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Katta hajmdagi ma’lumotlar tuzilmalari (list, dict, JSON) odatiy `print()` orqali chiqarilganda juda chalkash va uzun ko‘rinishda bo‘ladi. Shu sababli `pprint` (pretty print) kutubxonasi yordamida ma’lumotlarni **tartibli**, **o‘qish oson** va **chiroyli** ko‘rinishda chiqarishni o‘rganamiz.

---

## 📦 pprint kutubxonasini import qilish

`pprint` modulini ikki usulda import qilish mumkin:

### 1-usul: To‘liq modulni import qilish

```python
import pprint
pprint.pprint(obj)  # pprint modulining pprint() funksiyasini chaqiryapmiz
```

### 2-usul: Faqat funksiyani import qilish

```python
from pprint import pprint
pprint(obj)  # to‘g‘ridan-to‘g‘ri chaqirish mumkin
```

🔎 Har ikki usul **bir xil** natijani beradi. Farqi faqat yozilish uslubidadir.

---

## 🧪 Asosiy funksiyalar

| Funksiya       | Tushuntirish                               |
| -------------- | ------------------------------------------ |
| `pprint(obj)`  | Ekranga chiroyli formatda chiqaradi        |
| `pformat(obj)` | Ob’yektni chiroyli matn sifatida qaytaradi |

---

## 🧾 Amaliy misollar

### 📌 1. Oddiy `dict` obyektini chiroyli chiqarish

```python
mahsulotlar = {
    "meva": ["olma", "banan"],
    "ichimlik": {"suv": ["oddiy", "gazli"]}
}
import pprint
pprint.pprint(mahsulotlar)
```

### 📌 2. `pformat()` yordamida matn sifatida saqlash

```python
formatted = pprint.pformat(mahsulotlar)
print(formatted)
```

### 📌 3. JSON ma’lumotlar bilan ishlash

```python
import json
json_data = '{"ism": "Ali", "yosh": 25, "manzil": {"shahar": "Toshkent"}}'
data = json.loads(json_data)
pprint.pprint(data)
```

### 📌 4. Ichma-ich ro‘yxatlar

```python
murakkab = [
    {"id": 1, "status": "ok"},
    {"id": 2, "status": "error", "details": {"code": 400}}
]
pprint.pprint(murakkab)
```

### 📌 5. Ko‘p qatlamli API natijasi

```python
api_response = {
    "user": {"id": 1001, "roles": ["admin"]},
    "status": "success"
}
pprint.pprint(api_response)
```

---

## 🤔 Nega `pprint.pprint()` ikki marta yoziladi?

Aslida bu ikki marta yozilayotgandek ko‘rinsa ham, **bu faqat modul va funksiya nomining bir xil bo‘lishidan**. Quyidagicha farqlanadi:

| Import usuli                | Chaqarish usuli      | Tavsiya        |
| --------------------------- | -------------------- | -------------- |
| `import pprint`             | `pprint.pprint(obj)` | Modulli yozish |
| `from pprint import pprint` | `pprint(obj)`        | Qisqaroq usul  |

Ikkalasi ham to‘g‘ri ishlaydi — faqat stil va foydalanish uslubiga bog‘liq.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [pprint — Python Docs](https://docs.python.org/3/library/pprint.html)
* Foydali: log yozish, katta JSON’larni test qilish, debug qilishda ishlatiladi

---

✅ Endi siz pprint yordamida kodlaringizni yanada chiroyli va tushunarli ko‘rinishda chiqarishni bilasiz!
