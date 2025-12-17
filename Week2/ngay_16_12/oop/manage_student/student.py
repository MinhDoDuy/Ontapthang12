class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"Tên: {self.name}, Tuổi: {self.age}, Điểm: {self.score}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, score):
        self.students.append(Student(name, age, score))

    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def get_all_students(self):
        return self.students

    def get_best_students(self):
        if not self.students:
            return []
        max_score = max(s.score for s in self.students)
        return [s for s in self.students if s.score == max_score]


    #remotes / origin / main timf hieu - remote, local laf gif