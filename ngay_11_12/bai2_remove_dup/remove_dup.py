class Solution:
    def removeDup(self, nums):
        if len(nums) == 0:
            return 0

        k = 1 #de so dau tien luon dung
        i = 1 #kiem tra tung so

        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
