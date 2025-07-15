"""
Created on Thu Fri 20 10:57:14 2025

33-dars. Fayllar bilan ishlash. Pickle

@author: uktam
"""
# Execise: 1. Faylga yozish
# faylnomi = 'new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2004
# with open(faylnomi, 'w') as file:
#   file.write(ism)
#   file.write(str(tyil))
  
# Execise: 2. Faylga yozish. 
filenomi = 'new_file,txt'
ism = 'Olimjon Xasanov'
tyil = 2004
with open(filenomi, 'w') as file:
    file.write(ism + '\n')
    file.write(str(tyil) + '\n')
    
# Execise: 3. Faylga yozish
with open(filenomi, 'a') as file:
    file.write('Alijon Valiyev ')
    file.write('2002-yil')

# Fileni o'qish
with open(filenomi, 'r') as file:
    for line in file:
        print(line.strip())  # Har bir qatorni tozalab chiqaramiz
        

