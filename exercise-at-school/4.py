#program to get five marks of each subject of a student and calculate
#average %. then based on average point give grade as followrs:
#9,0 > -> D - distinction
#8 to 8.9 -> M - Merit
#7 to 7.9 -> A - First class
#6 to 6.9 -> B - Second
#5 to 5.9 -> C - Third
#less than 5 -> Fail
marks = []
for i in range(5):
    mark = float(input("Enter mark {}: ".format(i + 1)))
    marks.append(mark)

avg = sum(marks) / len(marks)
print("Student's average score is: {:.2f}".format(avg))

if avg >= 9.0:
    print("Grade is: D - Distinction")
elif 8.0 <= avg < 9.0:
    print("Grade is: M - Merit")
elif 7.0 <= avg < 8.0:
    print("Grade is: A - First class")
elif 6.0 <= avg < 7.0:
    print("Grade is: B - Second")
elif 5.0 <= avg < 6.0:
    print("Grade is: C - Third")
else:
    print("Grade is: Fail")
