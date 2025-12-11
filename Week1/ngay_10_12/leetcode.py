

#2 Remove Duplicates from Sorted Array
class Solution2:
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
s = Solution2()
arr = [1,1,2,3,4,5,6,6,7]
s.removeDup(arr)
print(arr)
print("------------------------")

#3 Reverse String
class Solution3:
    def reversedString(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
s = Solution3()
arr = ["h","e","l","r","l","o"]
s.reversedString(arr)
print(arr)
print("------------------------")

#4 Add Digits
#Lấy 1 số công 2 chữ lại nếu số đó có 2 chữ số
#Nếu công lại mà vẫn có 2 chữ số thì quay lại công tiếp
class Solution4:
    def addDigits(self, num):
        while num >= 10:
            tong = 0

            while num > 0:
                tong += num % 10
                num //= 10
            num = tong
        return num
s = Solution4()
print(s.addDigits(46))
print("------------------------")

# tong = 38 % 10 = 8
# 38 // 10 = 3
#
# tong = 8
# num = 3
#
# tong = 3 % 10 = 3
# 3 // 10 = 0
#
# tong 3 + 8 = 11
#
# tong = 11
# num = 0
#
# tong += 11 % 10 = 1
# 11 // 10 = 1
#
# tong = 1
# num = 1
#
# tong += 1 % 10 = 1
# tong 1 + 1 = 2
#
# 1 // 10 = 0
# num = 0
#
# num = tong
# num = 2


# tong += 26 % 10 = 6
# 26 // 10 = 2
# 
# tong = 6
# num = 2
# 
# tong += 2%10 =2
# 2//10 = 0

#5 Palindrome Number
class Solution5:
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
s = Solution5()
print(s.number(121))
print(s.number(122))
print("------------------------")

# digit = x % 10 -> 121 % 10 = 1
# rs = rs * 10 + digit -> 0 * 10 + 1 = 1
# x = 121 // 10 = 12
#
# digit = 12 % 10 = 2
# rs = 1 * 10 + 2 = 12
# x = 12 // 10 = 1
#
# digit = 1 % 10 = 1
# rs = 12 * 10 + 1 = 121
# x = 1 // 10 = 0
#
# x = 242
# digit = x % 10 -> 242 % 10 = 2
# rs = rs * 10 + digit -> rs = 0 * 10 + 2 = 2
# x = 242 // 10 = 24
#
# digit = 24 % 10 = 4
# rs = 2 * 10 + 4 = 24
# x = 24 // 10 = 2
#
# digit = 2 % 10 = 2
# rs = 24 * 10 + 2 = 242
# x = 2 // 10 = 0

#6 Plus One
class Solution6:
    def plus_one(self, digits):
        n = len(digits)

        i = n-1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
            i -= 1
        return [1] + digits
s = Solution6()
print(s.plus_one([9]))

# nếu số cuối bằng 9 thì sẽ xuống else và bằng 0
# sau tiếp sẽ i-=1 là sang vị trị tiếp theo