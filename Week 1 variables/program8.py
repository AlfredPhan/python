#Program - 7 Random Value generation
"""
The purpose of randint library is to display the random integer
numbers between the given range.
randint is a module referenced function extracted from the random module
"""

from random import randint
min_str = input("Min: ")
max_str = input("Max: ")
minimum = int(min_str)
maximum = int(max_str)
random1 = randint(minimum, maximum)
random2 = randint(minimum, maximum)
random3 = randint(minimum, maximum)
random4 = randint(minimum, maximum)
random5 = randint(minimum, maximum)
#print(f"{random1} {random2} {random3} {random4} {random5}")
print("Random number 1: ", random1)
print("Random number 2: ", random2)
print("Random number 3: ", random3)
print("Random number 4: ", random4)
print("Random number 5: ", random5)
print()
print("Press return to continue ...")
