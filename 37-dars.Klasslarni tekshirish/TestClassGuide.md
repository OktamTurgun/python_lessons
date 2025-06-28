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

# Python klasslarni test qilish: Ish tartibi (Qo'llanma)

Bu hujjat `unittest` yordamida klasslarni test qilish va terminalda testni ishga tushirish bo‘yicha bosqichma-bosqich qo‘llanmadir.

...

## 🔹 5-dars: `Cart` klassi bilan amaliy savatcha tizimi

**`cart.py`**:

```python
class Cart:
    def __init__(self):
        self.items = {}

    def add(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Miqdor musbat bo'lishi kerak.")
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove(self, product):
        if product in self.items:
            del self.items[product]
        else:
            raise ValueError("Mahsulot savatchada yo'q.")

    def update(self, product, quantity):
        if quantity < 0:
            raise ValueError("Miqdor manfiy bo'lishi mumkin emas.")
        if product not in self.items:
            raise ValueError("Mahsulot savatchada yo'q.")
        if quantity == 0:
            self.remove(product)
        else:
            self.items[product] = quantity

    def total_items(self):
        return sum(self.items.values())

    def clear(self):
        self.items.clear()
```

**`test_cart.py` (haqiqiy `Product` klassi bilan)**:

```python
import unittest
from cart import Cart
from product import Product

class TestCartWithProduct(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.apple = Product("Apple", 2.5, 100)
        self.banana = Product("Banana", 1.0, 50)

    def test_add_product(self):
        self.cart.add(self.apple, 3)
        self.assertEqual(self.cart.items[self.apple], 3)

    def test_add_product_twice(self):
        self.cart.add(self.apple, 2)
        self.cart.add(self.apple, 1)
        self.assertEqual(self.cart.items[self.apple], 3)

    def test_add_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add(self.apple, 0)

    def test_remove_existing(self):
        self.cart.add(self.apple, 1)
        self.cart.remove(self.apple)
        self.assertNotIn(self.apple, self.cart.items)

    def test_remove_nonexistent(self):
        with self.assertRaises(ValueError):
            self.cart.remove(self.banana)

    def test_update_quantity(self):
        self.cart.add(self.apple, 1)
        self.cart.update(self.apple, 5)
        self.assertEqual(self.cart.items[self.apple], 5)

    def test_update_zero(self):
        self.cart.add(self.apple, 2)
        self.cart.update(self.apple, 0)
        self.assertNotIn(self.apple, self.cart.items)

    def test_update_invalid_quantity(self):
        self.cart.add(self.apple, 2)
        with self.assertRaises(ValueError):
            self.cart.update(self.apple, -1)

    def test_update_nonexistent(self):
        with self.assertRaises(ValueError):
            self.cart.update(self.banana, 1)

    def test_total_items(self):
        self.cart.add(self.apple, 2)
        self.cart.add(self.banana, 3)
        self.assertEqual(self.cart.total_items(), 5)

    def test_clear_cart(self):
        self.cart.add(self.apple, 1)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)

if __name__ == "__main__":
    unittest.main()
```

---

## 🔸 Git Commit Qo‘llanma: `cart.py` va `test_cart.py` fayllari

### 1. Git staging:

```bash
git add cart.py test_cart.py
```

### 2. Eng yaxshi commit xabarlari:

#### Oddiy variant:

```bash
git commit -m "Add Cart class and unit tests"
```

#### Professional (to‘liq) variant:

```bash
git commit -m "Implement Cart class with full unit test coverage"
```

#### Conventional Commit uslubi:

```bash
git commit -m "feat(cart): create Cart class and unit tests"
```

| Teg        | Ma’nosi                      |
| ---------- | ---------------------------- |
| `feat`     | yangi imkoniyat              |
| `fix`      | xatolik tuzatish             |
| `test`     | faqat testlar                |
| `refactor` | kod tuzilmasini o‘zgartirish |

---

## 🌐 GitHub’ga push qilish (yuklash) tartibi

### 1. GitHub remote sozlash (faqat 1-marta kerak):

```bash
# Agar siz allaqachon remote qo‘shgan bo‘lsangiz, bu bosqichni o'tkazing.
git remote add origin https://github.com/username/repo.git
```

> Agar quyidagi xato chiqsa:
>
> ```
> error: remote origin already exists.
> ```
>
> bu degani siz allaqachon remote sozlagansiz. Qayta yozish shart emas.

### 2. Branch nomini tekshirish:

```bash
git branch
```

### 3. GitHub’ga push qilish:

```bash
git push origin main  # yoki master yoki boshqa branch nomi
```

### 4. GitHub’da tekshirish:

* Repozitoriyga kiring
* Fayllar va so‘nggi commit nomini ko‘ring

---