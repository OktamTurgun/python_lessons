# json.load() — JSON fayldan Python obyektiga o‘qish
# Amaliy topshiriq:
# kitob.json faylni oching.

# json.load() yordamida fayldagi JSON ma’lumotni Python obyektiga aylantiring.

# Obyektdan nomi va mavzular ni ekranga chiqaring.

# 🎯 Kutilgan natija:
# Kitob nomi: Python darsi
# Mavzular: ['OOP', 'JSON', 'Pickle']

import json
# JSON fayldan o'qish
with open('data/kitob.json', 'r') as file:
    kitob_obj = json.load(file)
# Obyektdan nomi va mavzularni chiqarish
print(f"Kitob nomi: {kitob_obj['nomi']}")
print(f"Mavzular: {kitob_obj['mavzular']}")


