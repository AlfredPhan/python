#Program No.-4 Representation of Assignment Operator
name = input("What is your name: ")
option = input("Are you a student [y/n]? ")
message = f"Hello {name}"
# a+=5 means a= a+5 (a-=6 a=a-6), (a*=7 a=a*7)
if option == "y" or option == "Y":
    message += "-congrats, you are entitled to a 10% discount"
elif option =="n" or option == "N":
    message += " - sorry, you must pay the regular price"
else:
        message += " - You entered wrong, please re-enter y/n." 

print(message)
print()
input("Press return to continue ...")

