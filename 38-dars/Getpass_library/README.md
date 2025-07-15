# 11-dars: Python `getpass` kutubxonasi bilan ishlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda `getpass` kutubxonasi yordamida **foydalanuvchidan yashirin parol kiritishni** o‘rganamiz.

---

## 📦 Import qilish

```python
import getpass
```

---

## 🧪 Misol: oddiy login

```python
foydalanuvchi = input("Foydalanuvchi nomi: ")
parol = getpass.getpass("Parol: ")

if parol == "123456":
    print(f"Xush kelibsiz, {foydalanuvchi}!")
else:
    print("⚠️ Noto‘g‘ri parol!")
```

---

## 📌 Nima uchun `getpass`?

| Oddiy input     | getpass                |
| --------------- | ---------------------- |
| Parol ko‘rinadi | Parol ko‘rinmaydi      |
| Xavfsiz emas    | Xavfsiz terminal uchun |

---

## ⚠️ Muhim ogohlantirish

* `getpass.getpass()` faqat **terminal/konsol** muhitida ishlaydi
* **Jupyter Notebook**, **GUI** va **VS Code interactive** oynasida xatolik beradi

---

## 📝 Uyga vazifa

1. Login-parol tekshiradigan kichik tizim yarating (kamida 2 foydalanuvchi bilan)
2. Parolni ikki marta kiritib, tasdiqlovchi tizim yarating

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/getpass.html](https://docs.python.org/3/library/getpass.html)
* Foydalanuvchi ismi va parolini xavfsiz olish uchun ishlatiladi

---

🚀 Keyingi dars: `re` kutubxonasi — matnni izlash, almashtirish va tekshirish uchun regular expressions
