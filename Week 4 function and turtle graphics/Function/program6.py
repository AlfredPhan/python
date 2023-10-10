#Program No.6 Function with arguments and with return values
def input_int(value):
    string = input(value)
    number = int(string)
    return number

def cal(num1,num2,operation):
    if operation == "+":
        combination = num1 + num2
    elif operation == "-":
        combination = num1 - num2
    return combination

def output(para1,para2):
    print(f"{para1} {para2}")

num1 = input_int("First number: ")
num2 = input_int("Second number: ")
operation = input("Operation [+,-]: ")
combination = cal(num1, num2, operation)
output("Answer is: ",combination)
