class Solution:
    def lambda_map(self):
        nums = [1, 3, 5, 7, 9, 11, 13]
        squared = list(map(lambda x:x ** 2, nums))
        filtered = list(filter(lambda x: x > 10, squared))
        #Vì map hay filter cần 1 hàm nên phải cho lambda vào là cách tạo hàm nhanh
        #Là hàm dùng 1 lần không dùng cho hàm logic dài, phức tạp

        #kieu du lieu
        return squared, filtered