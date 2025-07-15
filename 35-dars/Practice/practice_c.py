"""
Foydalanuvchidan ikkita son qabul qilib, ularning bo'linmasini 
hisoblovchi dastur yozing. Xatolarni (nolga bo'lish, son emas matn kiritish) to'g'ri boshqaring.
"""
# Example: 1
num1 = input('Birinchi sonni kiriting: ')
num2 = input('Ikkinchi sonni kiriting: ')
try:
    num1 = float(num1)
    num2 = float(num2)
    result = num1 / num2
except ValueError as e:
    if "could not convert" in str(e):
        print("Xato: Noto'g'ri format! Faqat son kiriting.")
except ZeroDivisionError as e:
    print(f"Xato: {e} - nolga bo'lish mumkin emas!")

else:
    print(f"{num1} / {num2} Natija: {result:.2f}")
finally:
    print("Dastur tugadi.")

# Example: 2
print("Ikki sonning bo'linmasini hisoblobchi dastur.")
print("Dastur to'xtashi uchun 'exit' deb yozing!")

while True:
    num1 = input("\nBirinchi sonni kiriting: ")
    if num1.lower() == "exit":
        break

    num2 = input("\nIkkinchi sonni kiriting: ")
    if num2.lower() == "exit":
        break

    try:
        num1 = float(num1)
        num2 = float(num2)

        if num2 == 0:
            raise ZeroDivisionError("Nolga bo'lish mumkin emas.")

        result = num1 / num2

    except ValueError:
        print("Xato! Iltimos, faqat raqam kiriting. (masalan: 16 yoki 2.5).")
    except ZeroDivisionError as e:
        print(f"Xato! {e}")
    else:
        if result.is_integer():  # Agar natija butun son bo'lsa
            print(f"Natija: {int(num1)} / {int(num2)} = {int(result)}")
        else:
            print(f"Natija: {num1} / {num2} = {result:.2f}")
    finally:
        print("---")
print("Dastur tugadi!")
