# Python klasslarni test qilish: Ish tartibi (Qo'llanma)

Bu hujjat `unittest` yordamida klasslarni test qilish va terminalda testni ishga tushirish bo‘yicha bosqichma-bosqich qo‘llanmadir.

---

## 1. Test qilinadigan faylni tayyorlash

**`car.py`**:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.km = 0

    def get_info(self):
        return f"{self.make} {self.model} - {self.km} km"

    def add_km(self, km):
        if km < 0:
            raise ValueError("KM manfiy bo'lishi mumkin emas.")
        self.km += km
```

---

## 2. Test faylini yozish

**`test_car.py`**:

```python
import unittest
from car import Car

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Chevrolet", "Cobalt")

    def test_get_info(self):
        self.assertEqual(self.car.get_info(), "Chevrolet Cobalt - 0 km")

    def test_add_km(self):
        self.car.add_km(120)
        self.assertEqual(self.car.km, 120)

    def test_add_negative_km(self):
        with self.assertRaises(ValueError):
            self.car.add_km(-50)

if __name__ == "__main__":
    unittest.main()
```

---

## 3. Test faylini to‘g‘ri papkaga joylashtirish

Masalan:

```
C:\Users\User\Documents\GitHub\python_lessons\python_lessons\37-dars.Klasslarni tekshirish\
├── car.py
└── test_car.py
```

---

## 4. Terminalni kerakli papkaga moslash

Windows PowerShell yoki Terminal oching:

```powershell
cd "C:\Users\User\Documents\GitHub\python_lessons\python_lessons\37-dars.Klasslarni tekshirish"
```

Bu buyruq orqali siz terminal ish muhitini kerakli papkaga yo‘naltirasiz.

---

## 5. Testni ishga tushirish

```powershell
python test_car.py
```

Agar hammasi to‘g‘ri bo‘lsa, natija quyidagidek bo‘ladi:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---

## 6. Foydali buyruqlar

| Buyruq                | Maqsadi                                |
| --------------------- | -------------------------------------- |
| `cd "yo'l"`           | Terminal ishchi papkasini o‘zgartiradi |
| `dir`                 | Papkada mavjud fayllarni ko‘rsatadi    |
| `dir *.py`            | Faqat `.py` fayllarni ko‘rsatadi       |
| `python fayl_nomi.py` | Python faylni ishga tushiradi          |

---

## 7. Muammolar va yechimlar

| Xatolik                     | Sababi             | Yechimi                                                               |
| --------------------------- | ------------------ | --------------------------------------------------------------------- |
| `No such file or directory` | Fayl topilmadi     | Fayl nomini tekshiring, to‘g‘ri papkada turganini aniqlang            |
| `ModuleNotFoundError`       | Fayl importda xato | Fayl bir papkada ekaniga va to‘g‘ri nomlanganiga ishonch hosil qiling |

---

## 8. Tavsiya

* Fayl nomlarini aniq yozing: `car.py`, `test_car.py`
* Test fayl nomi `test_*.py` formatida bo‘lsin
* VS Code ichida ishlayotgan bo‘lsangiz, terminalni to‘g‘ri papkaga moslang

---

Bu qo‘llanma `unittest` asosida klasslarni test qilishni o‘rganayotgan foydalanuvchilar uchun mo‘ljallangan. Amaliyot orqali mustahkamlash tavsiya etiladi.

📁 Papka: `37-dars.Klasslarni tekshirish`
📂 Fayllar: `car.py`, `test_car.py`
