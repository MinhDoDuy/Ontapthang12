#1. Máy tính 2 số
a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))

print("Addition a + b: ", a+b)
print("Subtraction	 a - b: ", a-b)
print("Multiplication a * b: ", a*b)
print("Division	a / b: ", a/b)
print("Modulus a % b: ", a%b)
print("Exponentiation a ** b: ", a**b)
print("Floor division a // b: ", a//b)
print("-----------------------------")

#2. Đếm ký tự trong chuỗi
n = input("Nhap chuoi: ")
print("so ky tu: ", len(n))
print("-----------------------------")

#3. Đếm số từ
text = input("Nhap chuoi: ")
word = text.split()
so_tu = len(word)

print("so tu trong cau la: ", so_tu)
print("----------------------------")

#4. Chương trình xử lý chuỗi
text1 = input("Nhập 1 câu: ").strip().lower()

words = text1.split()
so_tu = len(words)

so_chu_cai = 0
for ch in text1:
    if ch.isalpha():
        so_chu_cai += 1

print("Số từ:", so_tu)
print("Số chữ cái:", so_chu_cai)

