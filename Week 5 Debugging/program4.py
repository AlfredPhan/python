#Question
#04RandomValues_validation has four problems:
#three are errors which will prevent the code from working;
#one is a bug which means that the code will not work as expected
#(it should output 5 random values between
# the minimum & maximum input by the user).

from random import randint

min_str = input("Min: ")
max_str = input("Max: ")
minimum = int(min_str)
maximum = int(max_str)

if maximum > minimum:
    random1 = randint(minimum, maximum)
    random2 = randint(minimum, maximum)
    random3 = randint(minimum, maximum)
    random4 = randint(minimum, maximum)
    random5 = randint(minimum, maximum)
    print(f"{random1} {random2} {random3} {random4} {random5}")
else:
    print(f"{maximum} is less than {minimum}")

print()
input("Press return to continue ...")
