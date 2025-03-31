# students_data_processor.py

def main():
    no = int(input("Enter number of students: "))

    file = open('output_data.txt', 'w')

    for i in range(1, no + 1):
        print(f"For Student {i}:")
        name = input("Enter name: ")
        score = input("Enter the score: ")
        data_format = f"Name: {name} Score: {score}\n"
        file.write(data_format)

    file.close()

    try:
        read_file = open("output_data.txt", "r")
        data = read_file.read()
        print(data, end='')
        read_file.close()
    except FileNotFoundError:
        print("File 'output_data.txt' not found.")

if __name__ == "__main__":
    main()
