# 13-dars: Python `hashlib` kutubxonasi — Ma’lumotlarni xeshlash

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning `hashlib` kutubxonasi yordamida quyidagilarni o‘rganamiz:

* Matnlarni **md5** va **sha256** algoritmlari bilan xeshlash
* Parolni xavfsiz saqlash va tekshirish
* Xesh qiymatlarini solishtirish
* Xesh funksiyalarining xususiyatlari

---

## 📦 Import qilish

```python
import hashlib
```

---

## 🔐 Matnni xeshlash

```python
matn = "salom123"
md5_xesh = hashlib.md5(matn.encode()).hexdigest()
sha256_xesh = hashlib.sha256(matn.encode()).hexdigest()

print("MD5:", md5_xesh)
print("SHA256:", sha256_xesh)
```

* `.encode()` — matnni baytlarga aylantiradi
* `.hexdigest()` — xesh qiymatini 16lik satrga aylantiradi

---

## 📏 Xesh uzunliklari

```python
len(md5_xesh)      # 32 belgi
len(sha256_xesh)   # 64 belgi
```

---

## ✅ Parolni tekshirish

```python
# Oldindan xeshlangan parol
saqlangan = hashlib.sha256("admin123".encode()).hexdigest()

# Yangi kiritilgan parol
kiritilgan = input("Parolni kiriting: ")
if hashlib.sha256(kiritilgan.encode()).hexdigest() == saqlangan:
    print("✅ Parol to‘g‘ri")
else:
    print("❌ Noto‘g‘ri parol")
```

---

## ⚠️ Muhim eslatma

* Xesh funksiyasi **bir tomonlama**: xeshdan asl matnni qaytarib bo‘lmaydi
* `md5` — tez ishlaydi, lekin xavfsiz emas
* `sha256` — xavfsizroq, lekin sekinroq

---

## 📝 Uyga vazifa

1. O‘zingiz istalgan 3 ta so‘z yoki parolni `sha256` bilan xeshlang.
2. Foydalanuvchidan parol so‘rab, xeshlangan qiymat bilan solishtiring.
3. `md5` va `sha256` ni ishlatib, uzunlik va farqlarini kuzating.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/hashlib.html](https://docs.python.org/3/library/hashlib.html)
* Foydali: [https://passwordsgenerator.net/md5-hash-generator/](https://passwordsgenerator.net/md5-hash-generator/)

---
