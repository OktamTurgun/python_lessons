
def avto_info(kompaniya, model, rang, korobka='avtomat', yil=None, narh=None):
  """
  Avtomobil haqida ma'lumotlarni lug'at ko'rinishida qaytaradi.
  
  Args:
      kompaniya (str): Avtomobil ishlab chiqaruvchi kompaniya nomi
      model (str): Avtomobil modeli
      rang (str): Avtomobil rangi
      korobka (str, optional): Uzatmalar qutisi turi. Defaults to 'avtomat'.
      yil (str, optional): Ishlab chiqarilgan yili. Defaults to None.
      narh (str, optional): Avtomobil narxi. Defaults to None.
  
  Returns:
      dict: Avtomobil haqida to'liq ma'lumotlarni o'z ichiga olgan lug'at
  """
  
  avto = {
      'kompaniya': kompaniya,
      'model': model,
      'rang': rang,
      'korobka': korobka,
      'yil':yil,
      'narh': narh
  }
  return avto


def cars_input():
  """
  Foydalanuvchidan avtomobillar haqida ma'lumotlarni qabul qilib, ro'yxat qaytaradi.
  
  Returns:
      list: Avtomobillar haqida ma'lumotlarni o'z ichiga olgan lug'atlar ro'yxati
  """
  cars = []
  while True:
      print("\nQuyidagi ma'lumotlartni kiriting:\n", end='')
      kompaniya=input("Ishlab chiqruvchi: ")
      model = input("Modeli: ")
      rang = input("Rangi: ")
      korobka = input("Korobka (avtomat/mexanika): ") or 'avtomat'
      yil = input("Yili: ")
      narh = input("Narhi: ")
      
      cars.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
      
      javob = input("Yana avtomabil qoshasizmi? (yes/no): ")
      if javob == 'no':
          break
      
  return cars
        
def cars_print(cars):
  """
  Avtomobillar ro'yxatini chiroyli shaklda konsolga chiqaradi.
  
  Args:
      cars (list): Avtomobillar haqida ma'lumotlarni o'z ichiga olgan lug'atlar ro'yxati
  
  Prints:
      Avtomobillar haqida formatlangan ma'lumotlar
  """
  print("\nSalonimizdagi avtolar:")
  for avto in cars:
        price = avto['narh'] if avto['narh'] else 'Noma\'lum'
        print(f"{avto['kompaniya']} {avto['model']}, {avto['yil']}-yil. Narhi: {price}$")


if __name__ == "__main__":
  avtolar = cars_input()
  cars_print(avtolar)
  
