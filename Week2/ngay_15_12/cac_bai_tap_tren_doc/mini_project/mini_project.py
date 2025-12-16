# Tạo list từ 1–50
# In các số chia hết cho 3 + bình phương các số đó bằng list comprehension

class Solution:
    def miniProject(self):
        return [x**2 for x in range(1,51) if x % 3 == 0 ]
