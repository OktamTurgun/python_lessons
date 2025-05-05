# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
countries = ['Pakistan', 'Bangladesh', 'Turkey', 'Japan', 'Indanesia', 'Turkmenistan', 'Avganistan']
# print(countries)

# Ro'yxatni uzunligini consolga chiqaring
length_count = len(countries)
# print(length_count) # 7

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
sorted_countries = sorted(countries)
# print(sorted_countries) # ['Avganistan', 'Bangladesh', 'Indanesia', 'Japan', 'Pakistan', 'Turkey', 'Turkmenistan']

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
reversed_countries = sorted(countries, reverse=True)
# print(reversed_countries) # ['Turkmenistan', 'Turkey', 'Pakistan', 'Japan', 'Indanesia', 'Bangladesh', 'Avganistan']

# Asl ro'yxatni qaytadan console'ga chiqaring
# print(countries) # ['Pakistan', 'Bangladesh', 'Turkey', 'Japan', 'Indanesia', 'Turkmenistan', 'Avganistan']

# reverse() methodi yordamida ro'yxatni ortidan boshlab chiqaring
countries.reverse()
# print(countries) # ['Avganistan', 'Turkmenistan', 'Indanesia', 'Japan', 'Turkey', 'Bangladesh', 'Pakistan']

# sort() methodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda console'ga chiqaring
countries.sort()
# print(countries) # ['Avganistan', 'Bangladesh', 'Indanesia', 'Japan', 'Pakistan', 'Turkey', 'Turkmenistan']
countries.sort(reverse=True)
print(countries) # ['Turkmenistan', 'Turkey', 'Pakistan', 'Japan', 'Indanesia', 'Bangladesh', 'Avganistan']
