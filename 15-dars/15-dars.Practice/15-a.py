"""
Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo 
ketma-ketligida chiroyli qilib konsolga chiqaring. 
"""
python_dict = {
  'string': "matn (har qanday qo'shtirnoq ichidagi ifoda)",
  'integer': 'butun son',
  'float': "o'nlik son",
  'boolean': 'mantiqiy qiymat (True/False)',
  'none': "qiymat yo'qligini bildiradi",
  'list': "ro'yxat (o'zgaruvchan, tartiblangan)",
  'tuple': "o'zgarmas ro'yxat",
  'dictionary': "lug'at (kalit:qiymat juftligi)",
  'set': "to'plam (taklifsiz, tartibsiz)",
  'for': 'takrorlash operatori',
  'while': 'shartli takrorlash operatori',
  'if': 'shart operatori',
  'else': 'aks holda',
  'elif': 'aks holda, agar',
  'in': 'ichida borligini tekshirish operatori'
}

for key, value in sorted(python_dict.items()):
  print(f"{key.title()}: {value.capitalize()}")

# str.format() - yordamida formatlab chiqarish
print("\nPython izohli lug'ati:")
for key, value in sorted(python_dict.items()):
  #print("{:<10}: {}".format(key.title(), value.capitalize()))
  print(f"{key.title():<10}:{value.capitalize()}") # f"" string yordamida formatlash