# 15-dars: Python `shutil` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning `shutil` kutubxonasi yordamida **fayllar va papkalar bilan** ishlashni o‘rganamiz:

* Faylni nusxalash (oddiy va metadata bilan)
* Faylni boshqa joyga ko‘chirish
* Fayl va papkalarni o‘chirish
* Papkani `.zip` formatga arxivlash
* Real amaliy holatlar: backup, tiklash

---

## 📦 Import qilish

```python
import shutil
import os
```

---

## 📁 Faylni nusxalash

```python
shutil.copy("data.txt", "data_backup.txt")         # oddiy
shutil.copy2("data.txt", "data_full_backup.txt")    # metadata bilan
```

---

## 📤 Faylni ko‘chirish

```python
shutil.move("data_backup.txt", "backup/data_backup.txt")
```

---

## 🗑️ Fayl yoki papkani o‘chirish

```python
os.remove("file.txt")                 # Fayl o‘chirish
shutil.rmtree("papka_nomi")          # Papkani ichidagilari bilan birga o‘chirish
```

---

## 📦 Arxivlash

```python
shutil.make_archive("my_backup", "zip", "data_folder")
# Natija: my_backup.zip
```

---

## 🧪 Amaliy mashqlar

### 1. Yangi papka yaratib, faylni unga ko‘chirish

```python
os.mkdir("archive_folder")
shutil.copy("data.txt", "archive_folder/data_copy.txt")
```

### 2. Faylni vaqtincha zaxiralab, qayta tiklash

```python
shutil.copy("data.txt", "temp_backup.txt")
os.remove("data.txt")
shutil.copy("temp_backup.txt", "data.txt")
os.remove("temp_backup.txt")
```

---

## 📝 Uyga vazifa

1. `.docx` yoki `.png` faylni nusxalab boshqa papkaga ko‘chiring.
2. Berilgan papkani `.zip` formatga arxivlang.
3. Faylni vaqtincha o‘chirib, qayta tiklaydigan funksiya yozing.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/shutil.html](https://docs.python.org/3/library/shutil.html)
* `os.path.exists()` — fayl yoki papka mavjudligini tekshirish

---
