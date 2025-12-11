#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
class Solution:
    def sortArraybyParity(self, nums):
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
s = Solution()
print(s.sortArraybyParity([2,3,4,5,6,6,7,8]))

#Defanging an IP Address
class Solution2:
    def defanginganIPAddress(self, address):
        return address.replace(".", "[.]")
s = Solution2()
print(s.defanginganIPAddress("1.1.1.1"))

#Fizz Buzz
# class Solution3:
#     def fizzBuzz(self, n):
#         result = []
#
#         for i in range(1, n+1):
#             if i % 3 == 0 and i % 5 == 0:
#                 result.append("FizzBuzz")
#             elif i % 3 == 0:
#                 result.append("Fizz")
#             elif i % 5 == 0:
#                 result.append("Buzz")
#             else:
#                 result.append(str(i))
#         return result
# s = Solution3()
# print(s.fizzBuzz(25))

#To Lower Case
class Solution4:
    def toLowerCase(self, s):
        return s.lower()

s = Solution4()
print(s.toLowerCase("Hello"))
print(s.toLowerCase("HEEEELOOOOO"))

#Count Odd Numbers in an Interval Range
class Solution5:
    def countOddNumbersinanIntervalRange(self, high, low):
        return (high + 1) // 2 - low // 2
s = Solution5()
low = int(input("Nhap Low: "))
high = int(input("Nhap High: "))
print(s.countOddNumbersinanIntervalRange(high, low))

#Smallest Even Multiple
class Solution6:
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return n
        else:
            return n * 2
s = Solution6()
n = int(input("Nhap n: "))
print(s.smallestEvenMultiple(n))

#Jewels and Stones
class Solution8:
    def jewelsandStones(self, jewels, stones):
        count = 0
        for st in stones:
            if st in jewels:
                count += 1
        return count
s = Solution8()
print("Số viên jewels trong stones là:" ,s.jewelsandStones("a", "aaAAaaAA"))

#Contains Duplicate
class Solution9:
    def containsDuplicate(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] == nums[i]:
                    return True
        return False
s = Solution9()
print(s.containsDuplicate([1,2,3,1]))  # True
print(s.containsDuplicate([1,2,3,4]))  # False
