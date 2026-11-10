# Student Grade Management System

student = {}


def add_student(name, roll_no):
    name = name.lower()
    student[name] = roll_no
    print(f"{name} : {roll_no}")


def search_student(name):
    roll_no = student.get(name.lower())

    if roll_no:
        print(f"{name} : {roll_no}")
    else:
        print("Student not found.")


def update_student(name, roll_no):
    if name in student:
        student[name] = roll_no
        print(f"{name} updated to roll no {roll_no}.")
    else:
        print("Student not found.")


def delete_student(name):
    if name in student:
        del student[name]
        print(f"{name} deleted.")
    else:
        print("Student not found.")


def gen_report(name, english, math, science):
    total = english + math + science
    percentage = total / 3

    print("\nStudent Details")
    print("Name:", name)
    print("English:", english)
    print("Math:", math)
    print("Science:", science)
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")


def main():
    while True:
        print("\nStudent Report")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_no = input("Enter roll no: ")
            add_student(name, roll_no)

        elif choice == "2":
            name = input("Enter student name: ")
            search_student(name)

        elif choice == "3":
            name = input("Enter student name: ")
            roll_no = input("Enter roll no: ")
            update_student(name, roll_no)

        elif choice == "4":
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == "5":
            name = input("Enter student name: ")
            english = int(input("Enter English marks: "))
            math = int(input("Enter Math marks: "))
            science = int(input("Enter Science marks: "))

            gen_report(name, english, math, science)

        elif choice == "6":
            print("Closing the program....")
            break

        else:
            print("Please enter a valid choice.")


if __name__ == "__main__":
    main()