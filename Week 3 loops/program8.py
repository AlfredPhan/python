#Program No.8 Mixing of looping and decision statements
name = input("What is your name? ")
while name != "":
    student_str = input("Are you a student [y/n]? ")
    student = student_str.lower() in ("y","yes")
    age = int(input("How old are you? "))
    message = f"Hello {name}"
    if student and (age <= 18 or age > 65):
        message += " - congratulations, you are entitled to a 20%"
    elif student or (age <= 18 or age > 65):
        message += " - congratulations, you are entitled to a 10%"
    else:
        message += " - sorry, you must pay the regular price"
    print(message)
    print()
    name = input("What is your name: ")
print()
input("Press return to continue ...")
