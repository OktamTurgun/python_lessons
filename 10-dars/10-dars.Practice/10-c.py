"""
Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
 "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
"""
# num1 = float(input("1-sonni kiriting: "))
# num2 = float(input("2-sonni kiriting: "))
# if num1 == num2:
#   print(f"Sonlar teng: {num1} = {num2}")
# elif num1 > num2:
#   print(f"{num1} katta {num2} dan")
# else:
#   print(f"{num1} kichik {num2} dan")

"""
Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga
 "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
"""
# number = int(input("Istalgan son kiriting: "))
# print("Manfiy son") if number<0 else print("Musbat son")

"""
Agar yuqoridagi kodni 0 holatini ham alohida ko'rsatish kerak bo'lsa:
"""
num = int(input("Istalgan son kiriting: "))
print("Manfiy son" if num < 0 else "Musbat son" if num > 0 else "Nol")
