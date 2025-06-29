"""
19-dars: Python pprint kutubxonasi — Chiroyli va tartibli chiqarish
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda pprint (pretty print) kutubxonasi yordamida:
 - Katta hajmdagi lug‘at, ro‘yxat, JSON strukturalarni o‘qiladigan ko‘rinishda chiqarish
 - pprint() va pformat() funksiyalari
 - Amaliy mashqlar
"""

from collections import defaultdict
import json
import pprint

# 1. Murakkab dictionary
mahsulotlar = {
    "meva": ["olma", "banan", "nok"],
    "sabzavot": ["pomidor", "bodring", "kartoshka"],
    "ichimlik": {
        "gazli": ["cola", "fanta"],
        "suv": ["mineral", "oddiy"]
    }
}

print("Oddiy print():")
print(mahsulotlar)

print("\nChiroyli pprint.pprint():")
pprint.pprint(mahsulotlar)

# 2. pformat: matn sifatida saqlash
lugat_str = pprint.pformat(mahsulotlar)
print("\nMatn sifatida formatlangan:")
print(lugat_str)

# 3. Amaliy mashq: JSON struktura
json_data = '{"ism": "Ali", "yosh": 25, "manzil": {"shahar": "Toshkent", "kocha": "Yunusobod"}}'
data = json.loads(json_data)

print("\nJSON pprint:")
pprint.pprint(data)

# 4. Amaliy mashq: Ichma-ich ro‘yxatlar
murakkab = [
    {"id": 1, "status": "ok", "items": [1, 2, 3]},
    {"id": 2, "status": "error", "items": [4, 5, {"a": 10, "b": 20}]}
]
pprint.pprint(murakkab)

# 5. Amaliy mashq: API natijasi
api_response = {
    "user": {
        "id": 1001,
        "name": "Ali",
        "roles": ["admin", "editor"],
        "activity": {
            "last_login": "2025-06-28",
            "logins": ["2025-06-27", "2025-06-26", "2025-06-25"]
        }
    },
    "status": "success"
}
print("\nAPI javobi:")
pprint.pprint(api_response)

# 6. Amaliy mashq: Ko‘p satrli jadval
jadval = [
    {"talaba": "Ali", "fanlar": {"math": 90, "english": 85}},
    {"talaba": "Vali", "fanlar": {"math": 78, "english": 88}},
    {"talaba": "Sami", "fanlar": {"math": 92, "english": 91}},
]
print("\nTalabalar natijalari:")
pprint.pprint(jadval)

# 7. Amaliy mashq: Nested default value tuzilmasi
nested = defaultdict(lambda: defaultdict(list))
nested['class1']['students'].extend(["Ali", "Vali"])
nested['class2']['students'].append("Karim")
print("\nNested defaultdict:")
pprint.pprint(nested)
