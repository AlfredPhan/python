#Program No.10 Match builtin functions
from random import randint
def print_list(items, header = None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()
# temporarily fix the list parameters
minimum = 1
maximum = 50
n_randoms = 7

randoms = []
for counter in range(n_randoms):
    randoms.append(randint(minimum,maximum))
randoms.sort()
print_list(randoms)

mi = min(randoms)
ma = max(randoms)
s = sum(randoms)
average = s/len(randoms)
print(f"min = {mi} ")
print(f"max = {ma} ")
print(f"sum = {s} ")
print(f"avg = {average} ") 
