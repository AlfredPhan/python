#Program No.3
#Direct passing the parameter inside Function
def output(para1,para2):
    print(f"{para1} {para2}")

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
operation = input("Operation [+,-]: ")

if operation == "+":
    combination = num1 + num2
elif operation == "-":
    combination = num1 - num2
#Calling the Function
output("Answer: ",combination)#Actual parameters passing
output(combination, "is the answer")
output("Is this version better?", "Yes, I think so")
output("This version is better:", True)
