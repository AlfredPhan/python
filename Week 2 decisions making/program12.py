#program No.12 Random generation of Values using random package
from random import randint
min_str = input("Min: ")
max_str = input("Max: ")
min = int(min_str)
max = int(max_str)
if max > min:
    random1 = randint(min,max)
    random2 = randint(min,max)
    random3 = randint(min,max)
    random4 = randint(min,max)
    print(f"{random1} {random2} {random3} {random4}")
elif max < min:
    print(f"{max} is less than {min}")
else:
    print(f"{max} and {min} are equal values")
print()
input("Press return to continue ...")
