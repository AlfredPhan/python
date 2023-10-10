#Program No.4
#Passing the Function Arguments
def input_first_int():   #defining the function here
    num1 = int(input("First number: "))
    return num1

def input_second_int(): #defining the function here
    num2 = int(input("Second number: "))
    return num2

def output(para1,para2): #defining the function here
    print(f"{para1} {para2}")

num1 = input_first_int() #Function is called
num2 = input_second_int()
operation = input("Operation [+,-]: ")
if operation == "+":
    combination = num1 + num2
elif operation == "-":
    combination = num1 - num2
output(f"Answer is: ",combination)
