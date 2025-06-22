# json.dumps() — Python obyektini JSON matnga aylantirish
# Amaliy topshiriq:
# Kitob nomli dictionary yarating.

# Unda quyidagi ma’lumotlar bo‘lsin:

kitob = {
    "nomi": "Python darsi",
    "muallif": "Uktam Turgunov",
    "narx": 50000,
    "mavzular": ["OOP", "JSON", "Pickle"]
}
# Uni json.dumps() yordamida JSON formatga aylantiring.
# indent=4 bilan chiroyli chop eting.
# Natijani chop eting:

import json
kitob_json = json.dumps(kitob, indent=4)
print(kitob_json)