from functools import reduce

"""
Mavzu: Practice. OOP boʻlimi uchun amaliy topshiriq
Muallif: Uktam Turgunov
Sana: 2025-07-07
Vazifa:
Sonlar ro'yxatini qabul qilib eng kattasini qaytaruvchi funksiya
"""

# Exercise: 1


def eng_katta(nums):
    """Sonlar ro'yxatini qabul qilib eng katta sonno qaytaruvchi funksiya"""
    return max(nums)


# test
print(eng_katta([5, 12, 23, 56, 87, 7, 0]))

# Alternativ yechimlar
# Exercise: 2


def eng_katta_2(nums):
    """max funksiyasiz eng katta sonni topish"""
    katta = nums[0]
    for son in nums[1:]:
        if son > katta:
            katta = son
    return katta


print(eng_katta_2([5, 12, 23, 56, 87, 7, 0]))

# Exercise: 3


def eng_katta_3(nums):
    """sort funksiyasi yordamida eng katta sonni topish"""
    return sorted(nums)[-1]


print(eng_katta_3([5, 12, 23, 56, 87, 7, 0]))

# Exercise: 4


def eng_katta_4(nums):
    """lambda va reduce yordamida eng katta sonni topish"""
    return reduce(lambda x, y: x if x > y else y, nums)


print(eng_katta_4([5, 12, 23, 56, 87, 7, 0]))

# Exercise: 5


def eng_katta_5(nums):
    """for va enumerate yordamida eng katta sonni topish"""
    katta = nums[0]
    for i, son in enumerate(nums):
        if son > katta:
            katta = son
    return katta


print(eng_katta_5([5, 12, 23, 56, 87, 7, 0]))
