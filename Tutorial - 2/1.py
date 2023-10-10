#1
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
<<<<<<< HEAD
cal = input("Enter the operation: (+,-,*,/) ")

if number2 == 0 and cal == "/":
    print("Answer can't divide by zero")
=======
cal = input("Enter the operation (+,-,*,/): ")

if number2 == 0 and cal == "/":
    print("Answer: you can't divide by zero")
>>>>>>> aa29dc55517a573992c801bb841c6fd8292d16d2
elif cal == "+":
    print("Answer: ",number1 + number2)
elif cal == "-":
    print("Answer: ",number1 - number2)
elif cal == "*":
    print("Answer: ",number1 * number2)
elif cal == "/":
    print("Answer: ",number1 / number2)
else:
<<<<<<< HEAD
    print("Invalid operation")
print()
input("Press return to continue ...")

=======
    print("Invalid result")

print()
input("Press return to continue ...")




    
>>>>>>> aa29dc55517a573992c801bb841c6fd8292d16d2
