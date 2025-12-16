from student import StudentManager

manager = StudentManager()

# Thêm sinh viên
manager.add_student("Minh", 20, 9)
manager.add_student("An", 21, 8.5)
manager.add_student("Nam", 24, 8)
manager.add_student("Bình", 19, 9)

# In danh sách sinh viên
print("DANH SÁCH SINH VIÊN:")
for s in manager.get_all_students():
    print(s)

# In sinh viên điểm cao nhất
best_students = manager.get_best_students()

print("\nSINH VIÊN ĐIỂM CAO NHẤT:")
for s in best_students:
    print(s)
