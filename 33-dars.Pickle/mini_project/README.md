# 📘 Student Manager — mini loyiha

Ushbu loyiha Python'da `pickle` yordamida talabalarni faylga saqlash, ularni ko'rish va o'chirish imkonini beruvchi oddiy dasturiy modeldir. CLI (Command Line Interface) menyu asosida boshqariladi.

## 🧱 Texnologiyalar

* Python 3.x
* `pickle` moduli
* Konsol menyu
* Faylga saqlash: `students.pkl`

---

## 🔧 Dastur imkoniyatlari

### ✅ Talaba qo'shish

Foydalanuvchidan ism, familiya, yosh kiritiladi. Obyekt sifatida `students.pkl` fayliga yoziladi.

### 📋 Talabalar ro‘yxatini ko‘rish

Binary fayldan ma'lumotlar o'qiladi va konsolga chiqariladi. Bo‘sh bo‘lsa, ogohlantirish chiqariladi.

### ❌ Talabani o‘chirish

Ro‘yxatdan indeks bo‘yicha talabani tanlab o‘chirish mumkin. Saqlangan fayl avtomatik yangilanadi.

### 🔚 Chiqish

CLI menyudan chiqish.

---

## 📂 Fayllar tuzilmasi

```
├── student_manager.py   # Asosiy Python dasturi
├── students.pkl         # Pickle fayli (dastur ishga tushgandan keyin yaratiladi)
├── README.md            # Loyihaga izoh va hujjat
```

---

## 🚀 Ishga tushirish

```bash
python student_manager.py
```

---

## 🛡️ Xavfsizlik eslatmasi

Pickle moduli faqat ishonchli fayllar bilan ishlaganda xavfsiz. Internetdan yuklab olingan `.pkl` fayllarni `load()` qilish xavfli bo‘lishi mumkin.

👉 Batafsil yo‘riqnoma: [Pickle xavfsizlik qo‘llanmasi](./Pickle%20Xavfsizlik%20Yo%20Riqnoma.md)


---

## 📌 Muallif: Uktam Turgunov

© 2025 — Python amaliy loyihalar
