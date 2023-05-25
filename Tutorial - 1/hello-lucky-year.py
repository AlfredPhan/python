#Tutorial - 1
#Hello Lucky Year

import random
name = input("What is your name? ")
year_of_birth = int(input("What year were you born? "))

lucky_year = random.randint(year_of_birth, year_of_birth + 70)
print("Hello",name,"your lucky year is: ",lucky_year)
