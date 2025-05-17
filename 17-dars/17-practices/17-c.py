"""
Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib
qolmoqda. Xatolarni to'g'rilay olasizmi?
"""
# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting: "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat.lower() == 'exit':
#       print("Dastur tugatildi!")
#       break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
'''try-except yordamida tekshiramiz'''
savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting: "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
      print("Dastur tugatildi!")
      break
    try:
      qiymat = float(qiymat)
      if qiymat < 0:
        print("Musbat son kiriting!")
        continue
      ildiz = qiymat ** 0.5
      print(f"{qiymat} ning ildizi {ildiz} ga teng")
    except ValueError:
      print("Iltomos, musbat son kiriting yoki 'exit' deb yozing!")  
      
