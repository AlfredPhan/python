#Program No .2
#Funtion definition should always be at the top of program
#the variables inside the ()paranthesis is called Parameters
def output(text, combination): #Formal Parameters
    print(f"{text} {combination}") #f string statement

number1 = int(input("First number: "))#First statement executiom
number2 = int(input("Second number: "))
operation = input("Operation [+,-,]: ")

if operation == "+": #Equality operator
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2


output("Answer:", combination) #Funtion Call
output("I said the answer is", combination) #Funtion Call
print()
#Program 8 Bug Scope

def input_and_convert(prompt, conversion_fn):
    String = input(prompt)
    number = conversion_fn(String)   #type casting
    return number

def calculate(number1,number2,operation) :
    if operation == "+":
        combination = number1 + number2
    elif operation == "-":
        combination = number1 - number2
    return combination

def output(parameter1, parameter2):
    print(f"{parameter1} {parameter2}")
    
number1 = input_and_convert("First name: ",int)

number2 = input_and_convert("Second name: ",int)
operation = input_and_convert("Operation[+,-]: ", str)

combination = calculate(number1, number2 , operation)
output("Answer:",a)#Bug Scope also called function scope error
output("Answer:",combination)
print()
input("Press return to continue...")
#Program No. 13
def input_and_convert(prompt, conversion_fn):
    string = input(prompt)
    number = conversion_fn(string)
    return number

def calculate(number1, number2, operation):
    if operation == "+":
        combination = number1 + number2
    elif operation == "-":
        combination = number1 - number2
    return combination

def output(parameter1, parameter2):
    print(f"{parameter1} {parameter2}")

number1 = input_and_convert("First number: ", int)
number2 = input_and_convert("Second number: ", int)
operation =  input_and_convert("Operation [+, -]:", str)
combination = calculate(number1, number2, operation)
output("Answer:", combination)

print()
input("press return to continue...")
