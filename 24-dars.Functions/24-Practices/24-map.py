"""
map funksiyasi yordamida ro'yxatdagi har bir sonning kvadratini hisoblash
"""

from typing import List


def kvadratlar(sonlar: List[int]) -> List[float]:
    """
    Ro'yxatdagi har bir sonning kvadratini hisoblaydi.

    Args:
        sonlar (List[int]): Sonlar ro'yxati

    Returns:
        List[float]: Har bir sonning kvadrati
    """
    return list(map(lambda x: x**2, sonlar))


kvadrat_sonlar = kvadratlar(list(range(10)))
print("Sonlar:", list(range(10)))
print("Sonlarning kvadrati:", kvadrat_sonlar)

# Map funksiyasi yordamida turli xil mashqlarni bajarish
words = [
    "hello",
    "world",
    "python",
    "map",
    "function",
    "example",
]

capitalized_words = list(map(lambda x: x.capitalized(), words))
print("So'zlar:", words)  # ['hello', 'world', 'python', 'map', 'function', 'example']
print(
    "So'zlar bosh harf bilan:", capitalized_words
)  # ['Hello', 'World', 'Python', 'Map', 'Function', 'Example']

"""Map funksiyasi yordamida so'zlarning uzunligini hisoblash""" ""


def uzunliklar(words: List[str]) -> List[int]:
    """
    Ro'yxatdagi har bir so'zning uzunligini hisoblaydi.

    Args:
        words (List[str]): So'zlar ro'yxati

    Returns:
        List[int]: Har bir so'zning uzunligi
    """
    return list(map(len, words))


soz_uzunliklari = uzunliklar(words)
print("So'zlar:", words)
print("So'zlarning uzunligi:", soz_uzunliklari)


# Fahrenheit dan Celsiusga o'tkazish
def fahrenheit_to_celsius(fahrenheit: List[float]) -> List[float]:
    """
    Fahrenheit darajasini Celsius darajasiga o'tkazadi.

    Args:
        fahrenheit (List[float]): Fahrenheit ro'yxati

    Returns:
        List[float]: Celsius ro'yxati
    """
    return list(map(lambda x: (x - 32) * 5 / 9, fahrenheit))


fahrenheit_values = [32, 50, 68, 86, 104]
celsius_values = fahrenheit_to_celsius(fahrenheit_values)
print("Fahrenheit:", fahrenheit_values)
print("Celsius:", celsius_values)

# example 2
fahrenheit = [32, 68, 86, 100, 212]
celsius = list(map(lambda f: (f - 32) * 5 / 9, fahrenheit))
print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)
# example 3


def celcius_to_fahreheit(celcius: list[float]) -> list[float]:
    """
    Celsius darajasini Fahrenheit darajasiga o'tkazadi.

    Args:
        celcius (list[float]): Celsius ro'yxati

    Returns:
        list[float]: Fahrenheit ro'yxati
    """
    return list(map(lambda c: (c * 9 / 5) + 32, celsius))


celsius_values = [0, 20, 37, 100]
fahrenheit_values = celcius_to_fahreheit(celsius_values)
print("Celsius:", celsius_values)
print("Fahrenheit:", fahrenheit_values)
