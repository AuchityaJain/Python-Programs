###Do not change the provided code skeleton.

def main():
    ###Write the code here
    try:
        num_courses = int(input("Enter the number of courses: "))
    except ValueError:
        print("Invalid no. of courses")
        return

    if num_courses < 1:
        print("Invalid no. of courses")
        return

    passed_courses = []

    for _ in range(num_courses):
        course_name = input("Enter the name of the subject and marks respectively:\n")
        try:
            marks = int(input())
        except ValueError:
            print("Invalid mark")
            return

        if marks < 0 or marks > 100:
            print("Invalid mark")
            return

        if marks >= 80:
            passed_courses.append((course_name, marks))

    if passed_courses:
        print("The courses you have cleared are:")
        for course, mark in passed_courses:
            print(f"{course} {mark}")
    else:
        print("You have not cleared any courses with 80% or above.")

    return

if __name__ == '__main__':
    main()
