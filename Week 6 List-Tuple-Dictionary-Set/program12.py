#Program No.12 Random functions with list
from random import randint
def print_list(items, header = None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()

def get_min_v1(items):
    items.sort()
    return items[0]

def get_min_v2(items):
    small = items[0]
    for item in items[1:]:
        if item < small:
            small = item #every round new number will be small
    return small

def get_sum(items):
    total = 0
    for item in items:
        total += item #total = total + item
    return total

#temporarily fix the list parameters
minimum = 1
maximum = 50
n_randoms = 7
randoms = []
for countern in range(n_randoms):
    randoms.append(randint(minimum,maximum))
print_list(randoms)
a = get_min_v1(randoms)
print(f"get_min_v1 = " ,a)
print(f"get_min_v2 = {get_min_v2(randoms)}")
print(f"        min = {min(randoms)}")
print(f"get_sum = {get_sum(randoms)}")
print(f"    sum = {sum(randoms)}")
print()
input("Press return to continue...")


            

