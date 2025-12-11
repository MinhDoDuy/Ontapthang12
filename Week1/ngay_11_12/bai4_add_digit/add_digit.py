class Solution:
    def add_digit(self, num):
        while num >= 10:
            tong = 0

            while num > 0:
                tong += num % 10
                num //= 10
            num = tong
        return num
