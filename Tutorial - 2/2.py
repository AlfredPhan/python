#2
name = input("What is your name? ")
student_str = input("Are you a student [y/n]? ")
student = student_str.lower() in ("y","yes")
age = int(input("How old are you? "))
message = f"Hello {name}"

if name.lower() == "chris":
    message += " - just give 30% discount"
else:
    message += " - just give 20% discount"
print(message)
print()
input("Press return to continue ...")
