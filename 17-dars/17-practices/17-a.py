"""
Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
"""
savol = "Yaxshi ko'rgan kitoblarizni kiriting: "
savol += "(Dasturni to'xtatish uchun 'stop' deb yozing) "
kitoblar = []

while True:
  book = input(savol).strip().title()
  if book.lower() == 'stop':
    print("Dastur tugadi!")
    break
  kitoblar.append(book)
  # print(book)

print("\nYour favourite books:")
for kitob in kitoblar:
  print(f" - {kitob}")
    
''''''   
# savol = "\nYaxshi ko'rgan kitoblarizni kiriting: "
# savol += "(Dasturni to'xtatish uchun 'stop' deb yozing) "    
# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!') 
    