from uaclient.api.u.pro.attach.auto.full_auto_attach.v1 import event


class Solution:
    def sort_Array_By_Parity(self, nums):
        # even = [x for x in nums if x % 2 == 0]
        # odd = [x for x in nums if x % 2 == 1]
        # return even + odd

        even = list(filter(lambda x: x % 2 == 0, nums))
        odd = list(filter(lambda x: x % 2 == 1, nums))
        return even + odd