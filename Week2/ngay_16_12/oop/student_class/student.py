class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def info_Student(self):
        print("Tên: ", self.name)
        print("Age: ", self.age)
        print("Score: ", self.score)