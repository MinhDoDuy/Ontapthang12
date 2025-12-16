import random

def generate_numbers(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(1, 100))
    return nums

def analyze_numbers(nums):
    max_num = max(nums)
    min_num = min(nums)
    avg = sum(nums) / len(nums)
    return max_num, min_num, avg
