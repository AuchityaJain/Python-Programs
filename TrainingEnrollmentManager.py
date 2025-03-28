def main():
    ### Write your code here
    try:
        num_students = int(input("Enter the no of student details to be created: "))
    except ValueError:
        print("Invalid Input")
        return

    if num_students <= 0:
        print("Invalid Input")
        return

    student_list = []

    for _ in range(num_students):
        student = {}
        name = input("Name: ")
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Invalid Input")
            return
        location = input("location:")  # Corrected line

        if age <= 10 or age > 20:
            print("Invalid Input")
            return

        student["Name"] = name
        student["Age"] = age
        student["Location"] = location
        student_list.append(student)

    print("Here's the list of student details:")
    for student in student_list:
        print(student)

    search_location = input("Enter the training location: ")

    students_found = False
    for student in student_list:
        if student["Location"] == search_location:
            if not students_found:
                print(f"Student(s) enrolled in this training location:")
                students_found = True
            print(student["Name"])

    if not students_found:
        print("Invalid location")
    return

if __name__ == '__main__':
    main()
