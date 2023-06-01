#Program No.7 Displaying random number using for loop and f string
from random import randint
min = int(input("Min: "))
max = int(input("Max: "))
n_randoms = int(input("How many random numbers? "))
output = ""
for counter in range(n_randoms):
    output += f" {randint(min,max)}"
    #print(output,end="\n")
print(output)
print()
input("Press return to continue ...")
