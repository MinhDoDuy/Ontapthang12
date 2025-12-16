from random_utils import generate_numbers, analyze_numbers

nums = generate_numbers(10)

max_num, min_num, avg = analyze_numbers(nums)

print("Danh sách số:", nums)
print("Số lớn nhất:", max_num)
print("Số nhỏ nhất:", min_num)
print("Trung bình:", avg)