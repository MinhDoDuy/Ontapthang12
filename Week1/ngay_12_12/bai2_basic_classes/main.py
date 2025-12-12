from basic_classes import Solution, Circle, Rectangle

def main():
    p = Solution('minhdo', 22)
    p.introduce()

    c = Circle(2)
    print("Area: ",c.area())
    print("Circumference: ", c.circumference())

    r = Rectangle(5, 2)
    print("Area: ", r.area())
    print("Perimeter: ", r.perimeter())

if __name__ == "__main__":
    main()

