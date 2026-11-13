def student_report(name, sc, eng, math):
    total = sc + eng + math
    percentage = total / 3
    print("Name: ", name)
    print("Science: ", sc)
    print("English: ", eng)
    print("Math: ", math)
    print("Total_Marks: ", total)
    print("Percentage: ", percentage)

student_report("Britney", 93, 81, 89)

