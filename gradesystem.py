#student grade system
total = 500
name = input("Enter the name of student:  ")
print("Name:", name)

#getting the data
marks = float(input("Enter marks of your subject1: "))
marks2 = float(input("Enter marks of your subject2: "))
marks3 = float(input("Enter marks of your subject3: "))
marks4 = float(input("Enter marks of your subject4: "))
marks5 = float(input("Enter marks of your subject5: "))

#To calculate the total of all
total_marks = marks + marks2 + marks3 + marks4 + marks5
print(f"total_marks of the student: {total_marks}")

#calculate percentage
percentage = (total_marks/total)*100
print(f"total percentage of the student: {percentage:.2f}%")

#grading & pass/fail
if percentage >= 90:
    print("Grade: A and passed!")
elif percentage >= 80:
    print("Grade: B and passed!")
elif percentage >= 70:
    print("Grade: C and passed!")
elif percentage >= 60:
    print("Grade: D and passed!")
elif percentage < 35:
    print("Grade: F and failed the test!")




