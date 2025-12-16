from linhtinh import nums


class Solution:
    def even_list(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        n = [x for x in nums if x % 2 == 0]
        return n


