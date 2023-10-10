#Week-5 Debugging
#Program No.1 Getting input message using function parameters
def get_message(name,student,age):
    message = f"Hello {name}"
    if student and (age <= 18 or age > 65):
        message += " - congratulations , 20% discount"
    elif student or (age <= 18 or age > 65):
        message += " - congratulations , 10% discount"
    else: #adult and not student
        message += " - sorry, regular price"
    return message
name = input("What is your name? ")
student_str = input("Are you a student [y/n]? ")
student = student_str.lower() in ("y","yes")
age = int(input("How old are you? "))
message = get_message(name,student,age)
print(message)
