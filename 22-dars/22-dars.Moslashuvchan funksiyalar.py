"""
Created on Fri May 25 11:04:42 2025

22-dars. Moslashuvchan funksiyalar (*args va **kwargs)

@author: uktam
"""
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
  """Bu funksiya avtomobil haqida ma'lumotlarni lug'at ko'rinishida qaytaradi."""
  avto = {
      'kompaniya':kompaniya,
      'model':model,
      'rang':rangi,
      'korobka':korobka,
      'yil':yili,
      'narh':narhi
      }
  return avto
avto1 = avto_info("BYD", 'song', 'qora', 'avtomat', 2024)
avto2 = avto_info("BMW", 'X7', 'qora', 'mexanika', 2025, 55000)
cars = [avto1, avto2]

print("Online bozordagi avtomobillar:")

for car in cars:
    if car['narh']:
        narh = car['narh']
    else:
        narh = "Nomalum"
    print(f"{car['rang'].title()} {car['kompaniya']} {car['model']} Narhi: {narh}")
    
''''''
def oraliq(min,max,step):
  """Berilgan oraliqdagi sonlarni ro'yxat ko'rinishida qaytaruvchi funksiya"""
  numbers = []
  while min<max:
      numbers.append(min)
      min += step
  return numbers
print(oraliq(0,10,2))
print(oraliq(10,21,3))

''''''
def summa(*nums):
    """Berilgan sonlarning yig'indisini hisoblaydigan funksiya
     *nums - moslashuvchan argument, bu funksiya chaqirilganda
     istalgan sonli argumentlarni qabul qiladi
     nums - o'zgarmas ro'yxat (tuple) ko'rinishida bo'ladi
    """
    total = 0 # tuple (o'zgarmas ro'yxat)
    for num in nums:
        total += num
    return total
print(summa(1, 2, 3, 4, 5))
print(summa(10, 20, 30))
print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))

''''''
def yigindi(x,y,*numbers):
    return x+y+sum(numbers)

print(yigindi(1, 2, 3, 4, 5, 6, 7, 8, 9)) # 45
print(yigindi(7, 8, 9)) # 24

print(yigindi(5)) # TypeError: yigindi() missing 1 required positional argument: 'y'

''''''
def avto_info(kompaniya, model, **malumotlar):
    """Avto haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info('BYD', 'Song', rang='qizil', yil=2024, narh=23000, korobka='avtomat')
avto2 = avto_info('Chevrolet', 'Spark', rang='oq', yil=2024, narh=8000)
avto3 = avto_info('Mercedes', 'G63SUV', rang='qora')
cars = [avto1, avto2, avto3]
for car, info in avto1.items():
    print(f"{car}: {info}")

''''''
# *args – Ixtiyoriy sonli pozitsion argumentlar
# *args – bu tuple sifatida ishlaydi. Nechta argument bersangiz, hammasi qabul qilinadi.
def yigindi(*args):
    """Berilgan sonlarning yig'indisini hisoblaydigan funksiya"""
    # args - o'zgarmas ro'yxat (tuple) ko'rinishida bo'ladi
    return sum(args)

print(yigindi(1, 2))          # 3
print(yigindi(1, 2, 3, 4))    # 10

''''''
# **kwargs – Ixtiyoriy sonli kalit-qiymat (keyword) argumentlar
# **kwargs – bu dictionary (lug'at) sifatida ishlaydi. Argumentlar kalit=qiymat 
# ko'rinishida uzatiladi.
def malumotlar(**kwargs):
  """Berilgan kalit-qiymat argumentlarini lug'at ko'rinishida qaytaruvchi funksiya"""
  for kalit, qiymat in kwargs.items():
      print(f"{kalit}: {qiymat}")

malumotlar(ism="Ali", yosh=25, kasb="Dasturchi")
malumotlar(kompaniya="BYD", model="Song", rang="qizil", yil=2024, narh=23000)
malumotlar(ism="Rustam", yosh=30, shahar="Toshkent", til="uzbek", kasb="Dasturchi")

''''''
# *args va **kwargs ni birgalikda ishlatish
def funk(*args, **kwargs):
    print("Pozitsionlar:", args)
    print("Kalit-qiymatlar:", kwargs)

funk(1, 2, 3, 4, 5, ism="Ali", yosh=25 , shahar="Toshkent", til="uzbek", kasb="Dasturchi")
result = funk(1, 2, 3, 4, 5, ism="Ali", yosh=25, shahar="Toshkent", til="uzbek", kasb="Dasturchi")
print(result)

''''''
# Funksiya ichida *args ni ajratib ishlatish:
def kopaytir(faktor, *sonlar):
  """Berilgan sonlarni faktor bilan ko'paytirib yangi ro'yxat qaytaruvchi funksiya"""
  return [faktor * son for son in sonlar] # 

print(kopaytir(2, 1, 2, 3, 4))  # [2, 4, 6, 8] 

''''''
# Funksiya ichida **kwargs ni ajratib ishlatish:
def avto_info(kompaniya, model, **malumotlar):
    """Avtomobil haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar
avto1 = avto_info('BYD', 'Song', rang='qizil', yil=2024, narh=23000, korobka='avtomat')

''''''
# **kwargs bilan default qiymatlarni aniqlash:
def sozlamalar(**kwargs):
    """Foydalanuvchi sozlamalarini qaytaruvchi funksiya"""
    # Default qiymatlarni aniqlash
    til = kwargs.get('til', 'uz')
    mavzu = kwargs.get('mavzu', 'dark')
    print(f"Til: {til}, Mavzu: {mavzu}")

sozlamalar(til='en') # 
sozlamalar(mavzu='light') #
sozlamalar(til='ru', mavzu='python') # Til: ru, Mavzu: python
'''
.get() metodi lug'atdan qiymat olishning xavfsiz usuli hisoblanadi. 
Agar oddiy kwargs['til'] deb yozsak va 'til' kaliti mavjud bo'lmasa, 
KeyError xatolik yuzaga keladi. .get() metodi esa xatolikka yo'l qo'ymaydi.

Bu usul dasturlashda sozlamalar (configurations) bilan ishlashda juda qulay, 
chunda foydalanuvchi ba'zi parametrlarni bermasa ham, dastur standart 
qiymatlar bilan ishlashda davom eta oladi.
'''

















