#Program No.6 Conditional checking in elif
name = input("What is your name? ")
student_str = input("Are you a student [y/n]? ")
student = student_str.lower() in ("y", "yes", "YES")
age = int(input("How old are you? "))
message = f"Hello {name}"

if student:
    message += " - Sorry you are not eligible for Driv.License"
elif age >= 18:
    message += " - congratulations, Eligible for Driv.License"
else:
    message += " - No conditions you can drive"
print(message)
print()
input("Press return to continue ...")
