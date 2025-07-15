"""
Yoshni so'rab, tug'ilgan yilini hisoblovchi dastur yozing. 
Foydalanuvchi manfiy son yoki juda katta son kiritishga urinsa, xabar chiqsin.
"""
# Example: 1
try:
    age = int(input("Yoshingizni kiriting: "))
    if age < 0:
        raise ValueError("Xato! Yosh manfiy bo'lishi mumkin emas.")
    if age > 120:
        raise ValueError("Xato! Yosh 120 dan katta bo'lishi mumkin emas.")
    print(f"Siz {2025-age}-yilda tug'ilgansiz.")

except ValueError as e:
    if "invalid literal for int()" in str(e):
        print("Xato! iltimos, faqat butun son kiriting.")
    else:
        print(f"Xato! {e}")

else:
    print("Yoshingiz muvaffaqiyatli qabul qilindi")

finally:
    print("Dastur tugadi.")

# Example: 2 To'liq takomillashtirilgan versiya:
import datetime


def calculate_birth_year():
    current_year = datetime.datetime.now().year

    while True:
        try:
            age = input("\nYoshingizni kiriting (chiqish uchun 'exit'): ")
            if age.lower() == 'exit':
                print("Dastur tugatildi.")
                break

            age = int(age)

            if age < 0:
                raise ValueError("Yosh manfiy bo'lishi mumkin emas!")
            if age > 120:
                raise ValueError("Yosh 120 dan katta bo'lishi mumkin emas!")

            print(f"Siz {current_year-age}-yilda tug'ilgansiz.")
            print("Yoshingiz muvaffaqiyatli qabul qilindi")

        except ValueError as e:
            print(f"Xato: {e}" if str(e).startswith("Yosh") else
                  "Xato: Iltimos, faqat butun son kiriting (masalan: 25)")
        finally:
            print("---")


calculate_birth_year()
