"""
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z 
(atamani) kiriting (masalan integer, float, string, if, else va hokazo)
va har birining qisqacha tarjimasini yozing.
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
    
    # Funksiyalar
    'len()': "ro'yxat yoki matn uzunligini aniqlash funksiyasi",
    'range()': "ma'lum oraliqdagi sonlar ketma-ketligini yaratuvchi funksiya",
    'print()': 'chiqarish funksiyasi',
    'input()': 'kiritish funksiyasi',
    'type()': "ma'lumot turini aniqlash funksiyasi",
    
    # String metodlari
    '.lower()': "har bir harfni kichik harfga o'zgartiradi",
    '.upper()': "har bir harfni katta harfga o'zgartiradi",
    '.title()': "matndagi har bir so'zning birinchi harfini katta bilan yozadi",
    '.capitalize()': "matnning birinchi harfini katta bilan yozadi",
    '.strip()': "matn boshi va oxiridagi bo'shliqlarni olib tashlaydi",
    '.split()': "matnni bo'lib ro'yxatga aylantiradi",
    'join': ".join() metodi - ro'yxat elementlarini matnga birlashtiradi",
    
    # List metodlari
    '.append()': "ro'yxat oxiriga element qo'shish",
    '.insert()': "ro'yxatning istalgan joyiga element qo'shish",
    '.remove()': "ro'yxatdan elementni qiymati bo'yicha o'chirish",
    '.pop()': "ro'yxatdan indeks bo'yicha elementni o'chirib, uni qaytarish",
    '.sort()': "ro'yxatni tartiblash metodi",
    '.reverse()': "ro'yxatni teskari aylantirish metodi",
    '.copy()': "ro'yxatning nusxasini olish",
    '.count()': "ro'yxatdagi element sonini hisoblash",
    
    # Dictionary metodlari
    '.keys()': "lug'atdagi barcha kalitlarni qaytaradi",
    '.values()': "lug'atdagi barcha qiymatlarni qaytaradi",
    '.items()': "lug'atdagi barcha juftliklarni qaytaradi",
    '.get()': "kalit bo'yicha qiymatni qaytaradi (xato bermaydi)",
    '.update()': "lug'atni yangi juftliklar bilan yangilaydi",
    
    # OOP tushunchalari
    'class': 'sinf (obyektlar shabloni)',
    'object': 'obyekt (sinf namunasi)',
    'attribute': "xususiyat (obyekt o'zgaruvchisi)",
    'method': "metod (obyekt funksiyasi)",
    'inheritance': "meros olish",
    'polymorphism': "ko'p shakllilik",
    
    # Xatoliklar
    'SyntaxError': "sinta'tik xato",
    'IndexError': "noto'g'ri indeks",
    'KeyError': "lug'atda mavjud bo'lmagan kalit",
    'ValueError': "oto'g'ri qiymat",
    'TypeError': "noto'g'ri turdagi qiymat",
    'try-except': "xatoliklarni qo'llab-quvvatlash bloki"
}

"""
Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini
yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa,
"Bunda so'z mavjud emas" degan xabarni chiqaring.
"""
# kalit = input("Kalit so'z kiriting? ").lower()
# print(python_dict.get(kalit, "Bunday so'z mavjud emas!").capitalize())

# kalit = input("Kalit so'z kiriting? ")

# meaning = python_dict.get(kalit)
# if meaning == None:
#   print("Bunday so'z mavjud emas!")
# else:
#   print(f"{kalit.title()} {meaning}")


""" Ushbu kodni optimal ko'rinishi """

print("Python lug'atiga xush kelibsiz! (chiqish uchun 'exit' deb yozing)")

while True:
  kalit = input(" \nKalit so'z kiriting: ").strip().lower()

  if kalit == 'exit':
    print("dastur to'xtatildi!")
    break

  # Agar foydalanuvchi so'z kiritmasa
  if not kalit:
    print("Iltimos, so'z kiriting: ")
    continue

  # Barcha variantlarni bir vaqtda tekshirish
  variants = [kalit, f'.{kalit}', f'{kalit}()', f'.{kalit}()']
  found = False
  
  for variant in variants:
      if variant in python_dict:
          print(f"\n{variant.upper()}: \n{python_dict[variant].capitalize()}")
          found = True
          break
  
  if not found:
      print(f"\n'{kalit}' so'zi topilmadi!")
      
      # Qo'shimcha yordam
      similar = [word for word in python_dict.keys() if kalit in word]
      if similar:
          print(f"Shu so'zlarga o'xshashlar: {', '.join(similar[:3])}")
    