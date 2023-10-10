#3
<<<<<<< HEAD
from random import randint
name = input("What is your name? ")
random = randint(1,10)
message = f"Hello {name},your lucky number is {random} "
=======
#3.1
from random import randint
name = input("What is your name? ")
random = randint(1,10)
message = f"Hello {name}, your lucky number is {random} "
>>>>>>> aa29dc55517a573992c801bb841c6fd8292d16d2

if random == 3 or random == 9:
    message += "and you have won a price"
if random == 7:
    message += "and you have hit the jackpot"
print(message)
print()
input("Press return to continue ...")

<<<<<<< HEAD
=======
#3.2
>>>>>>> aa29dc55517a573992c801bb841c6fd8292d16d2
from random import randint
name = input("What is your name? ")
random = randint(1,10)
message = f"Hello {name}, your lucky number is {random} "

if random == 3 or random == 9:
    message += "and you have won a price"
elif random == 7:
    message += "and you have hit the jackpot"
print(message)
<<<<<<< HEAD
print()
input("Press return to continue ...")
=======
>>>>>>> aa29dc55517a573992c801bb841c6fd8292d16d2

