#Program No.10 Default value in arguments
def input_and_convert(value,conversion_fn):
    string = input(value)
    number = conversion_fn(string)
    return number

def cal(num1,num2,operation = "+"):
    if operation == "+":
        combination = num1 + num2
    elif operation == "-":
        combination = num1 - num2
    return combination

def output(para1,para2):
    print(f"{para1} {para2}")

num1 = input_and_convert("First number: ",int)
num2 = input_and_convert("Second number: ",int)
operation = input_and_convert("Operation [+,-]: ",str)
combination = cal(num1,num2,operation)
output("Answer: ",combination)
addition = cal(num1,num2)
output("Sum: ",addition)
