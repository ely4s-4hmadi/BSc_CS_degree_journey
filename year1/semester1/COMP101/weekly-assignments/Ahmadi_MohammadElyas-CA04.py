#Ahmadi_MohammadElyas  201792013  October2025  CA04.py
# Program to calculate final grades based on code and test marks with late penalties

print("Welcome To Assignment Grading System")

more_students = "y"
valid_grade_range = range(0, 101)
valid_late_days_range = range(0, 3)
student_id = 0

while more_students == "y":
    #Generaing the student ID#:
    student_id += 1
    print(f"student id: {student_id}")

    #Initialize total for 2 grades
    total = 0

    #Inner For loop for two grades (deterministic)
    for i in range(2):
        if i == 0:
           grade_name = "code grade"
        else: #i == 1
           grade_name = "test grade"

        grade = input(f"Enter the student's {grade_name} (0-100): ")
        while not grade.isdigit() or int(grade) not in valid_grade_range:
            print(f"Invalid input. Enter the student's {grade_name} as an integer between 0 and 100.")
            grade = input(f"Enter the student's {grade_name} (0-100): ")
        grade = int(grade)

        #Add the two grades to total
        total = total + grade

        #Also store the grades in variables for output
        if i == 0:
           code_grade = grade
        else:
            test_grade = grade

    #Asking for the Days Late:
    days_late = input("Enter the Student's days late for submission (0-2): ")
    while not days_late.isdigit() or int(days_late) not in valid_late_days_range:
        print("Invalid number. Days late must be 0, 1, or 2.")
        days_late = input("Enter the Student's days late for submission (0-2): ")
    days_late = int(days_late)


    #Calculations:
    raw_grade = total/2
    final_grade = raw_grade - (5*days_late)

    if final_grade < 0:
        final_grade = 0



    #Outputs:
    print()
    print(f"Student ID number: {student_id}")
    print(f"Student's code grade: {code_grade}")
    print(f"Student's test grade: {test_grade}")
    print(f"Student's raw grade: {raw_grade}")
    print(f"Student's late days of submission: {days_late} days")
    print(f"Student's final grade: {final_grade}")
    print()

    #Asking if the user want to continue:
    more_students = input("Do you want to process another Student? y/n: ").lower()
    while more_students not in ("y", "n"):
        print("Invalid input. Please enter only 'y' for yes or 'n' for no.")
        more_students = input("Do you want to process another student? y/n: ").lower()

    if more_students == "n":
        print("Program finished. Thanks for using the program.")