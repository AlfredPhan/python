#program No.11 Logical Not operator
name = input("What is your name? ")
student_str = input("Are you a student [y/n]? ")
student = student_str.lower() in ("y","yes")
age = int(input("How old are you? "))
adult = age > 18 and age <= 65 # if age is 90 F -> 0 22
message = f"Hello {name}"
# purpose of not operator is to do invertion
if student and not adult: #1 and 1 = 1
    message += " - congratulation, you are entitled to a 20% discount "
elif student or not adult:
    message += " - congratulations, you are entitled to a 10% discount "
else:
    message += "- sorry, you must pay the regular price"
print(message)
print()
input("Press return to continue ...")
