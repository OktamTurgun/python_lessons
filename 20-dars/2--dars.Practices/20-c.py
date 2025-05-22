"""
Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
"""
def aylana_info(radius):
    """Aylaning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya."""
    return {          
        'radius': radius,
        'diametr': 2 * radius,
        'perimetr': 2 * 3.14 * radius,
        'yuza': 3.14 * (radius ** 2)
    }
aylana = aylana_info(5)
print(f"Radiusi {aylana['radius']} ga teng bo'lgan aylananing: \n"
      f"{'-'*35}\n"
      f"Diametri: {aylana['diametr']} ga\n"
      f"Perimetri: {aylana['perimetr']} ga \n"
      f"Yuzasi esa: {aylana['yuza']} ga teng")
# Aylaning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya
# yozing. Funksiyani chaqirib, aylaning radiusini 5 ga teng qilib ko'ring.
print(aylana_info(5))


''''''
def aylana_info(radius, pi=3.14159):
    """Aylaning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya."""
    aylana = {
        'radius':radius,
        'diametr':2*radius,
        'perimetr': 2*radius*pi,
        'yuza':pi*radius**2
        }
    return aylana
javob = aylana_info(5)
print(f"Radiusi {javob['radius']} ga teng bolgan aylananing: \n"
      f"{'-'*35}\n"
      f"Diametri: {javob['diametr']} ga\n"
      f"Perimetri: {javob['perimetr']} ga \n"
      f"Yuzasi esa: {javob['yuza']} ga teng")

''''''
def circle_data(radius, pi=3.14159):
    """Aylaning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya."""
    aylana = {
        'radius': radius,
        'diametr': 2 * radius,
        'perimetr': 2 * radius * pi,
        'yuza': pi * radius ** 2
    }
    return aylana

circle = circle_data(5)
print(f"""Radiusi {circle['radius']} ga teng bo'lgan aylananing:
{"-" * 30}
Diametri: {circle['diametr']} ga
Perimetri: {circle['perimetr']} ga
Yuzasi esa: {circle['yuza']} ga teng""")