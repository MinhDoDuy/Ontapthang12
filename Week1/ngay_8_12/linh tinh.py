# #1 Nối chuỗi
# fs_name = input("Nhap Ho: ")
# ls_name = input("Nhap Ten: ")
# 
# full_name = ls_name + " " + fs_name
# 
# print("Ho va ten: ", full_name)
# print("----------------------")
# 
# #2 Tính độ dài chuỗi
# text = input("Nhap vao 1 chuoi ky tu: ")
# length = len(text)
# 
# print("Chuoi ky tu: ", length)
# print("-----------------------")
# 
# #3 Viết hoa toàn bộ
# text1 = input("Nhap chuoi upper: ")
# upper_text1 = text1.upper()
# 
# print("Chuoi ky tu upper: ", text1.upper())
# print("-----------------------")
# 
# #4 Viết thường toàn bộ
# text2 = input("Nhap chuoi lower: ")
# lower_text2 = text2.lower()
# print("Chuoi ky tu lower: ", text2.lower())
# print("-----------------------")
# 
# #5 Thay thế chữ trong chuỗi
# text3 = input("Nhap chuoi goc: ")
# old = input("Nhap tu can thay the: ")
# new = input("Nhap tu moi: ")
# 
# result = text3.replace(old, new)
# print("Chuoi sau khi thay the: ", result)

#6 Viết hoa chữ cái đầu
text = input("Nhập câu: ")

# Tách câu thành danh sách từ
words = text.split()

new_words = []   # danh sách chứa từ sau khi xử lý

for w in words:
    if len(w) > 0:              # nếu từ không rỗng
        first = w[0].upper()    # chữ đầu viết hoa
        rest = w[1:]            # phần còn lại giữ nguyên
        new_w = first + rest    # ghép thành từ mới
        new_words.append(new_w) # push vào list
    else:
        new_words.append(w)

# Ghép list thành câu hoàn chỉnh
result = " ".join(new_words)

print("Kết quả:", result)




