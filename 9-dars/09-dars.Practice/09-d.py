"""
Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing.
Ro'yxatni konsolga chiqaring
"""
# n_people = int(input("Bugun necha kishi bilan suxbat qildungiz? ").strip())
# names = []
# for n in range(n_people):
#   names.append(input(f"{n+1}-suxbat qilgan insoniz kim? ").title())
# print(f"Bugun: " + ' va ' .join(names),'bilan suxbat qildiz!')

"""
Yuqoridagi masalani biroz optimallashgan korinishda
"""
user_input = input("Bugun necha kishi bilan suxbat qildingiz? ").strip()
number_part = user_input.split()[0] # Faqat birinchi so'zni oladi (masalan: "3 kishi" >>> "3")

try:
  n_people = int(number_part) # Raqamga o'girish
except ValueError:
  print("Noto'g'ri kiritish! Faqat raqam kiriting (masalan: '3' yoki '3 kishi')")
  n_people = 0 # Agar raqam bo'lmasa 0 deb qabul qilamaiz

names = []
for n in range(n_people):
  names.append(input(f"{n+1}-suxbat qilgan insoniz kim? ").title())

if n_people == 0:
  print("Demak! bugun xech kim bilan suxbat qilmadingiz.")
elif n_people == 1:
  print(f"Bugun {names[0]} bilan suxbat qildingiz.")
elif n_people == 2:
  print(f"Bugun {names[0]} va {names[1]} bilan suxbar qildingiz.")
else:
  all_names_except_last = ", " .join(names[:-1])
  print(f"Bugun {all_names_except_last} va {names[-1]} bilan suxbat qildingiz.")
