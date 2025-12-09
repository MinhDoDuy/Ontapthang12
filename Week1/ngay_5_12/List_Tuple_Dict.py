#Bài 1: Tạo list 5 số
my_list = [4,5,6,3,1]
print("List:", my_list)
print("-------------------------")

#Bài 2: Tạo tuple tọa độ (x,y)
toa_do = (5,6)
print("Toa do tuple:", toa_do)
print("-------------------------")

#Bài 3: Tạo dict {ten: diem}
thuc_tap = {"Minh": 9.0, "Nghĩa": 10.0}
print(thuc_tap)
print("-------------------------")

#Các bài tập nhỏ
#Bài 4: Nhập n dựa trên list và tuple
n = int(input("Nhập số phần tử n: "))

list = []

for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    list.append(x)

tpl = tuple(list)

print("Tuple: ", tpl)
print("List: ", list)
print("-------------------------")

#Bài 5: Quản lý sinh viên dựa trên dict
n = int(input("Nhap so luong hoc sinh: "))
sinh_vien = {}

for i in range(n):
    ten = input(f"Nhap ten sinh vien {i+1}: ")
    diem = float(input(f"Nhap diem sinh vien {ten}: "))
    sinh_vien[ten] = diem

max_score = max(sinh_vien.values())
print("\nSinh vien co diem so cao nhat la: ")
for ten, diem in sinh_vien.items():
    if diem == max_score:
        print(f"{ten} la nguoi dat diem cao nhat la {diem}")
print("------------------------------")

#Bài 6: Quản lý sản phẩm
n = int(input("Nhap so luong san pham: "))
san_pham = {}

for i in range(n):
    ten = input(f"Nhap ten san pham {i+1}: ")
    gia = float(input(f"Nhap gia san pham {ten}: "))
    so_luong = int(input(f"Nhap so luong san pham {ten}: "))

    san_pham[ten] = {
        "gia" : gia,
        "so_luong" : so_luong
    }

tong_tien = 0
for ten, thong_tin in san_pham.items():
    tong_tien += thong_tin["gia"] * thong_tin["so_luong"]
print("tong so tien trong kho la: ",tong_tien)