# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
even_numbers = list(range(120,1200,2))
# print(even_numbers) # 120, 122, 124, 126 ..., 1198

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
sum_numbers = sum(even_numbers)
# print(sum_numbers) # 355860

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
min_numbers = min(even_numbers)
max_numbers = max(even_numbers)
max_min_diff = max_numbers - min_numbers
# print(max_min_diff) # 1078

# Ro'yxatdagi elementlar sonini xisoblang
length_numbers = len(even_numbers)
# print(length_numbers) # 540

# Ro'yxatni boshidan , o'rtasidan, oxiridan 20 ta qiymatni console'ga chiqaring
first_20 = even_numbers[:20] 
last_20 = even_numbers[-20:]

middle_index = length_numbers // 2
middle_20 = even_numbers[middle_index -10 : middle_index + 10]

print(middle_index)
# print(first_20) # [120, 122, 124, 126, 128, 130, 132, ..., 158]
# print(last_20) # [1160, 1162, 1164, 1166, 1168, ..., 1198]
print(middle_20) # [640, 642, 644, 646, 648, 650, 652, 654, 656, 658, 660, 662, 664, 666, 668, 670, 672, 674, 676, 678]
