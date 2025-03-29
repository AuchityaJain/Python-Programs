def main():
    students = []
    try:
        n = int(input("Enter no. of students: "))
        if n <= 0:
            print("Invalid Input\nHere's the list:\n", students)
            return

        for _ in range(n):
            name = input("Name: ")
            age = int(input("Age: "))
            if age <= 10 or age >= 80:
                print("Invalid Input\nHere's the list:\n", students)
                return
            students.append({"Name": name, "Age": age})

        while True:
            choice = input("Add more? (1/0): ")
            if choice == '1':
                n = int(input("Enter no. of students: "))
                if n <= 0:
                    print("Invalid Input\nHere's the list:\n", students)
                    return
                for _ in range(n):
                    name = input("Name: ")
                    age = int(input("Age: "))
                    if age <= 10 or age >= 80:
                        print("Invalid Input\nHere's the list:\n", students)
                        return
                    students.append({"Name": name, "Age": age})
            elif choice == '0':
                print("Here's the list of student details :")  # Corrected output
                for student in students:
                    print(student)
                sorted_students = sorted(students, key=lambda x: x["Name"])
                print("Here's the list of student details sorted with respect to name :")  # Corrected output
                for student in sorted_students:
                    print(student)
                return
            else:
                print("Invalid Input\nHere's the list:\n", students)
                sorted_students = sorted(students, key=lambda x: x["Name"])
                print("Here's the list of student details sorted with respect to name :")  # Corrected output
                for student in sorted_students:
                    print(student)
                return
    except ValueError:
        print("Invalid Input\nHere's the list:\n", students)

if __name__ == "__main__":
    main()
