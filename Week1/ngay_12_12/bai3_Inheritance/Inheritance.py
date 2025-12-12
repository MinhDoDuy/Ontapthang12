class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

class Employee(Person):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age)
        self.salary = salary
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Position: {self.position}")


class Animal():
    def make_sound(self):
        print("Some genric animal sound...")

class Dog(Animal):
    def make_sound(self):
        return "Gau! Gau!"
class Cat(Animal):
    def make_sound(self):
        return "Meo! Meo!"

