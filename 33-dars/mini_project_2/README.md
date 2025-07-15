# 🛒 Mahsulot Manager (Python + Pickle)

**Mahsulot Manager** — bu oddiy konsol dasturi bo‘lib, foydalanuvchiga mahsulotlar ro‘yxatini saqlash, ko‘rish, qo‘shish va o‘chirish imkonini beradi.

Ma’lumotlar `pickle` kutubxonasi yordamida `mahsulotlar.pkl` fayliga saqlanadi.

---

## 📦 Dastur imkoniyatlari:

* ✅ Mahsulotlar ro‘yxatini ko‘rish
* ➕ Yangi mahsulot qo‘shish (nomi va narxi bilan)
* ❌ Mahsulotni nomi bo‘yicha o‘chirish
* 📁 Fayl mavjud bo‘lmasa, avtomatik yaratish
* 💾 Ma’lumotlarni `pickle` orqali xavfsiz saqlash

---

## 📁 Fayl tuzilmasi

```
├── mahsulot_manager.py        # Asosiy menyu va CRUD funksiyalar
├── mahsulotlar.pkl            # Mahsulotlar saqlanuvchi fayl (avtomatik yaratiladi)
├── README.md                  # Loyihaga izoh
```

---

## ▶️ Ishga tushirish

Terminal/konsolda:

```bash
python mahsulot_manager.py
```

---

## 📘 Dasturdan foydalanish

1. Dastur ishga tushgach, siz quyidagi menyuni ko‘rasiz:

   ```
   1. Mahsulotlarni ko‘rish
   2. Yangi mahsulot qo‘shish
   3. Mahsulotni o‘chirish
   0. Chiqish
   ```
2. Raqamni kiriting va ko‘rsatmalarga amal qiling.

---

## 🧠 Texnologiyalar

* `Python` (v3.7+)
* `pickle` moduli — obyektlarni faylga saqlash uchun
* `os.path` — fayl mavjudligini tekshirish

---

## 🚨 Eslatma (Xavfsizlik):

Pickle bilan ishlaganda **faqat ishonchli fayllarni** oching. Chunki `pickle.load()` noaniq fayldan ishlatilsa, zararli kodni ishga tushirishi mumkin.

---

## ✍️ Muallif

* Ism: Uktam (foydalanuvchi)
* Yordamchi: ChatGPT (OpenAI)

---

## 🗂 Fikrlar yoki takliflar?

Yangi funksiyalar yoki xatoliklar haqida fikringiz bo‘lsa, bemalol ayting — loyiha kengaytiriladi!
