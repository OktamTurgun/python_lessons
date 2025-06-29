# 09-dars: Python `pathlib` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`pathlib`** kutubxonasi yordamida zamonaviy va obyektga asoslangan **fayl yo‘llari bilan ishlash** ko‘nikmalarini o‘rganamiz.

---

## 📦 Import qilish

```python
from pathlib import Path
```

---

## 📂 Path obyektlari yaratish

```python
path1 = Path("example.txt")
path2 = Path.home() / "Documents" / "data.txt"
```

* `Path()` — fayl yoki papka yo‘li yaratadi
* `/` operatori yordamida yo‘lni birlashtirish mumkin
* `Path.home()` — foydalanuvchi katalogi (C:/Users/username)

---

## ✅ Fayl va papka mavjudligini tekshirish

```python
path.exists()    # Fayl mavjudmi?
path.is_file()   # Faylmi?
path.is_dir()    # Papkami?
```

---

## 📖 Faylni o‘qish va yozish

```python
path.write_text("Matn")      # Matn yozish
matn = path.read_text()      # Matn o‘qish
```

---

## 🧱 Fayl haqida ma’lumot

```python
path.name     # Fayl nomi
path.suffix   # Kengaytmasi (.txt)
path.parent   # Ota papkasi
```

---

## 🔍 Papkada fayl qidirish

```python
for fayl in Path(".").glob("*.txt"):
    print(fayl.name)
```

➡️ `glob()` yordamida muayyan kengaytmali fayllarni topish mumkin.

---

## 📝 Uyga vazifa

1. `Path.home()` yordamida o‘z papkangizdagi `myfile.txt` faylini yarating.
2. Faylga biror matn yozing va uni qayta o‘qing.
3. `.suffix`, `.name`, `.parent` orqali fayl haqida ma’lumot chiqaring.
4. Joriy papkadagi barcha `.py` fayllarni chop eting.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/pathlib.html](https://docs.python.org/3/library/pathlib.html)
* `pathlib` — `os.path` va `open()` funksiyalarining zamonaviy alternativi.

---
