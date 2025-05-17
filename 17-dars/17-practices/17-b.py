"""
Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
"""
savol = "Yoshingizni kiriting: "

while True:
  qiymat = input(savol).strip()  
  # if qiymat.lower() == 'exit' or qiymat.lower() == 'quite':
  if qiymat.lower() in ('exit', 'quite', 'stop', 'quit'): # in operatori yaxshiroq variant
    print("Dastur tugadi")
    break
  
  try:
    age = int(qiymat)
    if age<0 or age>100:
      raise ValueError("Yosh 0 bilabn 100 oralig'ida bo'lishi kerak!")
  except ValueError as e:
    if "invalit literal" in str(e).lower():
      print("Iltimos, faqat raqam kiriting!: ")
    else:
      print(e)
    continue
  
  if age<7 or age>65:
    price = 0
  elif 7 <=age<= 18:
    price = 15000
  else: 
    price = 25000
    
  # if price == 0:
  #   print("Sizga kirish bepul.") 
  # else:
  #   print(f"Sizga kirish {price} so'm.")
  # f-string boaln xam narhlarni chiqarish mumkin
  print(f"Sizga kirish {'bepul' if price == 0 else f'{price} so\'m'}.")

'''Example 2'''   
# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")
    