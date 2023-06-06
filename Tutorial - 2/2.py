#2
name = input("What is your name? ")
student = input("Are you a student [y/n]: ")
student_str = student.lower() in ("y","yes")
message = f"Hello {name}"

if name.lower() in "chris":
    message += " - You gets a 30% discount"
else:
    message += " - You gets a 20% discount"
print(message)
print()
input("Press return to continue ...")
