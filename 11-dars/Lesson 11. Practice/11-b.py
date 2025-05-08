"""
Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
Agar foydalanuvchi 7 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
"""
age = int(input("Yoshingiz nechida? "))
if age < 7 or age > 60:
  print("Kirish sizga bepul")
elif age < 18:
  print("Sizga kirish 10000 so'm")
else:
  print("Sizga kirish 20000 so'm")

''''''
age = int(input("Yoshingiz nechida? "))
if age < 7 or age > 60:
  narh = 0
elif age < 18:
  narh = 10000
else:
  narh = 20000
print(f"Sizga kirish {narh} so'm")

'''Ternary operator yordamida'''
age = int(input("Yoshingiz nechida? "))
narh = 0 if age < 7 or age > 60 else 1000 if age < 18 else 20000
print(f"Sizga kirish {narh} so'm")