# List to store student data
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    gender = input('enter gender:')
    students.append((name, marks, gender))

print("\n--- Student Report ---")

total_marks = 0

for student in students:
    name = student[0]
    marks = student[1]
    gender = student[2]

    
    total_marks += marks
    
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    print("Name:", name, "| Marks:", marks, "| Grade:", grade,"| gender:",gender)

average = total_marks / n
print("\nClass Average:", average)

if average >= 75:
    print("Overall Performance: Good")
elif average <= 50:
    print('fail')
    
