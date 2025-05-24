'''
Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir
matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 
'''
def capitalize_words(words):
  """Ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgartiradi"""
  # royxatni o'zgartirmaydi
  capitalized_words = []
  for word in words:
      capitalized_words.append(word.capitalize())
  return capitalized_words
  
fruits = ['olma', 'banan', 'apelsin']
capitalized_fruits = capitalize_words(fruits) 
print(capitalized_fruits) # ['Olma', 'Banan', 'Apelsin']

''''''
def katta_harf(royxat):
    """Ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgartiradi"""
    # royxatni o'zgartirmaydi
    yangi = royxat.copy()  # asl ro'yxatdan nusxa
    for i in range(len(yangi)):
        yangi[i] = yangi[i].capitalize()
    return yangi
names = ['john', 'alex', 'micheal']
print(katta_harf(names))      # ['John', 'Alex', 'Micheal']
print(names)               # ['john', 'alex', 'micheal']

''''''  
def katta_harf(royxat):
    """Ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgartiradi"""
  # royxatni o'zgartirmaydi
    return [x.capitalize() for x in royxat]
  
clothes = ['kofta', 'shim', 'kurtka']
print(katta_harf(clothes))      # ['Kofta', 'Shim', 'Kurtka']

''''''
def capitalize_words(words):
    """Ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgartiradi"""
    # royxatni o'zgartirmaydi 
    return [word.capitalize() for word in words]  
  
cars = ['toyota', 'bmw', 'mercedes']
capitalized_cars = capitalize_words(cars)   
print(capitalized_cars) # ['Toyota', 'Bmw', 'Mercedes']
