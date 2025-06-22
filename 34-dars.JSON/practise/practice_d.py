# json.dump() — Python obyektini JSON faylga yozish
# Amaliy topshiriq:
# Avval kitob dictionaryni quyidagicha yarating (agar oldingisi mavjud bo‘lsa, o‘shani oling):

# Uni json.dump() yordamida kitob.json nomli faylga yozing.

# indent=4 bo‘lishi shart (chiroyli format uchun).

# ✅ Kutilgan natija:
# Fayl yaratilsin: kitob.json
# Ichida kitob ma’lumotlari JSON ko‘rinishda bo‘lsin.
import json
from practice_c import kitob_obj

with open('kitob.json', 'w') as file:
  json.dump(kitob_obj,file,indent=4)
  
with open('kitob.json', 'r') as file:
  kitob_data = file.read()
  
print(type(kitob_data)) # <class 'str'>