import math

x = 400
# Misollar math modulidan foydalanish
print(math.sqrt(x))  # 20.0 # x ning kvadrat ildizi

print(math.pow(5, 2))  # 25.0 # 5 ning kvadratini hisoblaydi

print(math.floor(4.7))  # 4 # 4.7 ni pastga qarab yaxlitlaydi

print(math.pi)  # 3.141592653589793 # Pi soni

print(math.e)  # 2.718281828459045 # Euler soni (e soni ya'ni tabiiy logarifmning asosiy soni)

print(math.factorial(5))  # 120 # 5 ning faktoriali (5! = 5 * 4 * 3 * 2 * 1)

print(math.isqrt(25))  # 5 # 25 ning butun kvadrat 

print(math.comb(5, 2))  # 10 # 5 ning 2 elementli kombinatsiyalar soni

print(math.gcd(48, 18))  # 6 # 48 va 18 ning eng katta umumiy bo'luvchisi

print(math.lcm(4, 6))  # 12 # 4 va 6 ning eng kichik umumiy ko'paytmasi

print(math.sin(math.pi / 2))  # 1.0 # Pi/2 ning sinus qiymati

print(math.log2(8))  # 3.0 # 8 ning 2 asosidagi logarifmi

print(math.log10(100))  # 2.0 # 100 ning 10 asosidagi logarifmi

print(math.ceil(4.2))  # 5 # 4.2 ni yuqoriga qarab yaxlitlaydi


def rectangle_area(length, width):
  """Returns the area of a rectangle given its length and width."""
  if length < 0 or width < 0:
      raise ValueError("Length and width cannot be negative")
  return length * width

y = 10
z = 20
print(rectangle_area(y, z))  # 200

def aylana_yuzi(radius):
  """Returns the area of a circle given its radius."""
  if radius < 0:
      raise ValueError("Radius cannot be negative")
  return math.pi * (radius ** 2)
r = 5
print(aylana_yuzi(r))  # 78.53981633974483

def kub_yuzi(tomonlar_uzunligi):
  """Returns the surface area of a cube given the length of its sides."""
  if tomonlar_uzunligi < 0:
      raise ValueError("Side length cannot be negative")
  return 6 * (tomonlar_uzunligi ** 2)
s = 3
print(kub_yuzi(s))  # 54
