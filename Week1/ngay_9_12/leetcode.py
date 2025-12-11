class Solution:
    def fizzBuzz(self, n):
        result = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
s = Solution()
print(s.fizzBuzz(20))
print("1---------------------------")

class Solution2:
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")
s2 = Solution2()
print(s2.defangIPaddr("1.1.1.1"))
print(s2.defangIPaddr("255.100.50.0"))
print("2---------------------------")

class Solution3:
    def toLowerCase(self, s):
        return s.lower()
s3 = Solution3()
print(s3.toLowerCase("Hello"))
print(s3.toLowerCase("hEre"))
print("3---------------------------")

class Solution4:
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
s4 = Solution4()
print(s4.numJewelsInStones("b", "aAAbbbb"))
print(s4.numJewelsInStones("zZ", "ZZ"))
print("4---------------------------")

class Solution5(object):
    def sortArrayByParity(self, nums):
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
s5 = Solution5()
print(s5.sortArrayByParity([3,1,2,4,6,9]))
print(s5.sortArrayByParity([0]))
print("5---------------------------")

class Solution6:
    def signOfProduct(self, nums):
        product = 1
        for num in nums:
            product *= num
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
s6 = Solution6()
print(s6.signOfProduct([-1,-2,-3,-4,3,2,1]))
print(s6.signOfProduct([1,5,0,2,-3]))
print(s6.signOfProduct([-1,1,-1,1,-1]))
print("6---------------------------")

class Solution7:
    def subtractProductAndSum(self, n):
        product = 1
        total = 0

        for digit in str(n):
            product *= int(digit)
            total += int(digit)
        return product - total
s7 = Solution7()
print(s7.subtractProductAndSum(234))
print(s7.subtractProductAndSum(4421))
print("7---------------------------")