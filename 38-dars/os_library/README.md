# 04-dars: Python `os` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`os`** kutubxonasi yordamida **fayl va papkalar bilan ishlash**,
**yo‘llarni boshqarish**, va **tizim haqidagi ma’lumotlarni olish**ni o‘rganamiz.

---

## 📦 `os` kutubxonasini import qilish

```python
import os
```

---

## 📁 Asosiy funksiyalar

### 📂 Papka bilan ishlash

| Funksiya                      | Tavsif                            |
| ----------------------------- | --------------------------------- |
| `os.getcwd()`                 | Joriy ishchi katalogni qaytaradi  |
| `os.listdir(path)`            | Fayllar ro‘yxatini beradi         |
| `os.makedirs(path, exist_ok)` | Papkalarni zanjir holida yaratadi |

### 📄 Fayl/papka mavjudligini tekshirish

| Funksiya               | Tavsif                             |
| ---------------------- | ---------------------------------- |
| `os.path.exists(path)` | Fayl/papka mavjudligini tekshiradi |
| `os.path.isfile(path)` | Fayl ekanligini tekshiradi         |
| `os.path.isdir(path)`  | Papka ekanligini tekshiradi        |

### 🔗 Yo‘llar bilan ishlash

```python
os.path.join("data", "file.txt")
```

➡️ Bu usul turli tizimlarda (Windows/Linux) mos yo‘l yaratadi.

### 🖥️ Tizim ma’lumotlari

```python
os.name          # nt (Windows), posix (Linux, Mac)
```

---

## 🔐 Amaliy mashq: Fayl mavjudligini tekshirish

```python
def check_or_create(filename):
    if os.path.exists(filename):
        print(f"{filename} mavjud")
    else:
        with open(filename, "w") as f:
            f.write("Yangi fayl yaratildi")
        print(f"{filename} yaratildi")
```

---

## 📝 Uyga vazifa

1. `data/new_folder` nomli papka yarating.
2. Shu papkaga `info.txt` degan fayl yaratib ichiga yozing.
3. `os.path` yordamida fayl yoki papka ekanligini tekshiring.
4. Joriy ishchi katalogdagi fayllar ro‘yxatini chiqaring.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)
* `os.remove(file)` — fayl o‘chirish
* `os.rmdir(folder)` — papka o‘chirish

---
