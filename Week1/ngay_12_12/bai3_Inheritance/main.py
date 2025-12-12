from Inheritance import Employee, Animal, Dog, Cat



def main():
    e = Employee('Minh', 22, 200000, 'Dev')
    e.introduce()
    e.display_info()

    print("----------------------------")
    d = Dog()
    c = Cat()
    print("Chó kêu: ", d.make_sound())
    print("Mèo kêu: ", c.make_sound())

if __name__ == "__main__":
    main()

