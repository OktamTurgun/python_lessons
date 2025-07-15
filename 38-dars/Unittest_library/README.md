# 18-dars: Python `unittest` kutubxonasi bilan test yozish

📅 Sana: 2025-06-28
✍️ Muallif: Uktam Turgunov

---

## 🎯 Maqsad

Ushbu darsda Python’ning `unittest` kutubxonasi yordamida:

* Test klassi yaratish
* Funksiyalarni avtomatik test qilish
* assertEqual, assertTrue, assertIn kabi test metodlari bilan tanishish
* Kod ishonchliligini oshirish

---

## 📦 Import qilish

```python
import unittest
```

---

## 🧪 Test qilinadigan funksiyalar

```python
def kvadrat(son):
    return son * son

def salom_ber(ism):
    return f"Salom, {ism.title()}!"
```

---

## 🧰 Test klassi va metodlar

```python
class TestMyFunctions(unittest.TestCase):
    def test_kvadrat(self):
        self.assertEqual(kvadrat(2), 4)
        self.assertEqual(kvadrat(-3), 9)
        self.assertNotEqual(kvadrat(5), 20)

    def test_salom_ber(self):
        self.assertEqual(salom_ber("ali"), "Salom, Ali!")
        self.assertIn("Salom", salom_ber("vali"))
```

---

## ▶️ Testni ishga tushurish

```python
if __name__ == '__main__':
    unittest.main()
```

---

## ✅ Asosiy test metodlari

| Metod                | Tushuntirish               |
| -------------------- | -------------------------- |
| assertEqual(a, b)    | a == b                     |
| assertNotEqual(a, b) | a != b                     |
| assertTrue(x)        | x rost bo‘lsa              |
| assertFalse(x)       | x yolg‘on bo‘lsa           |
| assertIn(a, b)       | a elementi b ichida bo‘lsa |
| assertIsNone(x)      | x `None` bo‘lsa            |

---

## 📝 Uyga vazifa

1. Ikki sonni qo‘shuvchi funksiya yarating va test yozing.
2. Berilgan son juftmi tekshiruvchi funksiya yozing va testlang.
3. `unittest` ni modullar bilan ajratilgan holatda ishlatishni o‘rganing.

---

## 📚 Qo‘shimcha

* Rasmiy hujjat: [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)
* Qo‘shimcha o‘rganish uchun: pytest, doctest

---
