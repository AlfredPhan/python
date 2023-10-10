#Program No.5 Using Same Function argument for two input values
def input_int(value):
    string = input(value)
    number = int(string) #type casting
    return number
def output(para1,para2):
    print(f"{para1} {para2}")

num1 = input_int("First number: ")
num2 = input_int("Second number: ")
operation = input("Operation [+,-]: ")
if operation == "+" :
    combination = num1 + num2
elif operation == "-":
    combination = num1 - num2
output("Answer: ",combination)
