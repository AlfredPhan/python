#Program No.2 (if, elif, else statements)
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
operation = input("Operation [+,*]: ")

if operation == "+":
    combination = num1 + num2
elif operation == "*":
    combination = num1 * num2
elif operation == "/":
    combination = num1 / num2
else:
    combination = num1 - num2

print(f"Answer: {combination}")
print()
input("Press return to continue ...")
