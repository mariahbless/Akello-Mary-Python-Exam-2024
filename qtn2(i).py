
student_name = input("Enter your the student's name here: ")
student_number = input("Enter the Student Number here: ")
programming = int(input("Enter the marks for programming here: "))
data_science = int(input("Enter the marks for data science here : "))
computer_application = int(input("Enter the marks for computer application here: "))

total_mark = programming + data_science + computer_application
number_of_courses = 3
average_mark = total_mark / number_of_courses
print(f"The average mark of the student  is: {average_mark:.3f}") #3f signifies that 3 decimal places
