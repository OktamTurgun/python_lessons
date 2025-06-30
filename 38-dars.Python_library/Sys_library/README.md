# 05-dars: Python `sys` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning **`sys`** kutubxonasi yordamida **komanda qatori argumentlari**,
**standart chiqishlar**, **modul yo‘llari** va **chiqish kodi** bilan ishlashni o‘rganamiz.

---

## 📦 `sys` kutubxonasini import qilish

```python
import sys
```

---

## 🧰 Asosiy funksiyalar

### 🧾 Komanda qatori argumentlari

```python
print(sys.argv)   # ['fayl.py', 'arg1', 'arg2', ...]
```

➡️ Bu orqali siz terminaldan berilgan argumentlarni olishingiz mumkin.

### 🧪 Python versiyasi

```python
print(sys.version)   # Python versiyasi haqida ma’lumot
```

### 🔄 Dasturni yakunlash

```python
sys.exit("Xatolik yoki yakun sababli chiqish")
```

### 📤 Standart chiqish va xatolik

```python
sys.stdout.write("Oddiy chiqish")
sys.stderr.write("Xatolik chiqishi")
```

### 📁 Modul yo‘llari ro‘yxati

```python
for path in sys.path:
    print(path)
```

➡️ Python `import` vaqtida qayerlardan modul izlaydi.

---

## 🎯 Amaliy mashq: Ism orqali salomlashish

```python
def salom_ber():
    if len(sys.argv) > 1:
        ism = sys.argv[1]
        print(f"Salom, {ism}!")
    else:
        print("Foydalanuvchi ismi berilmadi.")
```

---

## 📝 Uyga vazifa

1. Terminaldan ism va yosh argumentini olib ularni chiqaring.
   `python script.py Ali 30` → `Salom, Ali! Siz 30 yoshdasiz.`
2. Foydalanuvchi ismi berilmasa `sys.exit()` yordamida chiqish xabarini bering.
3. Python versiyasini tekshirib chiqaring va chop eting.
4. `sys.path` ro‘yxatidan o‘zingiz yaratgan papkani qo‘shing.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)
* `sys.modules` — yuklangan modullar

---

🚀 Keyingi dars: `statistics` kutubxonasi — o‘rtacha, median, dispersiya hisoblash
