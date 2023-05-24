#Program No.8 use of logical operator
#in -> membership operator , and or
#not in -> Membership
name = input("What is your name? ")
student_str = input("Are you a student [y/n]? ")
student = student_str.lower() in ("y", "Y", "Yes")

age_str = input("How old are you? ")
age = int(age_str)
message = f"Hello {name}"
if student and age <=18 or age > 65:
    message += " - congratulations, you are entitled to a 10% discount"
elif age > 18 or age < 65:
    message += " - sorry, you must pay the regular price"
print(message)

print()
input("Press return to continue ... ")
