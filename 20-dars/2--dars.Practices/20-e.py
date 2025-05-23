'''
Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta'rif: Har bir hadi o'zidan oldingi ikkita hadning yig'indisiga teng bo'lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang'ish had ko'pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
'''
# # Variant 1 
def fibonacci(n):
    """Fibonachchi ketma-ketligidagi n ta sonni qaytaruvchi funksiya."""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

'''''' 
# # Variant 2
# Eng samarali yechim
def fibonachchi(number):
    """Fibonachchi ketma-ketligidagi n ta sonni qaytaruvchi funksiya."""
    sonlar = []
    ## Fibonachchi ketma-ketligining dastlabki ikkita sonini belgilaymiz
    ## 0 va 1
    a, b = 0, 1
    ## Fibonachchi ketma-ketligidagi sonlarni hisoblaymiz
    ## va ro'yxatga qo'shamiz
    for _ in range(number):
        sonlar.append(a)
        a, b = b, a + b # a ga b ni, b ga a + b ni tenglaymiz
    ## Fibonachchi ketma-ketligidagi sonlarni qaytaramiz
    return sonlar
print(fibonachchi(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ''''''
# # Variant 3
def fibonachi(n):
  """Fibonachchi ketma-ketligidagi n ta sonni qaytaruvchi funksiya."""
  numbers = []
  for x in range(n):
    if x == 0 or x == 1:
      numbers.append(1)
    else:
      numbers.append(numbers[x-1] + numbers[x-2])
      
  return numbers
print(fibonachi(10))  # [1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonachi(20))

''''''
# # Variant 4
def fib(n):
    """Fibonachchi ketma-ketligidagi n ta sonni qaytaruvchi funksiya."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(fib(10)) 

''''''
# # Variant 5
def fibonacci(n):
    """Fibonachchi ketma-ketligidagi n ta sonni qaytaruvchi funksiya."""
    numbers = []
    a, b = 0, 1
    for _ in range(n):
        numbers.append(a)
        a, b = b, a + b
    return numbers