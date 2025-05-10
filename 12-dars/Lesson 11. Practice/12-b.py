"""
Xatolar bilan ishlash
"""
# Xato yozilgan code:
# yosh = (input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")

# To'g'irlangan code:
yosh = int(input("Yoshingiz nechida? ")) # Kiritilgan son str edi int ga o'tkazildi

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18: # Bu yerda xam SyntaxError: bor edi ya'ni : ikki nuqta qolib ketgan
    narh = 10000
else:
    narh = 20000
print(f"Chipta narhi: {narh} so'm") # IndentationError: code qatori toto'g'ri surib qo'yilgan