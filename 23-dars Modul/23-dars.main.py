"""
Created on Mon May 26 12:48:21 2025

23-dars. "Modullar"

@author: uktam
"""
# method 1: Importing the entire module
# import avto_info_modul 

# car1 = avto_info_modul.avto_info('BMW', 'X5', 'qora', 'avtomat', 2023, 50000)
# car2 = avto_info_modul.avto_info('Tesla', 'Model S', 'oq', 'avtomat', 2024, 80000)
# avto_info_modul.cars_print([car1, car2])

# method 2: Importing specific functions from the module
# import avto_info_modul as aim
# car1 = aim.avto_info('BMW', 'X5', 'qora', 'avtomat', 2023, 50000) 
# car2 = aim.avto_info('Tesla', 'Model S', 'oq', 'avtomat', 2024, 80000)
# car3 = aim.avto_info('Audi', 'A6', 'qizil', 'mexanika', 2022, 40000)
# aim.cars_print([car3, car1, car2])

# method 3: Importing specific functions with alias
from avto_info_modul import avto_info as ai, cars_print as cp
car4 = ai('Mercedes', 'C-Class', 'kulrang', 'avtomat', 2023, 60000)
car5 = ai('Lexus', 'RX', 'qora', 'avtomat', 2024, 70000)
cp([car4, car5])

# method 4: Importing all functions from the module
# * - barcha funksiyalarni import qiladi, Bunday usul rafsiya etilmaydi, 
# sababi barcha funksiyalarni import qiladi va bu nomlar to'qnashuviga olib kelishi mumkin. 
# from avto_info_modul import * 
# car6 = avto_info('Porsche', 'Cayenne', 'oq', 'avtomat', 2023, 90000)
# car7 = avto_info('Jaguar', 'F-Pace', 'qizil', 'avtomat', 2024, 85000) 
# cars_print([car6, car7])


