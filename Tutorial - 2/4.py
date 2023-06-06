#4
name = input("What is your name? ")
roll_number = input("Enter the student's roll number: ")

subject_marks = []
for x in range(5):
    marks = float(input(f"Enter marks for subject {x+1}: "))
    subject_marks.append(marks)

total_marks = sum(subject_marks)
average_marks = total_marks / len(subject_marks)

marks_out_of_10 = [marks/10 for marks in subject_marks]

if average_marks >= 9.0:
    grade = "Distinction"
elif average_marks >= 8.0:
    grade = "Merit"
elif average_marks >= 7.0:
    grade = "First Class"
elif average_marks >= 5.0:
    grade = "Second Class"
else:
    grade = "Fail"

# Print results
print(f"Name: {name}")
print(f"Roll number: {roll_number}")
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks}")
print(f"Grade: {grade}")
print(f"Marks out of 10: {marks_out_of_10}")
    

