"""
calculator.py nomli modul yarating va unda quyidagi funksiyalar bo'lsin:
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)
- power(a, b)
- sqrt(a)

Keyin main.py faylda bu moduldan foydalanib, oddiy kalkulyator dasturi yozing.
"""

def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a* b
def divide(a, b):
  return a / b if b != 0 else "Nolga bo'lish mumkin emas!"
def power(a, b):
  return a ** b 
def sqrt(a):
  if a < 0:
    return "Manfiy sinning kvadrat ildizi mavjud emas!"
  return a ** 0.5


  
