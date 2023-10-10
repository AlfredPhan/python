#Program No.8 Using loops with list
from random import randint
def print_list(items, header = None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()
min = 1
max = 50
n_randoms = 5
randoms = [] # initially 0 so len = 0
while len(randoms) < n_randoms: #0<5 if true i will go inside
    r = randint(min,max)
    if r not in randoms:
        randoms.append(r)
randoms.sort()
print_list(randoms,"RANDOM NUMBERS:")
