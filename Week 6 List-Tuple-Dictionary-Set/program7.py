#Program No.7 Random Number generation using function in list
from random import randint
def print_list(items, header = None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()
min = int(input("Min: "))
max = int(input("Max: "))
n_randoms = int(input("How many random numbers? "))
randoms = [] #empty list
for counter in range(n_randoms):
    randoms.append(randint(min,max))
randoms.sort() #from low to high (Ascending order)
print_list(randoms, "LIST OF RANDOM NUMBER")
print()
input("Press return to continue ...")
