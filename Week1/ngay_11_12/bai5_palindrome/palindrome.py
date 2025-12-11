class Solution:
    def number(self, x):
        if x < 0:
            return False

        og = x
        rs = 0

        while x > 0:
            digit = x % 10
            rs = rs * 10 + digit
            x //= 10

        if rs == og:
            return True
        else:
            return False