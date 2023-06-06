#Program No.16 Checking a prime number or not
#All natural numbers greater than 1 but not having more than two
#Factors such as multiple by 1 and the number itself is called
#Prime numbers
number = int(input("Enter the number to check: "))
if (number > 1):
    for i in range(2,number):
        if(number % i) == 0: #5%2 == 0
            print("The number is not a prime")
            break
        elif number == 2:
            print("The number is even prime")
    else:
        print("The number is not a prime")

print()
input("Press return to continue ...")
