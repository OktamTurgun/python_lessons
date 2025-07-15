# else va finally bloklari

# Blok	                Tavsifi:
# try	                Xatoga olib kelishi mumkin bo‘lgan kod yoziladi
# except	              Xato yuz berganda bajariladigan kod yoziladi
# else	                try ichidagi kod xatosiz bajarilganda ishlaydi
# finally	              Xato bo‘lishi yoki bo‘lmasligidan qat’i nazar doim bajariladi

# Misol:
try:
    n = int(input("Son kiriting: "))
except ValueError:
    print("Xato: Butun son kiriting.")
else:
    print(f"{n} sonining kvadrati {n**2}")
finally:
    print("Dastur tugadi.")


# Xatoni o‘zgaruvchi sifatida olish
# MIsol:
try:
    x = int("hello")  # Bu yerda xato yuz beradi
except ValueError as e:  # Xatoni o'zgaruvchi sifatida olish (as e)
    print("Xato turi:", type(e))
    print("Xabar:", e)
else:
    print("Xato bo'lmasa bajariladi", x)

# O‘z xatongizni yaratish (raise)
# O'z xatolarimizni yaratish uchun `raise` operatoridan foydalanamiz.

# Misol 1:


def tekshir(yosh):
    if yosh < 0:
        raise ValueError("Yosh manfiy bo‘lishi mumkin emas.")
    print("Yosh:", yosh)


# tekshir(-5)

# Misol 2
def tekshir_bal(bal):
    if bal < 0 or bal > 100:
        raise ValueError("Ball 0 va 100 oralig'ida bo'lishi kerak!")
    elif bal >= 60:
        print(f"Tabriklayman! Siz imtihondan {bal} bilan o'tdingiz!")
    else:
        print(f"Afsus! Siz imtihondan {bal} bilan o'tolmadingiz!")


try:
    tekshir_bal(105)
except ValueError as xato:
    print(xato)

# Exercise: 1
# Oddiy kalkulyator yaratish


def kalkulyator(a, b, amal):
    try:
        if amal == '+':
            return a + b
        elif amal == '-':
            return a - b
        elif amal == '*':
            return a * b
        elif amal == '/':
            if b == 0:
                raise ZeroDivisionError("Nolga bo'lish mumkin emas!")
            return a / b
        else:
            raise ValueError(
                "Noto'g'ri amal! Iltimos, +, -, *, yoki / ni tanlang.")
    except (ZeroDivisionError, ValueError) as e:
        print(f"Xato: {e}")
        return None


# Example usage
result = kalkulyator(10, 0, '/')
if result is not None:
    print(f"Natija: {result}")

# Example 2
try:
    a = float(input("Birinchi son: "))
    b = float(input("Ikkinchi son: "))
    amal = input("Amal (+, -, *, /): ")

    if amal == '+':
        print(a + b)
    elif amal == '-':
        print(a - b)
    elif amal == '*':
        print(a * b)
    elif amal == '/':
        print(a / b)
    else:
        print("Noto'g'ri amal!")

except ValueError:
    print("Son kiritishda xato!")
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas!")
except:
    print("Noma'lum xato yuz berdi!")
