# json.loads() — JSON matndan Python obyektiga o‘tkazish
# Amaliy topshiriq:
# Quyidagi kitob_json matnini oling (bu siz chop etgan JSON string):

import json
from practice_b import kitob
kitob_json = '''
{
    "nomi": "Python darsi",
    "muallif": "Uktam Turgunov",
    "narh": 50000,
    "mavzular": ["OOP", "JSON", "Pickle"]
}
'''
# json.loads() yordamida uni yana Python obyektiga aylantiring.

# Obyekt ichidan "muallif" va "narx" qiymatlarini alohida chop eting.

kitob_obj = json.loads(kitob_json)
print(f"Muallif: {kitob_obj["muallif"]}")
print(f"Kitob narhi: {kitob_obj["narh"]} so'm")
print(kitob_obj)