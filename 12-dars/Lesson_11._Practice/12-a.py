"""
Xatolar bilan ishlash
"""
# Xato yozilgan code:
# son = float(input("Juft son kiriting: ")
# if son%2==0:
#     print("Bu son juft emas.')
# else:
#     print("Rahmat!"))

# To'g'irlangan code:
son = float(input("Juft son kiriting: ")) # SyntaxError: Bu yerda qavs yopilmay qolgan
if son%2==0:
    print("Bu son juft emas.") # SynrtaxError: " '!= "" Qo'shtirnoq xato yopilgan, bir xil '' yoki "" dan foydalaning
else:
    print("Rahmat!") # SyntaxError: Bu yerda xam ortiqcha qavs yopilgan