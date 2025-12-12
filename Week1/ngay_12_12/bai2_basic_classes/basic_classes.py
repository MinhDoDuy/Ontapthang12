
class Solution:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
            print(f"Hi, I'm {self.name} and i'm {self.age} years old")

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def circumference(self):
        return 2 * math.pi * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.width + self.length)

    def is_square(self):
        return self.length == self.width