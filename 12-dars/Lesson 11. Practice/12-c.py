"""
Xatolarni topish: 
"""
# Xato yozilgan code:
# x = float(input("Birinchi sonni kiriting: ")
# y = float(input("Ikkinchi sonni kiriting: ")
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}")
# else
#     print(f"{x}>{y}")

# To'g'irlangan code:
x = float(input("Birinchi sonni kiriting: ")) # SyntaxErrro: qayslar yopilmagan
y = float(input("Ikkinchi sonni kiriting: ")) # SyntaxErrro: qayslar yopilmagan
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f'{x}<{y}') # SyntaxError: Qo'shtirnoq ikki xil yozilgan, ikkisidan birini tanlab yozing
else: # Bu qatorda ikki nuqta ':' qolib ketgan
    print(f"{x}>{y}")