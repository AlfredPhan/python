#2
name = input("What is your name? ")
<<<<<<< HEAD
student = input("Are you a student [y/n]: ")
student_str = student.lower() in ("y","yes")
message = f"Hello {name}"

if name.lower() in "chris":
    message += " - You gets a 30% discount"
else:
    message += " - You gets a 20% discount"
=======
student_str = input("Are you a student [y/n]? ")
student = student_str.lower() in ("y","yes")
age = int(input("How old are you? "))
message = f"Hello {name}"

if name.lower() == "chris":
    message += " - just give 30% discount"
else:
    message += " - just give 20% discount"
>>>>>>> aa29dc55517a573992c801bb841c6fd8292d16d2
print(message)
print()
input("Press return to continue ...")
