#Program No.1 Decision Statements
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
operation = input("Operation: [+,-,*,/,%]: ")

#Decision making of conditional statements
#indentation -> space giving automatically with correct syntax
#== means equality operator
if operation == "+":
    combination = num1 + num2
if operation == "-":
    combination = num1 - num2
if operation == "*":
    combination = num1 * num2
if operation == "/":
    combination = num1 / num2
if operation == "%":
    combination = num1 % num2
print(f"Answer: {combination}")
print()
print("Press return to continue ...")

    
