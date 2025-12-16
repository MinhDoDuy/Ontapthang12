#new_list[<action> for <item> in <iterator> if <some condition>]

class Solution:
    def findNumbers(self, nums):
        s = [x for x in nums if len(str(x)) % 2 == 0]
        return len(s)