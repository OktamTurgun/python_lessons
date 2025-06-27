def rotate(nums, k):
    n = len(nums)
    if n == 0:
        return
    k = k % n  # Agar k > n bo'lsa
    
    # 1. Butun ro'yxatni teskari qilish
    nums.reverse()
    
    # 2. Birinchi k elementni teskari qilish
    nums[:k] = nums[:k][::-1]
    
    # 3. Qolgan elementlarni teskari qilish
    nums[k:] = nums[k:][::-1]

# Test qilish uchun misollar
if __name__ == "__main__":
    # 1-test
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print(nums)  # [5, 6, 7, 1, 2, 3, 4]
    
    # 2-test
    nums = [-1, -100, 3, 99]
    k = 2
    rotate(nums, k)
    print(nums)  # [3, 99, -1, -100]
    
    # 3-test
    nums = []
    k = 3
    rotate(nums, k)
    print(nums)  # []
