"""
Yuqoridagi vazifani if-else yordamida qiling va natijani
ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
"""

python_dict = {
  # Asosiy tushunchalar
  'string': "matn (har qanday qo'shtirnoq ichidagi ifoda)",
  'integer': 'butun son',
  'float': "o'nlik son",
  'boolean': 'mantiqiy qiymat (True/False)',
  'None': "qiymat yo'qligini bildiradi",
  
  # Ma'lumot tuzilmalari
  'list': "ro'yxat (o'zgaruvchan, tartiblangan)",
  'tuple': "o'zgarmas ro'yxat",
  'dictionary': "lug'at (kalit:qiymat juftligi)",
  'set': "to'plam (taklifsiz, tartibsiz)",
  
  # Operatorlar
  'for': 'takrorlash operatori',
  'while': 'shartli takrorlash operatori',
  'if': 'shart operatori',
  'else': 'aks holda',
  'elif': 'aks holda, agar',
  'in': 'ichida borligini tekshirish operatori',
}
while True:
  kalit = input("Kalit so'z kiriting: (chiqish uchun 'exit' deb yozing) ").strip().lower()

  if kalit == 'exit':
     print("Dastur tugatildi!")
     break
  
  if not kalit:
     print("Hech narsa kiritilmadi! Iltimos, so'z kiriting: ")
     continue
  
  meaning = python_dict.get(kalit)

  if meaning:
     print(f"\n{kalit.title()} - {meaning.capitalize()} deb tarjima qilinadi")
  else:
     print(f"\nKechirasiz, '{kalit} so'zi lug'atda mavjud emas!'")
