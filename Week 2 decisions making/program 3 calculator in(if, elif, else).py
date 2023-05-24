#Program No.3 Calculator in (if, elif, else)
num1_str = input("First number: ")
num1 = int(num1_str)
num2_str = input("Second number: ")
num2 = int(num2_str)
operation = input("Operation [+,-,*,/]: ")
if operation == "+":
    combination = num1 + num2
elif operation == "-":
    combination = num1 - num2
elif operation == "*":
    combination = num1 * num2
elif operation == "/":
    combination = num1 / num2
elif operation == "%":
    combination = num1 % num2
else:
    print("Unknown operator symbol")
print(f"Answer: {combination}")
print()
input("Press return to continue ...")
