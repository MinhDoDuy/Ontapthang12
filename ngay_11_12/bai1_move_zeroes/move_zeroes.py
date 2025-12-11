#1 Move Zeroes
class Solution:
    def moveZeroes(self, nums):
        k = 0 #vị trí ghi tiếp theo
        i = 0 #vị trí duyệt mảng

        while i < len(nums):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
            i += 1

        while k < len(nums):
            nums[k] = 0
            k += 1
