def get_message(name, student, age, gender):

    message = f"Hello {name}"
    if age <= 18:
        message += " - congratulations, 20% discount"
    elif student or (age < 18 and gender=="female"):
        message += " - congratulations, 20% discount"
    else: # adult and not a student
        message += "- sorry, regular price"
    return message

name = input("What is your name? ")

gender = input("Female / Male / Other? ")

student_str = input("Are you a student [y/n]? ")
student = student_str.lower() in ("y", "yes")

age_str = input("How old are you? ")
age = int(age_str) # convert to integer

message = get_message(name, student, age, gender)

print(message)

print()
input("Press return to continue...")
