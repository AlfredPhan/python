#3
from random import randint
name = input("What is your name? ")
random = randint(1,10)
message = f"Hello {name},your lucky number is {random} "

if random == 3 or random == 9:
    message += "and you have won a price"
if random == 7:
    message += "and you have hit the jackpot"
print(message)
print()
input("Press return to continue ...")

from random import randint
name = input("What is your name? ")
random = randint(1,10)
message = f"Hello {name}, your lucky number is {random} "

if random == 3 or random == 9:
    message += "and you have won a price"
elif random == 7:
    message += "and you have hit the jackpot"
print(message)
print()
input("Press return to continue ...")

