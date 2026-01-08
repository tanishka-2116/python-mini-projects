
name = input("Enter student name: ")
marks = int(input("Enter marks out of 100: "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)
