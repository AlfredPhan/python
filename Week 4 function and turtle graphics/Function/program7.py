#Program No.7
#Passing names inside the function
def input_and_convert(prompt, conversation_fn):
    string = input(prompt)
    number = conversation_fn(string)  #type casting
    return number

def cal(fish, cornflake, teatray):
    if teatray == "+":
        flipflop = fish + cornflake
    elif teatray == "-":
        flipflop = fish - cornflake
    return flipflop

def output(para1,para2):
    print(f"{para1} {para2}")

#Calling the Function
num1 = input_and_convert("First number: ",int)

num2 = input_and_convert("Second number: ",int)

operation = input_and_convert("Operation [+,-]: ",str)

combination = cal(num1,num2,operation)

output("Answer: ",combination)
