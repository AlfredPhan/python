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
