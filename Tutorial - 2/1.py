#1
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
cal = input("Enter the operation (+,-,*,/): ")

if number2 == 0 and cal == "/":
    print("Answer: you can't divide by zero")
elif cal == "+":
    print("Answer: ",number1 + number2)
elif cal == "-":
    print("Answer: ",number1 - number2)
elif cal == "*":
    print("Answer: ",number1 * number2)
elif cal == "/":
    print("Answer: ",number1 / number2)
else:
    print("Invalid result")

print()
input("Press return to continue ...")




    
