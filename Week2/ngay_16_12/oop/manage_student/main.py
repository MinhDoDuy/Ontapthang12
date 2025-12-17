from student import StudentManager

def show_menu():
    print("\n===============Menu===============")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Get All Student")
    print("4. Show the Best Student")
    print("0. Exit")

def input_score():
    while True:
        try:
            score = float(input("Enter Score (1-10): "))
            if 1 <= score <= 10:
                return score
            else:
                print("🛑 Score must be between 1-10")
        except ValueError:
            print("🛑 Please enter Numbers")

def input_age():
    while True:
        try:
            age = int(input("Enter Age (15-30): "))
            if 15 <= age <= 30:
                return age
            else:
                print("🛑 Age must be between 15-30")
        except ValueError:
            print("🛑 Please enter Numbers")

def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Choose Your Answer: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = input_age()
            score = input_score()
            manager.add_student(name, age, score)
            print("✅ Add Sucessfully")

        elif choice == '2':
            student = manager.get_all_students()
            if not manager.get_all_students():
                print("🛑 No Student Found")
                continue

            print("\nList Student")
            for s in student:
                print(s)

            name = input("\nEnter name Student to delete: ")

            before = len(manager.get_all_students())
            manager.remove_student(name)
            after = len(manager.get_all_students())
            if before == after:
                print("🛑 Student not Found")
            else:
                print("✅ Delete Successfully")

        elif choice == '3':
            if not manager.get_all_students():
                print("🛑 No Student Found")
            else:
                print("\nList of Student: ")
                for s in manager.get_all_students():
                    print(s)

        elif choice == '4':
            best = manager.get_best_students()
            if not best:
                print("Dont have any Best student here")
            else:
                print("\nStudent have the Best Score: ")
                for s in best:
                    print(s)

        elif choice == '0':
            print("Exit")
            break

        else:
            print("🛑 Please input number 1-4")

if __name__ == "__main__":
    main()
