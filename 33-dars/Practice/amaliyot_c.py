"""
Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.
"""
import pickle

with open(r"pi_million_digits.txt") as file:
    pi = file.read().strip().replace("\n", "").replace(
        " ", "")  # Fayldagi matnni o'qib olamiz

# Tug'ilgan kunim pi da bormi?
bdate = "17072017"  # 17 Iyul, 2017-yil
if bdate in pi:
    print(f"Tug'ilgan kunim {(bdate)} π sonida mavjud.")
else:
    print(f"Tug'ilgan kunim {(bdate)} π sonida mavjud emas.")
print(bdate in pi)  # True or False

'''
# pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz

# with open('amaliyot/pi_float.dat','wb') as file:
#     pickle.dump(pi,file)
'''
pi_float = float(pi)  # matnni float (o'nlik) songa o'tkazamiz
with open('pi_float.dat', 'wb') as file:
    pickle.dump(pi_float, file)

# Faylni o'qish
with open('pi_float.dat', 'rb') as file:
    pi_from_file = pickle.load(file)
# Fayldan o'qilgan π soni: 3.141592653589793
print(f"Fayldan o'qilgan π soni: {pi_from_file}")
