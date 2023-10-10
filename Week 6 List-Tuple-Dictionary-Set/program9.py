#Program no 9 Using set and loop functions
from random import randint
def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{items}")
    print()
# temorarily fix the list parameters
minimum = 15
maximum = 30
n_randoms = 6

randoms = set() #empty set
while len(randoms) < n_randoms:
    r =randint(minimum,maximum)
    randoms.add(r)

print_list(randoms, "Unordered set")
sorted_randoms = list(randoms)
sorted_randoms.sort()
print_list(sorted_randoms, "Sorted list")

print()
input("Press return to continue...")
