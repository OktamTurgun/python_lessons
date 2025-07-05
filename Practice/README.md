# 🧮 OOP Practice: Hayot yo'li raqami (Numerologiya)

## 📌 Maqsad

Ushbu loyiha OOP (Obyektga yo‘naltirilgan dasturlash) bilimlarini mustahkamlash uchun amaliy mashq sifatida yozildi. Dastur foydalanuvchidan shaxsiy ma’lumotlarini olib, tug‘ilgan sanasiga asoslanib uning **hayot yo‘li raqamini (Life Path Number)** hisoblaydi va shu raqamga mos psixologik maslahat beradi.

---

## 📜 Vazifa

✅ Foydalanuvchidan quyidagi ma’lumotlarni olish:

* Ism
* Familiya
* Yosh
* Email
* Tug‘ilgan sana (YYYY-MM-DD)

✅ Shaxs uchun `Person` klassi yaratish va unga:

* `first_name`
* `last_name`
* `age`
* `email`
* `birth_day` (property sifatida)
  attributlarini berish.

✅ Metodlar:

* `get_info()` — barcha ma’lumotlarni chiroyli formatda chiqaradi.
* `get_life_path_number()` — tug‘ilgan sana asosida hayot yo‘li raqamini hisoblaydi.
* `get_info_by_number(number)` — raqamga mos psixologik maslahatni fayldan o‘qib beradi.

---

## 📁 Fayllar

* `practice_OOP.py` — asosiy kod.
* `life_path_info.txt` — har bir raqam uchun maslahatlar saqlangan matn fayli.

`life_path_info.txt` namunasi:

```
#1
Siz mustaqil va liderlik qobiliyatiga ega shaxssiz...

#2
Siz tinchliksevar va hamkorlikni yaxshi ko‘rasiz...
...
```

---

## 🚀 Ishga tushirish

1️⃣ `life_path_info.txt` faylini kerakli joyga (`practice_OOP.py` dagi yo‘lga) joylashtiring.
2️⃣ Terminalda quyidagi buyruqni bering:

```bash
python practice_OOP.py
```

3️⃣ Ma’lumotlarni kiriting va natijalarni o‘qing.

---

## 📋 Misol natija:

```
Ma'limotlaringizni kiriting:
Ismingiz: Jamshid
Familiyangiz: Karimov
Yoshingiz: 23
email: jamshid@example.com
Tug'ilgan sana: (yyyy-mm-dd): 2002-07-14

Shaxsiy ma'lumotlar:
First name: Jamshid
Last name: Karimov
Age: 23
Email: jamshid@example.com
Birth day: 14-07-2002

Hayot yo'li raqamingiz: 7

Siz uchun maxsus tavsiya:
Siz introspektiv va ruhiy o‘sishga intiluvchi shaxssiz...
```

---

## 📖 Talablar

* Python 3.9+
* Matn fayli (`life_path_info.txt`) mavjud bo‘lishi kerak.

---

## ✍️ Muallif

👤 Uktam Turgunov
📅 Sana: 2025-07-05

---

## ℹ️ Izohlar

* Fayl yo‘li platformaga mos tuzilganiga ishonch hosil qiling.
* `life_path_info.txt` ichida raqamlar # belgisi bilan boshlanishi va tavsiflar undan keyin yozilishi kerak.

---

## 🪄 Fikr va takliflar

Yaxshilash uchun:

* `life_path_info.txt` fayl yo‘lini dinamik qilish (config orqali yoki foydalanuvchidan so‘rash).
* Faylni faqat bir marta ochib, klass ichida keshlab qo‘yish.
* Testlar yozish va kodni modulga ajratish.
